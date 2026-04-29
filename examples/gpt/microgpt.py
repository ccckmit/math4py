"""GPT 模型 - 使用 math4py.tensor 梯度引擎实现。"""

import os
import math
import random
import numpy as np
from typing import List, Tuple, Optional

from math4py.tensor import Tensor
import math4py.tensor.function as F


def load_corpus(filepath: str) -> List[str]:
    """加载语料库。"""
    if not os.path.exists(filepath):
        return []
    with open(filepath, 'r', encoding='utf-8') as f:
        docs = [line.strip() for line in f if line.strip()]
    return docs


class Tokenizer:
    """简单的字符级分词器。"""

    def __init__(self, docs: List[str]):
        self.uchars = sorted(set(''.join(docs)))
        self.BOS = len(self.uchars)
        self.vocab_size = len(self.uchars) + 1
        print(f"vocab size: {self.vocab_size}")

    def encode(self, doc: str) -> List[int]:
        return [self.BOS] + [self.uchars.index(ch) for ch in doc] + [self.BOS]

    def decode(self, tokens: List[int]) -> str:
        result = []
        for t in tokens:
            if t == self.BOS:
                continue
            if t < len(self.uchars):
                result.append(self.uchars[t])
        return ''.join(result)


class SimpleGPT:
    """简化的 GPT 模型 - 正确维护梯度流。"""

    def __init__(self, vocab_size: int, n_embd: int = 32, n_layer: int = 2, block_size: int = 32):
        self.vocab_size = vocab_size
        self.n_embd = n_embd
        self.n_layer = n_layer
        self.block_size = block_size

        self._init_params()
        self.params = []
        self._collect_params()
        print(f"num params: {len(self.params)}")

    def _init_params(self):
        std = 0.1

        def matrix(nout, nin):
            return Tensor(
                np.random.randn(nout, nin) * std,
                requires_grad=True
            )

        # Token embedding 和 position embedding
        self.wte = matrix(self.vocab_size, self.n_embd)  # (vocab, embd)
        self.wpe = matrix(self.block_size, self.n_embd)  # (block, embd)
        self.lm_head = matrix(self.vocab_size, self.n_embd)  # (vocab, embd)

        # 层参数
        self.layers = []
        for i in range(self.n_layer):
            layer = {
                'wq': matrix(self.n_embd, self.n_embd),
                'wk': matrix(self.n_embd, self.n_embd),
                'wv': matrix(self.n_embd, self.n_embd),
                'wo': matrix(self.n_embd, self.n_embd),
                'mlp1': matrix(4 * self.n_embd, self.n_embd),
                'mlp2': matrix(self.n_embd, 4 * self.n_embd),
            }
            self.layers.append(layer)

    def _collect_params(self):
        self.params = [self.wte, self.wpe, self.lm_head]
        for layer in self.layers:
            for v in layer.values():
                self.params.append(v)

    def zero_grad(self):
        for p in self.params:
            if p.requires_grad:
                p.grad = np.zeros_like(p.data)

    def layer_norm(self, x: Tensor) -> Tensor:
        """RMSNorm"""
        mean = x.mean(axis=-1, keepdims=True)
        var = ((x - mean) ** 2).mean(axis=-1, keepdims=True)
        std = (var + 1e-5) ** 0.5
        return (x - mean) / std

    def embedding_lookup(self, token_ids: List[int]) -> Tensor:
        """Embedding lookup - 正确维护梯度流。"""
        # 從 wte 中取出對應的 embedding vectors
        embeddings = []
        for tid in token_ids:
            # 使用 __getitem__ 保持梯度連接
            emb = self.wte[tid]  # shape: (n_embd,)
            embeddings.append(emb.data)

        # 合併成矩陣
        emb_matrix = np.array(embeddings)
        result = Tensor(emb_matrix, requires_grad=True)
        result._children = [self.wte]

        def grad_fn(grad):
            # 將梯度累加到對應的 token embedding
            if self.wte.grad is None:
                self.wte.grad = np.zeros_like(self.wte.data)
            for i, tid in enumerate(token_ids):
                self.wte.grad[tid] += grad[i]

        result._grad_fn = grad_fn
        return result

    def positional_embedding(self, seq_len: int) -> Tensor:
        """Position embedding。"""
        pos_emb = self.wpe[:seq_len]  # 使用切片保持梯度
        return pos_emb

    def forward(self, token_ids: List[int]) -> Tuple[List[Tensor], List[Tensor]]:
        """前向传播。"""
        seq_len = len(token_ids)

        # Token embedding (保持梯度連接)
        tok_emb = self.embedding_lookup(token_ids)

        # Position embedding
        pos_emb = self.positional_embedding(seq_len)

        # 加入
        x = tok_emb + pos_emb
        x = self.layer_norm(x)

        # Transformer layers
        for li in range(self.n_layer):
            layer = self.layers[li]
            x_residual = x

            # Self-attention
            x = self.layer_norm(x)

            # Q, K, V
            q = x @ layer['wq'].T
            k = x @ layer['wk'].T
            v = x @ layer['wv'].T

            # Attention scores
            scores = q @ k.T / (self.n_embd ** 0.5)
            attn_weights = F.softmax(scores, axis=-1)
            x_attn = attn_weights @ v

            # Output projection
            x_attn = x_attn @ layer['wo'].T
            x = x_residual + x_attn

            # MLP
            x_residual = x
            x = self.layer_norm(x)
            x = x @ layer['mlp1'].T
            x = x.relu()
            x = x @ layer['mlp2'].T
            x = x_residual + x

        # LM head - 計算每個位置的 logits
        logits_list = []
        for i in range(seq_len):
            logits_i = x[i:i+1] @ self.lm_head.T  # shape: (1, vocab)
            logits_list.append(logits_i.reshape(-1))

        return logits_list

    def compute_loss(self, logits_list: List[Tensor], target_ids: List[int]) -> Tensor:
        """计算交叉熵损失。"""
        total_loss = None

        for logits, target_id in zip(logits_list, target_ids):
            # Softmax
            probs = F.softmax(logits.reshape(1, -1), axis=-1)

            # 取出目標類別的機率
            prob_target = probs[0, target_id]

            # NLL loss
            nll = -prob_target.log()

            if total_loss is None:
                total_loss = nll
            else:
                total_loss = total_loss + nll

        return total_loss / len(logits_list)

    def generate_one(self, token_id: int, pos_id: int, temperature: float = 0.8) -> int:
        """生成下一个 token。"""
        # Token embedding
        tok_emb = self.wte[token_id:token_id+1]  # shape: (1, n_embd)

        # Position embedding
        if pos_id < self.block_size:
            pos_emb = self.wpe[pos_id:pos_id+1]
        else:
            pos_emb = Tensor(np.zeros((1, self.n_embd)), requires_grad=False)

        x = tok_emb + pos_emb
        x = self.layer_norm(x)

        # Transformer layers (不保留梯度)
        for li in range(self.n_layer):
            layer = self.layers[li]
            x_residual = x

            x = self.layer_norm(x)

            q = x @ layer['wq'].T
            k = x @ layer['wk'].T
            v = x @ layer['wv'].T

            scores = q @ k.T / (self.n_embd ** 0.5)
            attn_weights = F.softmax(scores, axis=-1)
            x_attn = attn_weights @ v
            x_attn = x_attn @ layer['wo'].T
            x = x_residual + x_attn

            x_residual = x
            x = self.layer_norm(x)
            x = x @ layer['mlp1'].T
            x = x.relu()
            x = x @ layer['mlp2'].T
            x = x_residual + x

        # LM head
        logits = (x @ self.lm_head.T).reshape(-1)

        # Temperature scaling and softmax
        logits = logits / temperature
        probs = F.softmax(logits.reshape(1, -1), axis=-1).reshape(-1)

        probs_np = probs.data
        probs_np = probs_np / probs_np.sum()
        next_token_id = np.random.choice(self.vocab_size, p=probs_np)

        return next_token_id


def adam_update(params, grads, m, v, step, lr=0.001, beta1=0.9, beta2=0.99, eps=1e-8):
    """Adam 优化器更新。"""
    lr_t = lr * (1 - step / 1000)

    for i, (p, g) in enumerate(zip(params, grads)):
        m[i] = beta1 * m[i] + (1 - beta1) * g
        v[i] = beta2 * v[i] + (1 - beta2) * g ** 2
        m_hat = m[i] / (1 - beta1 ** (step + 1))
        v_hat = v[i] / (1 - beta2 ** (step + 1))
        p.data -= lr_t * m_hat / (v_hat ** 0.5 + eps)


def train(model, docs, tokenizer, num_steps=300):
    """训练模型。"""
    m = [0.0] * len(model.params)
    v = [0.0] * len(model.params)

    for step in range(num_steps):
        doc = docs[step % len(docs)]
        tokens = tokenizer.encode(doc)
        n = min(model.block_size, len(tokens) - 1)

        logits_list = model.forward(tokens[:n])
        target_ids = tokens[1:n+1]
        loss = model.compute_loss(logits_list, target_ids)

        model.zero_grad()
        loss.backward()

        grads = []
        for p in model.params:
            if p.grad is not None:
                grads.append(p.grad.copy())
            else:
                grads.append(np.zeros_like(p.data))

        adam_update(model.params, grads, m, v, step, lr=0.001)

        if (step + 1) % 50 == 0:
            loss_val = float(loss.data) if loss.data.ndim == 0 else float(loss.data.sum())
            print(f"step {step+1:4d} | loss {loss_val:.4f}")

    return model


def generate_samples(model, tokenizer, num_samples=10, temperature=0.8):
    """生成样本。"""
    print("\n--- generated samples ---")
    for i in range(num_samples):
        token_id = tokenizer.BOS
        sample = []

        for pos in range(model.block_size):
            next_id = model.generate_one(token_id, pos, temperature)
            if next_id == tokenizer.BOS:
                break
            if next_id < len(tokenizer.uchars):
                sample.append(tokenizer.uchars[next_id])
            token_id = next_id

        print(f"sample {i+1:2d}: {''.join(sample)}")


def main():
    random.seed(42)
    np.random.seed(42)

    corpus_path = "/Users/Shared/ccc/project/math4py/_data/corpus.txt"

    if os.path.exists(corpus_path):
        docs = load_corpus(corpus_path)
        random.shuffle(docs)
        print(f"num docs: {len(docs)}")
    else:
        docs = ["alice", "bob", "charlie", "david", "emma", "frank", "grace", "henry"]
        print(f"Using default docs: {docs}")

    tokenizer = Tokenizer(docs)

    model = SimpleGPT(
        vocab_size=tokenizer.vocab_size,
        n_embd=32,
        n_layer=2,
        block_size=32,
    )

    print("\n--- training ---")
    model = train(model, docs, tokenizer, num_steps=1000)

    generate_samples(model, tokenizer, num_samples=15, temperature=0.8)


if __name__ == "__main__":
    main()
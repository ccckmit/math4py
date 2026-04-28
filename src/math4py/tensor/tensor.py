"""張量物件 - 支援梯度和反向傳播的 numpy 封裝。"""

import numpy as np
from typing import Optional, Callable, List


class Tensor:
    """張量類別，支援自動微分。"""
    
    def __init__(self, data, requires_grad: bool = False):
        """初始化張量。"""
        if isinstance(data, np.ndarray):
            self.data = data.copy()
        else:
            self.data = np.array(data, dtype=np.float64)
        
        self.requires_grad = requires_grad
        self.grad = None
        self._grad_fn = None
        self._children = []
        
        if requires_grad:
            self.grad = np.zeros_like(self.data)
    
    def __repr__(self):
        return f"Tensor(shape={self.shape}, requires_grad={self.requires_grad})"
    
    @property
    def shape(self):
        return self.data.shape
    
    def backward(self, gradient: Optional[np.ndarray] = None):
        """反向傳播，計算梯度。"""
        if not self.requires_grad:
            return
        
        if gradient is None:
            if self.data.size != 1:
                raise RuntimeError("只有標量張量可以不用指定 gradient 直接呼叫 backward()")
            gradient = np.ones_like(self.data)
        
        # 使用拓撲排序進行反向傳播
        topo = []
        visited = set()
        
        def build_topo(v):
            if v not in visited:
                visited.add(v)
                for child in v._children:
                    build_topo(child)
                topo.append(v)
        
        build_topo(self)
        
        # 初始化梯度
        self.grad = gradient
        
        # 反向遍歷計算圖
        for v in reversed(topo):
            if v._grad_fn is not None and v.grad is not None:
                v._grad_fn(v.grad)
    
    def zero_grad(self):
        """將梯度歸零。"""
        if self.grad is not None:
            self.grad = np.zeros_like(self.grad)
    
    def __add__(self, other):
        """張量加法。"""
        if not isinstance(other, Tensor):
            other = Tensor(other)
        
        result_data = self.data + other.data
        result = Tensor(result_data, requires_grad=self.requires_grad or other.requires_grad)
        result._children = [self, other]
        
        if result.requires_grad:
            def grad_fn(grad):
                if self.requires_grad:
                    self.grad = grad.copy() if self.grad is None else self.grad + grad
                if other.requires_grad:
                    other.grad = grad.copy() if other.grad is None else other.grad + grad
            result._grad_fn = grad_fn
        
        return result
    
    def __mul__(self, other):
        """張量逐元素乘法。"""
        if not isinstance(other, Tensor):
            other = Tensor(other)
        
        result_data = self.data * other.data
        result = Tensor(result_data, requires_grad=self.requires_grad or other.requires_grad)
        result._children = [self, other]
        
        if result.requires_grad:
            def grad_fn(grad):
                if self.requires_grad:
                    grad_a = grad * other.data
                    self.grad = grad_a.copy() if self.grad is None else self.grad + grad_a
                if other.requires_grad:
                    grad_b = grad * self.data
                    other.grad = grad_b.copy() if other.grad is None else other.grad + grad_b
            result._grad_fn = grad_fn
        
        return result
    
    def __matmul__(self, other):
        """矩陣乘法。"""
        if not isinstance(other, Tensor):
            other = Tensor(other)
        
        result_data = self.data @ other.data
        result = Tensor(result_data, requires_grad=self.requires_grad or other.requires_grad)
        result._children = [self, other]
        
        if result.requires_grad:
            def grad_fn(grad):
                if self.requires_grad:
                    grad_a = grad @ other.data.T
                    self.grad = grad_a.copy() if self.grad is None else self.grad + grad_a
                if other.requires_grad:
                    grad_b = self.data.T @ grad
                    other.grad = grad_b.copy() if other.grad is None else other.grad + grad_b
            result._grad_fn = grad_fn
        
        return result
    
    def sum(self, axis=None, keepdims=False):
        """張量求和。"""
        result_data = np.sum(self.data, axis=axis, keepdims=keepdims)
        result = Tensor(result_data, requires_grad=self.requires_grad)
        result._children = [self]
        
        if result.requires_grad:
            def grad_fn(grad):
                if self.requires_grad:
                    if axis is None:
                        grad_expanded = np.ones_like(self.data) * grad
                    else:
                        shape = list(self.data.shape)
                        shape[axis] = 1
                        grad_expanded = np.ones_like(self.data) * np.expand_dims(grad, axis)
                    self.grad = grad_expanded.copy() if self.grad is None else self.grad + grad_expanded
            result._grad_fn = grad_fn
        
        return result
    
    def mean(self, axis=None, keepdims=False):
        """張量平均值。"""
        result_data = np.mean(self.data, axis=axis, keepdims=keepdims)
        result = Tensor(result_data, requires_grad=self.requires_grad)
        result._children = [self]
        
        if result.requires_grad:
            def grad_fn(grad):
                if self.requires_grad:
                    if axis is None:
                        grad_expanded = np.ones_like(self.data) * grad / self.data.size
                    else:
                        shape = list(self.data.shape)
                        shape[axis] = 1
                        grad_expanded = np.ones_like(self.data) * np.expand_dims(grad, axis) / self.data.shape[axis]
                    self.grad = grad_expanded.copy() if self.grad is None else self.grad + grad_expanded
            result._grad_fn = grad_fn
        
        return result
    
    def reshape(self, *shape):
        """改變形狀。"""
        original_shape = self.data.shape
        result_data = self.data.reshape(*shape)
        result = Tensor(result_data, requires_grad=self.requires_grad)
        result._children = [self]
        
        if result.requires_grad:
            def grad_fn(grad):
                if self.requires_grad:
                    grad_reshaped = grad.reshape(original_shape)
                    self.grad = grad_reshaped.copy() if self.grad is None else self.grad + grad_reshaped
            result._grad_fn = grad_fn
        
        return result
    
    def transpose(self, *axes):
        """轉置。"""
        result_data = self.data.transpose(*axes) if axes else self.data.T
        result = Tensor(result_data, requires_grad=self.requires_grad)
        result._children = [self]
        
        if result.requires_grad:
            def grad_fn(grad):
                if self.requires_grad:
                    if axes:
                        inv_axes = np.argsort(np.argsort(axes))
                        grad_T = grad.transpose(*inv_axes)
                    else:
                        grad_T = grad.T
                    self.grad = grad_T.copy() if self.grad is None else self.grad + grad_T
            result._grad_fn = grad_fn
        
        return result
    
    @property
    def T(self):
        """轉置的快捷方式。"""
        return self.transpose()
    
    def __neg__(self):
        """負號。"""
        result_data = -self.data
        result = Tensor(result_data, requires_grad=self.requires_grad)
        result._children = [self]
        
        if result.requires_grad:
            def grad_fn(grad):
                if self.requires_grad:
                    grad_neg = -grad
                    self.grad = grad_neg.copy() if self.grad is None else self.grad + grad_neg
            result._grad_fn = grad_fn
        
        return result
    
    def __sub__(self, other):
        """張量減法。"""
        return self + (-other)
    
    def __truediv__(self, other):
        """張量除法。"""
        if not isinstance(other, Tensor):
            other = Tensor(other)
        
        result_data = self.data / other.data
        result = Tensor(result_data, requires_grad=self.requires_grad or other.requires_grad)
        result._children = [self, other]
        
        if result.requires_grad:
            def grad_fn(grad):
                if self.requires_grad:
                    grad_a = grad / other.data
                    self.grad = grad_a.copy() if self.grad is None else self.grad + grad_a
                if other.requires_grad:
                    grad_b = -grad * self.data / (other.data ** 2)
                    other.grad = grad_b.copy() if other.grad is None else other.grad + grad_b
            result._grad_fn = grad_fn
        
        return result
    
    def exp(self):
        """指數函數。"""
        result_data = np.exp(self.data)
        result = Tensor(result_data, requires_grad=self.requires_grad)
        result._children = [self]
        
        if result.requires_grad:
            def grad_fn(grad):
                if self.requires_grad:
                    grad_exp = grad * result_data
                    self.grad = grad_exp.copy() if self.grad is None else self.grad + grad_exp
            result._grad_fn = grad_fn
        
        return result
    
    def log(self):
        """自然對數。"""
        result_data = np.log(self.data)
        result = Tensor(result_data, requires_grad=self.requires_grad)
        result._children = [self]
        
        if result.requires_grad:
            def grad_fn(grad):
                if self.requires_grad:
                    grad_log = grad / self.data
                    self.grad = grad_log.copy() if self.grad is None else self.grad + grad_log
            result._grad_fn = grad_fn
        
        return result
    
    def relu(self):
        """ReLU 激活函數。"""
        result_data = np.maximum(0, self.data)
        result = Tensor(result_data, requires_grad=self.requires_grad)
        result._children = [self]
        
        if result.requires_grad:
            def grad_fn(grad):
                if self.requires_grad:
                    mask = (self.data > 0).astype(np.float64)
                    grad_relu = grad * mask
                    self.grad = grad_relu.copy() if self.grad is None else self.grad + grad_relu
            result._grad_fn = grad_fn
        
        return result
    
    def sigmoid(self):
        """Sigmoid 激活函數。"""
        result_data = 1 / (1 + np.exp(-self.data))
        result = Tensor(result_data, requires_grad=self.requires_grad)
        result._children = [self]
        
        if result.requires_grad:
            def grad_fn(grad):
                if self.requires_grad:
                    grad_sig = grad * result_data * (1 - result_data)
                    self.grad = grad_sig.copy() if self.grad is None else self.grad + grad_sig
            result._grad_fn = grad_fn
        
        return result
    
    def detach(self):
        """返回一個不需要梯度的新張量。"""
        return Tensor(self.data.copy(), requires_grad=False)
    
    def numpy(self):
        """返回 numpy array。"""
        return self.data.copy()
    
    @staticmethod
    def zeros(*shape, requires_grad=False):
        """建立全零張量。"""
        return Tensor(np.zeros(shape), requires_grad=requires_grad)
    
    @staticmethod
    def ones(*shape, requires_grad=False):
        """建立全一張量。"""
        return Tensor(np.ones(shape), requires_grad=requires_grad)
    
    @staticmethod
    def randn(*shape, requires_grad=False):
        """建立標準正態分佈隨機張量。"""
        return Tensor(np.random.randn(*shape), requires_grad=requires_grad)

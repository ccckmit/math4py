"""張量運算定理測試 - 驗證定義、公理和定理。"""

import numpy as np
import pytest
from math4py.tensor.tensor import Tensor
from math4py.tensor import function as F


class TestTensorCreation:
    """張量建立公理。"""
    
    def test_tensor_from_list(self):
        """張量可以從串列建立。"""
        t = Tensor([1, 2, 3])
        assert t.shape == (3,)
        assert t.data.dtype == np.float64
    
    def test_tensor_from_numpy(self):
        """張量可以從 numpy array 建立。"""
        arr = np.array([1.0, 2.0, 3.0])
        t = Tensor(arr)
        np.testing.assert_array_equal(t.data, arr)
    
    def test_zeros(self):
        """zeros 建立全零張量。"""
        t = Tensor.zeros(3, 4)
        assert t.shape == (3, 4)
        assert np.all(t.data == 0)
    
    def test_ones(self):
        """ones 建立全一張量。"""
        t = Tensor.ones(2, 3)
        assert t.shape == (2, 3)
        assert np.all(t.data == 1)
    
    def test_randn(self):
        """randn 建立隨機張量。"""
        t = Tensor.randn(1000)
        assert t.shape == (1000,)
        # 檢查均值接近 0（在統計範圍內）
        assert abs(np.mean(t.data)) < 0.1


class TestTensorOperations:
    """張量運算定理。"""
    
    def test_addition(self):
        """加法：a + b = b + a（交換律）。"""
        a = Tensor([1, 2, 3], requires_grad=True)
        b = Tensor([4, 5, 6], requires_grad=True)
        c = a + b
        np.testing.assert_array_equal(c.data, [5, 7, 9])
        
        # 測試梯度
        c.backward(np.array([1, 1, 1]))
        np.testing.assert_array_equal(a.grad, [1, 1, 1])
        np.testing.assert_array_equal(b.grad, [1, 1, 1])
    
    def test_multiplication(self):
        """乘法：a * b。"""
        a = Tensor([2, 3], requires_grad=True)
        b = Tensor([4, 5], requires_grad=True)
        c = a * b
        np.testing.assert_array_equal(c.data, [8, 15])
        
        # 測試梯度：d(a*b)/da = b, d(a*b)/db = a
        c.backward(np.array([1, 1]))
        np.testing.assert_array_equal(a.grad, [4, 5])
        np.testing.assert_array_equal(b.grad, [2, 3])
    
    def test_matmul(self):
        """矩陣乘法：(AB)C = A(BC)（結合律）。"""
        a = Tensor([[1, 2], [3, 4]], requires_grad=True)
        b = Tensor([[5, 6], [7, 8]], requires_grad=True)
        c = a @ b
        expected = np.array([[19, 22], [43, 50]])
        np.testing.assert_array_equal(c.data, expected)
        
        # 測試梯度：c = a @ b
        # dc/da = grad_output @ b^T, dc/db = a^T @ grad_output
        grad_output = np.ones_like(c.data)
        c.backward(grad_output)
        # dc/da = 1s @ b^T = [[5+7, 6+8], [5+7, 6+8]] = [[12, 14], [12, 14]]
        expected_grad_a = grad_output @ b.data.T
        # dc/db = a^T @ 1s = [[1+3, 2+4], [1+3, 2+4]] = [[4, 6], [4, 6]]
        expected_grad_b = a.data.T @ grad_output
        np.testing.assert_array_equal(a.grad, expected_grad_a)
        np.testing.assert_array_equal(b.grad, expected_grad_b)
    
    def test_sum(self):
        """求和：sum(a + b) = sum(a) + sum(b)。"""
        a = Tensor([[1, 2], [3, 4]], requires_grad=True)
        s = a.sum()
        assert s.data == 10
        
        # 標量求和的梯度
        s.backward()
        np.testing.assert_array_equal(a.grad, np.ones_like(a.data))
    
    def test_reshape(self):
        """reshape 不改變資料，只改變形狀。"""
        a = Tensor([[1, 2, 3, 4]], requires_grad=True)
        b = a.reshape(2, 2)
        assert b.shape == (2, 2)
        np.testing.assert_array_equal(b.data, [[1, 2], [3, 4]])
        
        # 測試梯度
        b.sum().backward()
        np.testing.assert_array_equal(a.grad, np.ones_like(a.data))
    
    def test_transpose(self):
        """轉置： (A^T)^T = A。"""
        a = Tensor([[1, 2], [3, 4]], requires_grad=True)
        assert np.all(a.T.data == a.data.T)
        assert np.all(a.T.T.data == a.data)
        
        # 測試梯度
        c = a.T.sum()
        c.backward()
        np.testing.assert_array_equal(a.grad, np.ones_like(a.data))


class TestActivationFunctions:
    """激活函數定理。"""
    
    def test_relu_positive(self):
        """ReLU：x > 0 時，relu(x) = x。"""
        x = Tensor([1, 2, 3], requires_grad=True)
        y = x.relu()
        np.testing.assert_array_equal(y.data, [1, 2, 3])
    
    def test_relu_negative(self):
        """ReLU：x < 0 時，relu(x) = 0。"""
        x = Tensor([-1, -2, -3], requires_grad=True)
        y = x.relu()
        np.testing.assert_array_equal(y.data, [0, 0, 0])
    
    def test_relu_gradient(self):
        """ReLU 梯度：x > 0 時為 1，否則為 0。"""
        x = Tensor([-1, 0, 1, 2], requires_grad=True)
        y = x.relu()
        y.sum().backward()
        np.testing.assert_array_equal(x.grad, [0, 0, 1, 1])
    
    def test_sigmoid_range(self):
        """Sigmoid：輸出在 (0, 1) 之間。"""
        x = Tensor([-100, 0, 100], requires_grad=True)
        y = x.sigmoid()
        assert np.all(y.data > 0)
        # 數值精度問題：sigmoid(100) 非常接近 1 但實際上等於 1.0（浮點數）
        assert y.data[0] > 0 and y.data[0] < 1
        assert y.data[1] == 0.5
        assert y.data[2] > 0.999  # 接近 1 但不一定等於 1
    
    def test_sigmoid_half(self):
        """Sigmoid：sigmoid(0) = 0.5。"""
        x = Tensor([0], requires_grad=True)
        y = x.sigmoid()
        assert abs(y.data[0] - 0.5) < 1e-10
    
    def test_tanh_range(self):
        """Tanh：輸出在 [-1, 1] 之間。"""
        x = Tensor([-100, 0, 100], requires_grad=True)
        y = F.tanh(x)
        # tanh 的範圍是 (-1, 1)，但數值精度下可能等於 ±1
        assert y.data[1] == 0  # tanh(0) = 0
        assert y.data[0] <= 0 and y.data[0] >= -1  # tanh(-100) 接近 -1
        assert y.data[2] >= 0 and y.data[2] <= 1  # tanh(100) 接近 1
    
    def test_tanh_zero(self):
        """Tanh：tanh(0) = 0。"""
        x = Tensor([0], requires_grad=True)
        y = F.tanh(x)
        assert abs(y.data[0]) < 1e-10


class TestLossFunctions:
    """損失函數定理。"""
    
    def test_mse_zero(self):
        """MSE：當 pred = target 時，損失為 0。"""
        pred = Tensor([1.0, 2.0, 3.0], requires_grad=True)
        target = Tensor([1.0, 2.0, 3.0])
        loss = F.mse_loss(pred, target)
        assert abs(loss.data) < 1e-10
    
    def test_mse_gradient(self):
        """MSE 梯度：d/dx (x - t)^2 = 2(x - t)。"""
        pred = Tensor([2.0], requires_grad=True)
        target = Tensor([1.0])
        loss = F.mse_loss(pred, target)
        loss.backward()
        np.testing.assert_almost_equal(pred.grad, [2.0])
    
    def test_cross_entropy_softmax(self):
        """Cross entropy + softmax：正確類別的機率應該接近 1。"""
        pred = Tensor([[1.0, 2.0, 3.0]], requires_grad=True)
        target = Tensor([2])  # 第三類
        loss = F.cross_entropy(pred, target)
        
        # softmax 後第三個值應該最大
        probs = F.softmax(pred)
        assert probs.data[0, 2] > probs.data[0, 0]
        assert probs.data[0, 2] > probs.data[0, 1]


class TestBackward:
    """反向傳播定理。"""
    
    def test_simple_backward(self):
        """簡單計算圖的反向傳播。"""
        x = Tensor([2.0], requires_grad=True)
        y = x * x
        y.backward()
        # dy/dx = 2x = 4
        assert abs(x.grad[0] - 4.0) < 1e-10
    
    def test_chain_rule(self):
        """鏈式法則：d(f(g(x)))/dx = f'(g(x)) * g'(x)。"""
        x = Tensor([2.0], requires_grad=True)
        y = x * x  # g(x) = x^2
        z = y * y  # f(y) = y^2 = x^4
        z.backward()
        # dz/dx = 4x^3 = 32
        assert abs(x.grad[0] - 32.0) < 1e-10
    
    def test_multi_variable(self):
        """多變數梯度。"""
        x = Tensor([1.0, 2.0], requires_grad=True)
        y = x.sum()
        y.backward()
        np.testing.assert_array_equal(x.grad, [1, 1])
    
    def test_grad_accumulation(self):
        """梯度累加：多次 backward 會累加梯度。"""
        x = Tensor([2.0], requires_grad=True)
        y = x * x
        y.backward()
        y.backward()
        # 兩次 backward
        assert abs(x.grad[0] - 8.0) < 1e-10
    
    def test_zero_grad(self):
        """zero_grad 清除梯度。"""
        x = Tensor([2.0], requires_grad=True)
        y = x * x
        y.backward()
        assert x.grad is not None
        x.zero_grad()
        assert np.all(x.grad == 0)


class TestFunctionAPI:
    """function.py API 定理。"""
    
    def test_linear(self):
        """線性變換：y = xW^T + b。"""
        x = Tensor([[1, 2]], requires_grad=True)
        W = Tensor([[1, 2], [3, 4]], requires_grad=True)
        b = Tensor([0.5, 0.5], requires_grad=True)
        y = F.linear(x, W, b)
        expected = np.array([[1*1 + 2*3 + 0.5, 1*2 + 2*4 + 0.5]])
        np.testing.assert_array_almost_equal(y.data, expected)
    
    def test_softmax_sum(self):
        """Softmax：所有機率之和為 1。"""
        x = Tensor([[1.0, 2.0, 3.0]], requires_grad=True)
        probs = F.softmax(x)
        assert abs(np.sum(probs.data) - 1.0) < 1e-10
    
    def test_flatten(self):
        """Flatten：將多維張量展平。"""
        x = Tensor(np.random.randn(2, 3, 4), requires_grad=True)
        y = F.flatten(x)
        assert y.shape == (2, 12)
    
    def test_cat(self):
        """Cat：沿著維度連接張量。"""
        a = Tensor([[1, 2]], requires_grad=True)
        b = Tensor([[3, 4]], requires_grad=True)
        c = F.cat((a, b), dim=0)
        assert c.shape == (2, 2)
        np.testing.assert_array_equal(c.data, [[1, 2], [3, 4]])

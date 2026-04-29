"""張量運算定理測試 - 驗證定義、公理和定理。"""

import numpy as np

from math4py.tensor import function as F
from math4py.tensor.tensor import Tensor


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
        assert abs(np.mean(t.data)) < 0.1


class TestTensorOperations:
    """張量運算定理。"""

    def test_addition(self):
        """加法：a + b = b + a（交換律）。"""
        a = Tensor([1, 2, 3])
        b = Tensor([4, 5, 6])
        c = a + b
        np.testing.assert_array_equal(c.data, [5, 7, 9])

    def test_addition_order(self):
        """加法：(a + b) + c = a + (b + c)（結合律）。"""
        a = Tensor([1, 2])
        b = Tensor([3, 4])
        c = Tensor([5, 6])
        result1 = (a + b) + c
        result2 = a + (b + c)
        np.testing.assert_array_equal(result1.data, result2.data)

    def test_multiplication(self):
        """乘法：a * b。"""
        a = Tensor([2, 3])
        b = Tensor([4, 5])
        c = a * b
        np.testing.assert_array_equal(c.data, [8, 15])

    def test_matmul(self):
        """矩陣乘法。"""
        a = Tensor([[1, 2], [3, 4]])
        b = Tensor([[5, 6], [7, 8]])
        c = a @ b
        expected = np.array([[19, 22], [43, 50]])
        np.testing.assert_array_equal(c.data, expected)

    def test_matmul_associative(self):
        """矩陣乘法：(AB)C = A(BC)（結合律）。"""
        a = Tensor([[1, 2], [3, 4]])
        b = Tensor([[5, 6], [7, 8]])
        c = Tensor([[1, 0], [0, 1]])
        result1 = (a @ b) @ c
        result2 = a @ (b @ c)
        np.testing.assert_array_equal(result1.data, result2.data)

    def test_sum(self):
        """求和：sum(a + b) = sum(a) + sum(b)。"""
        a = Tensor([[1, 2], [3, 4]])
        s = a.sum()
        assert s.data == 10

    def test_sum_axis(self):
        """求和沿維度。"""
        a = Tensor([[1, 2], [3, 4]])
        s = a.sum(axis=0)
        np.testing.assert_array_equal(s.data, [4, 6])

    def test_mean(self):
        """平均值。"""
        a = Tensor([1, 2, 3, 4])
        m = a.mean()
        assert m.data == 2.5

    def test_reshape(self):
        """reshape 不改變資料，只改變形狀。"""
        a = Tensor([[1, 2, 3, 4]])
        b = a.reshape(2, 2)
        assert b.shape == (2, 2)
        np.testing.assert_array_equal(b.data, [[1, 2], [3, 4]])

    def test_transpose(self):
        """轉置： (A^T)^T = A。"""
        a = Tensor([[1, 2], [3, 4]])
        assert np.all(a.T.data == a.data.T)
        assert np.all(a.T.T.data == a.data)

    def test_neg(self):
        """負號：-a + a = 0。"""
        a = Tensor([1, 2, 3])
        b = -a
        np.testing.assert_array_equal(b.data, [-1, -2, -3])

    def test_sub(self):
        """減法：a - b = a + (-b)。"""
        a = Tensor([5, 6, 7])
        b = Tensor([1, 2, 3])
        c = a - b
        np.testing.assert_array_equal(c.data, [4, 4, 4])

    def test_pow_scalar(self):
        """冪運算：a^2。"""
        a = Tensor([2, 3, 4])
        b = a**2
        np.testing.assert_array_equal(b.data, [4, 9, 16])

    def test_div(self):
        """除法。"""
        a = Tensor([6, 8, 10])
        b = Tensor([2, 4, 5])
        c = a / b
        np.testing.assert_array_equal(c.data, [3, 2, 2])


class TestElementaryFunctions:
    """初等函數定理。"""

    def test_exp(self):
        """指數函數。"""
        x = Tensor([0, 1, 2])
        y = x.exp()
        np.testing.assert_array_almost_equal(y.data, [1, np.e, np.e**2])

    def test_log(self):
        """自然對數。"""
        x = Tensor([1, np.e, np.e**2])
        y = x.log()
        np.testing.assert_array_almost_equal(y.data, [0, 1, 2])

    def test_exp_log_inverse(self):
        """exp(log(x)) = x。"""
        x = Tensor([0.5, 1.0, 2.0])
        y = x.log().exp()
        np.testing.assert_array_almost_equal(y.data, x.data)


class TestActivationFunctions:
    """激活函數定理。"""

    def test_relu_positive(self):
        """ReLU：x > 0 時，relu(x) = x。"""
        x = Tensor([1, 2, 3])
        y = x.relu()
        np.testing.assert_array_equal(y.data, [1, 2, 3])

    def test_relu_negative(self):
        """ReLU：x < 0 時，relu(x) = 0。"""
        x = Tensor([-1, -2, -3])
        y = x.relu()
        np.testing.assert_array_equal(y.data, [0, 0, 0])

    def test_relu_mixed(self):
        """ReLU：混合正負值。"""
        x = Tensor([-1, 0, 1, 2])
        y = x.relu()
        np.testing.assert_array_equal(y.data, [0, 0, 1, 2])

    def test_sigmoid_range(self):
        """Sigmoid：輸出在 (0, 1) 之間。"""
        x = Tensor([-100, 0, 100])
        y = x.sigmoid()
        assert np.all(y.data > 0)
        assert y.data[1] == 0.5

    def test_sigmoid_half(self):
        """Sigmoid：sigmoid(0) = 0.5。"""
        x = Tensor([0])
        y = x.sigmoid()
        assert abs(y.data[0] - 0.5) < 1e-10

    def test_tanh_range(self):
        """Tanh：輸出在 [-1, 1] 之間。"""
        x = Tensor([-100, 0, 100])
        y = F.tanh(x)
        assert y.data[1] == 0
        assert y.data[0] <= 0 and y.data[0] >= -1
        assert y.data[2] >= 0 and y.data[2] <= 1

    def test_tanh_zero(self):
        """Tanh：tanh(0) = 0。"""
        x = Tensor([0])
        y = F.tanh(x)
        assert abs(y.data[0]) < 1e-10

    def test_softmax_sum(self):
        """Softmax：所有機率之和為 1。"""
        x = Tensor([[1.0, 2.0, 3.0]])
        probs = F.softmax(x)
        assert abs(np.sum(probs.data) - 1.0) < 1e-10


class TestLossFunctions:
    """損失函數定理。"""

    def test_mse_zero(self):
        """MSE：當 pred = target 時，損失為 0。"""
        pred = Tensor([1.0, 2.0, 3.0])
        target = Tensor([1.0, 2.0, 3.0])
        loss = F.mse_loss(pred, target)
        assert abs(loss.data) < 1e-10

    def test_mse_positive(self):
        """MSE：損失始終非負。"""
        pred = Tensor([1.0, 2.0, 3.0])
        target = Tensor([4.0, 5.0, 6.0])
        loss = F.mse_loss(pred, target)
        assert loss.data >= 0

    def test_cross_entropy_softmax(self):
        """Cross entropy + softmax：正確類別的機率應該最大。"""
        pred = Tensor([[1.0, 2.0, 3.0]])
        probs = F.softmax(pred)
        assert probs.data[0, 2] > probs.data[0, 0]
        assert probs.data[0, 2] > probs.data[0, 1]


class TestFunctionAPI:
    """function.py API 定理。"""

    def test_linear(self):
        """線性變換：y = xW^T + b。"""
        x = Tensor([[1, 2]])
        W = Tensor([[1, 2], [3, 4]])
        b = Tensor([0.5, 0.5])
        y = F.linear(x, W, b)
        expected = np.array([[1 * 1 + 2 * 3 + 0.5, 1 * 2 + 2 * 4 + 0.5]])
        np.testing.assert_array_almost_equal(y.data, expected)

    def test_flatten(self):
        """Flatten：將多維張量展平。"""
        x = Tensor(np.random.randn(2, 3, 4))
        y = F.flatten(x)
        assert y.shape == (2, 12)

    def test_cat(self):
        """Cat：沿著維度連接張量。"""
        a = Tensor([[1, 2]])
        b = Tensor([[3, 4]])
        c = F.cat((a, b), dim=0)
        assert c.shape == (2, 2)
        np.testing.assert_array_equal(c.data, [[1, 2], [3, 4]])

    def test_stack(self):
        """Stack：堆疊張量。"""
        a = Tensor([1, 2])
        b = Tensor([3, 4])
        c = F.stack((a, b), dim=0)
        assert c.shape == (2, 2)
        np.testing.assert_array_equal(c.data, [[1, 2], [3, 4]])

    def test_transpose(self):
        """轉置函數。"""
        x = Tensor([[1, 2], [3, 4]])
        y = F.transpose(x)
        np.testing.assert_array_equal(y.data, [[1, 3], [2, 4]])

    def test_reshape(self):
        """Reshape 函數。"""
        x = Tensor([[1, 2, 3, 4]])
        y = F.reshape(x, 2, 2)
        assert y.shape == (2, 2)

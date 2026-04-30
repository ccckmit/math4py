"""張量運算測試。"""

import numpy as np

from math4py.tensor import function as F
from math4py.tensor.tensor import Tensor


class TestTensorCreation:
    """張量建立測試。"""

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


class TestBasicOperations:
    """基本運算測試。"""

    def test_addition(self):
        """加法。"""
        a = Tensor([1, 2, 3])
        b = Tensor([4, 5, 6])
        c = a + b
        np.testing.assert_array_equal(c.data, [5, 7, 9])

    def test_addition_order(self):
        """加法結合律。"""
        a = Tensor([1, 2])
        b = Tensor([3, 4])
        c = Tensor([5, 6])
        result1 = (a + b) + c
        result2 = a + (b + c)
        np.testing.assert_array_equal(result1.data, result2.data)

    def test_multiplication(self):
        """逐元素乘法。"""
        a = Tensor([2, 3])
        b = Tensor([4, 5])
        c = a * b
        np.testing.assert_array_equal(c.data, [8, 15])

    def test_matrix_multiplication(self):
        """矩陣乘法。"""
        a = Tensor([[1, 2], [3, 4]])
        b = Tensor([[5, 6], [7, 8]])
        c = a @ b
        expected = np.array([[19, 22], [43, 50]])
        np.testing.assert_array_equal(c.data, expected)

    def test_matmul_associative(self):
        """矩陣乘法結合律 (AB)C = A(BC)。"""
        a = Tensor([[1, 2], [3, 4]])
        b = Tensor([[5, 6], [7, 8]])
        c = Tensor([[1, 0], [0, 1]])
        result1 = (a @ b) @ c
        result2 = a @ (b @ c)
        np.testing.assert_array_equal(result1.data, result2.data)


class TestReductionOperations:
    """歸約運算測試。"""

    def test_sum(self):
        """求和。"""
        a = Tensor([[1, 2], [3, 4]])
        s = a.sum()
        assert s.data == 10

    def test_sum_axis(self):
        """沿維度求和。"""
        a = Tensor([[1, 2], [3, 4]])
        s = a.sum(axis=0)
        np.testing.assert_array_equal(s.data, [4, 6])

    def test_mean(self):
        """平均值。"""
        a = Tensor([1, 2, 3, 4])
        m = a.mean()
        assert m.data == 2.5


class TestShapeOperations:
    """形狀操作測試。"""

    def test_reshape(self):
        """reshape。"""
        a = Tensor([[1, 2, 3, 4]])
        b = a.reshape(2, 2)
        assert b.shape == (2, 2)
        np.testing.assert_array_equal(b.data, [[1, 2], [3, 4]])

    def test_transpose(self):
        """轉置：(A^T)^T = A。"""
        a = Tensor([[1, 2], [3, 4]])
        np.testing.assert_array_equal(a.T.data, a.data.T)
        np.testing.assert_array_equal(a.T.T.data, a.data)

    def test_flatten(self):
        """展平。"""
        x = Tensor(np.random.randn(2, 3, 4))
        y = F.flatten(x)
        assert y.shape == (2, 12)


class TestElementaryOperations:
    """初等函數測試。"""

    def test_negative(self):
        """負號。"""
        a = Tensor([1, 2, 3])
        b = -a
        np.testing.assert_array_equal(b.data, [-1, -2, -3])

    def test_subtraction(self):
        """減法。"""
        a = Tensor([5, 6, 7])
        b = Tensor([1, 2, 3])
        c = a - b
        np.testing.assert_array_equal(c.data, [4, 4, 4])

    def test_pow_scalar(self):
        """冪運算。"""
        a = Tensor([2, 3, 4])
        b = a**2
        np.testing.assert_array_equal(b.data, [4, 9, 16])

    def test_division(self):
        """除法。"""
        a = Tensor([6, 8, 10])
        b = Tensor([2, 4, 5])
        c = a / b
        np.testing.assert_array_equal(c.data, [3, 2, 2])


class TestMathFunctions:
    """數學函數測試。"""

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
    """激活函數測試。"""

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

    def test_tanh_zero(self):
        """Tanh：tanh(0) = 0。"""
        x = Tensor([0])
        y = F.tanh(x)
        assert abs(y.data[0]) < 1e-10


class TestSoftmax:
    """Softmax 測試。"""

    def test_softmax_sum(self):
        """Softmax：所有機率之和為 1。"""
        x = Tensor([[1.0, 2.0, 3.0]])
        probs = F.softmax(x)
        assert abs(np.sum(probs.data) - 1.0) < 1e-10

    def test_softmax_max(self):
        """Softmax：最大值對應正確類別。"""
        pred = Tensor([[1.0, 2.0, 3.0]])
        probs = F.softmax(pred)
        assert np.argmax(probs.data) == 2


class TestLossFunctions:
    """損失函數測試。"""

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


class TestLinearFunction:
    """線性變換測試。"""

    def test_linear(self):
        """線性變換：y = xW^T + b。"""
        x = Tensor([[1, 2]])
        W = Tensor([[1, 2], [3, 4]])
        b = Tensor([0.5, 0.5])
        y = F.linear(x, W, b)
        expected = np.array([[1 * 1 + 2 * 3 + 0.5, 1 * 2 + 2 * 4 + 0.5]])
        np.testing.assert_array_almost_equal(y.data, expected)

    def test_linear_no_bias(self):
        """線性變換（無偏置）。"""
        x = Tensor([[1, 2]])
        W = Tensor([[1, 2], [3, 4]])
        y = F.linear(x, W)
        expected = np.array([[1 * 1 + 2 * 3, 1 * 2 + 2 * 4]])
        np.testing.assert_array_almost_equal(y.data, expected)


class TestCatAndStack:
    """連接和堆疊測試。"""

    def test_cat(self):
        """沿維度連接。"""
        a = Tensor([[1, 2]])
        b = Tensor([[3, 4]])
        c = F.cat((a, b), dim=0)
        assert c.shape == (2, 2)
        np.testing.assert_array_equal(c.data, [[1, 2], [3, 4]])

    def test_stack(self):
        """堆疊。"""
        a = Tensor([1, 2])
        b = Tensor([3, 4])
        c = F.stack((a, b), dim=0)
        assert c.shape == (2, 2)
        np.testing.assert_array_equal(c.data, [[1, 2], [3, 4]])


class TestIndexing:
    """索引測試。"""

    def test_indexing_1d(self):
        """一維索引。"""
        x = Tensor([1, 2, 3, 4])
        assert x[0].data == 1
        assert x[-1].data == 4

    def test_indexing_2d(self):
        """二維索引。"""
        x = Tensor([[1, 2], [3, 4]])
        np.testing.assert_array_equal(x[0].data, [1, 2])
        np.testing.assert_array_equal(x[:, 0].data, [1, 3])

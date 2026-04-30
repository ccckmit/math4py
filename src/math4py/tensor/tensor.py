"""張量物件 - numpy 封裝。"""

import numpy as np


class Tensor:
    """張量類別，numpy 封裝。"""

    def __init__(self, data):
        """初始化張量。"""
        if isinstance(data, np.ndarray):
            self.data = data.copy()
        else:
            self.data = np.array(data, dtype=np.float64)

    def __repr__(self):
        return f"Tensor(shape={self.shape})"

    @property
    def shape(self):
        return self.data.shape

    def __getitem__(self, key):
        """支援索引操作，如 tensor[0], tensor[0, 1]"""
        result_data = self.data[key]
        return Tensor(result_data)

    def __add__(self, other):
        """張量加法。"""
        if not isinstance(other, Tensor):
            other = Tensor(other)
        result_data = self.data + other.data
        return Tensor(result_data)

    def __mul__(self, other):
        """張量逐元素乘法。"""
        if not isinstance(other, Tensor):
            other = Tensor(other)
        result_data = self.data * other.data
        return Tensor(result_data)

    def __matmul__(self, other):
        """矩陣乘法。"""
        if not isinstance(other, Tensor):
            other = Tensor(other)
        result_data = self.data @ other.data
        return Tensor(result_data)

    def sum(self, axis=None, keepdims=False):
        """張量求和。"""
        result_data = np.sum(self.data, axis=axis, keepdims=keepdims)
        return Tensor(result_data)

    def mean(self, axis=None, keepdims=False):
        """張量平均值。"""
        result_data = np.mean(self.data, axis=axis, keepdims=keepdims)
        return Tensor(result_data)

    def reshape(self, *shape):
        """改變形狀。"""
        result_data = self.data.reshape(*shape)
        return Tensor(result_data)

    def transpose(self, *axes):
        """轉置。"""
        result_data = self.data.transpose(*axes) if axes else self.data.T
        return Tensor(result_data)

    @property
    def T(self):
        """轉置的快捷方式。"""
        return self.transpose()

    def __neg__(self):
        """負號。"""
        result_data = -self.data
        return Tensor(result_data)

    def __sub__(self, other):
        """張量減法。"""
        return self + (-other)

    def __pow__(self, exponent):
        """冪運算。"""
        if isinstance(exponent, (int, float)):
            result_data = self.data**exponent
            return Tensor(result_data)
        elif isinstance(exponent, Tensor):
            result_data = self.data**exponent.data
            return Tensor(result_data)
        return NotImplemented

    def __truediv__(self, other):
        """張量除法。"""
        if not isinstance(other, Tensor):
            other = Tensor(other)
        result_data = self.data / other.data
        return Tensor(result_data)

    def exp(self):
        """指數函數。"""
        result_data = np.exp(self.data)
        return Tensor(result_data)

    def log(self):
        """自然對數。"""
        result_data = np.log(self.data)
        return Tensor(result_data)

    def relu(self):
        """ReLU 激活函數。"""
        result_data = np.maximum(0, self.data)
        return Tensor(result_data)

    def sigmoid(self):
        """Sigmoid 激活函數。"""
        result_data = 1 / (1 + np.exp(-self.data))
        return Tensor(result_data)

    def softmax(self, axis=-1):
        """Softmax 激活函數。"""
        max_val = np.max(self.data, axis=axis, keepdims=True)
        exp_vals = np.exp(self.data - max_val)
        result_data = exp_vals / np.sum(exp_vals, axis=axis, keepdims=True)
        return Tensor(result_data)

    def numpy(self):
        """返回 numpy array。"""
        return self.data.copy()

    @staticmethod
    def zeros(*shape):
        """建立全零張量。"""
        return Tensor(np.zeros(shape))

    @staticmethod
    def ones(*shape):
        """建立全一張量。"""
        return Tensor(np.ones(shape))

    @staticmethod
    def randn(*shape):
        """建立標準正態分佈隨機張量。"""
        return Tensor(np.random.randn(*shape))

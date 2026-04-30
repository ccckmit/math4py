r"""Tensor theorem tests."""

import pytest
import numpy as np


class TestTensorCreation:
    def test_creation_from_list(self):
        from math4py.tensor.theorem import tensor_creation

        result = tensor_creation([1, 2, 3])
        assert result["pass"]
        assert result["shape"] == (3,)

    def test_creation_from_numpy(self):
        from math4py.tensor.theorem import tensor_creation

        result = tensor_creation(np.array([1.0, 2.0, 3.0]))
        assert result["pass"]


class TestTensorZerosOnes:
    def test_zeros(self):
        from math4py.tensor.theorem import tensor_zeros

        result = tensor_zeros((3, 4))
        assert result["pass"]
        assert result["shape"] == (3, 4)

    def test_ones(self):
        from math4py.tensor.theorem import tensor_ones

        result = tensor_ones((2, 3))
        assert result["pass"]


class TestAddition:
    def test_addition_commutativity(self):
        from math4py.tensor.theorem import addition_commutativity
        from math4py.tensor import Tensor

        a = Tensor([1, 2, 3])
        b = Tensor([4, 5, 6])
        result = addition_commutativity(a, b)
        assert result["pass"]

    def test_addition_associativity(self):
        from math4py.tensor.theorem import addition_associativity
        from math4py.tensor import Tensor

        a = Tensor([1, 2])
        b = Tensor([3, 4])
        c = Tensor([5, 6])
        result = addition_associativity(a, b, c)
        assert result["pass"]


class TestMultiplication:
    def test_multiplication(self):
        from math4py.tensor.theorem import multiplication
        from math4py.tensor import Tensor

        a = Tensor([2, 3])
        b = Tensor([4, 5])
        result = multiplication(a, b)
        assert result["pass"]
        np.testing.assert_array_equal(result["data"], [8, 15])


class TestMatmul:
    def test_matmul(self):
        from math4py.tensor.theorem import matmul
        from math4py.tensor import Tensor

        a = Tensor([[1, 2], [3, 4]])
        b = Tensor([[5, 6], [7, 8]])
        result = matmul(a, b)
        assert result["pass"]

    def test_matmul_associativity(self):
        from math4py.tensor.theorem import matmul_associativity
        from math4py.tensor import Tensor

        a = Tensor([[1, 2], [3, 4]])
        b = Tensor([[5, 6], [7, 8]])
        c = Tensor([[1, 0], [0, 1]])
        result = matmul_associativity(a, b, c)
        assert result["pass"]


class TestSumMean:
    def test_sum(self):
        from math4py.tensor.theorem import sum_property
        from math4py.tensor import Tensor

        a = Tensor([[1, 2], [3, 4]])
        result = sum_property(a)
        assert result["pass"]
        assert result["sum"] == 10

    def test_mean(self):
        from math4py.tensor.theorem import mean_property
        from math4py.tensor import Tensor

        a = Tensor([1, 2, 3, 4])
        result = mean_property(a)
        assert result["pass"]


class TestReshapeTranspose:
    def test_reshape(self):
        from math4py.tensor.theorem import reshape_property
        from math4py.tensor import Tensor

        a = Tensor([[1, 2, 3, 4]])
        result = reshape_property(a, (2, 2))
        assert result["pass"]
        assert result["shape"] == (2, 2)

    def test_transpose(self):
        from math4py.tensor.theorem import transpose_property
        from math4py.tensor import Tensor

        a = Tensor([[1, 2], [3, 4]])
        result = transpose_property(a)
        assert result["pass"]


class TestNegationSubtraction:
    def test_negation(self):
        from math4py.tensor.theorem import negation_property
        from math4py.tensor import Tensor

        a = Tensor([1, 2, 3])
        result = negation_property(a)
        assert result["pass"]

    def test_subtraction(self):
        from math4py.tensor.theorem import subtraction_property
        from math4py.tensor import Tensor

        a = Tensor([5, 6, 7])
        b = Tensor([1, 2, 3])
        result = subtraction_property(a, b)
        assert result["pass"]


class TestPowDiv:
    def test_pow(self):
        from math4py.tensor.theorem import pow_property
        from math4py.tensor import Tensor

        a = Tensor([2, 3, 4])
        result = pow_property(a, 2)
        assert result["pass"]

    def test_division(self):
        from math4py.tensor.theorem import division_property
        from math4py.tensor import Tensor

        a = Tensor([6, 8, 10])
        b = Tensor([2, 4, 5])
        result = division_property(a, b)
        assert result["pass"]


class TestExpLog:
    def test_exp(self):
        from math4py.tensor.theorem import exp_property
        from math4py.tensor import Tensor

        x = Tensor([0, 1, 2])
        result = exp_property(x)
        assert result["pass"]

    def test_log(self):
        from math4py.tensor.theorem import log_property
        from math4py.tensor import Tensor

        x = Tensor([1, np.e, np.e**2])
        result = log_property(x)
        assert result["pass"]

    def test_exp_log_inverse(self):
        from math4py.tensor.theorem import exp_log_inverse
        from math4py.tensor import Tensor

        x = Tensor([0.5, 1.0, 2.0])
        result = exp_log_inverse(x)
        assert result["pass"]


class TestRelu:
    def test_relu_positive(self):
        from math4py.tensor.theorem import relu_positive
        from math4py.tensor import Tensor

        x = Tensor([1, 2, 3])
        result = relu_positive(x)
        assert result["pass"]

    def test_relu_negative(self):
        from math4py.tensor.theorem import relu_negative
        from math4py.tensor import Tensor

        x = Tensor([-1, -2, -3])
        result = relu_negative(x)
        assert result["pass"]

    def test_relu_mixed(self):
        from math4py.tensor.theorem import relu_mixed
        from math4py.tensor import Tensor

        x = Tensor([-1, 0, 1, 2])
        result = relu_mixed(x)
        assert result["pass"]


class TestSigmoid:
    def test_sigmoid_range(self):
        from math4py.tensor.theorem import sigmoid_range
        from math4py.tensor import Tensor

        x = Tensor([-100, 0, 100])
        result = sigmoid_range(x)
        assert result["pass"]

    def test_sigmoid_half(self):
        from math4py.tensor.theorem import sigmoid_half
        from math4py.tensor import Tensor

        x = Tensor([0])
        result = sigmoid_half(x)
        assert result["pass"]


class TestTanh:
    def test_tanh_range(self):
        from math4py.tensor.theorem import tanh_range
        from math4py.tensor import Tensor

        x = Tensor([-100, 0, 100])
        result = tanh_range(x)
        assert result["pass"]

    def test_tanh_zero(self):
        from math4py.tensor.theorem import tanh_zero
        from math4py.tensor import Tensor

        x = Tensor([0])
        result = tanh_zero(x)
        assert result["pass"]


class TestSoftmax:
    def test_softmax_sum(self):
        from math4py.tensor.theorem import softmax_sum
        from math4py.tensor import Tensor

        x = Tensor([[1.0, 2.0, 3.0]])
        result = softmax_sum(x)
        assert result["pass"]


class TestMSE:
    def test_mse_zero(self):
        from math4py.tensor.theorem import mse_zero
        from math4py.tensor import Tensor

        pred = Tensor([1.0, 2.0, 3.0])
        target = Tensor([1.0, 2.0, 3.0])
        result = mse_zero(pred, target)
        assert result["pass"]

    def test_mse_positive(self):
        from math4py.tensor.theorem import mse_positive
        from math4py.tensor import Tensor

        pred = Tensor([1.0, 2.0, 3.0])
        target = Tensor([4.0, 5.0, 6.0])
        result = mse_positive(pred, target)
        assert result["pass"]


class TestFunctionAPI:
    def test_linear(self):
        from math4py.tensor.theorem import linear_transform
        from math4py.tensor import Tensor

        x = Tensor([[1, 2]])
        W = Tensor([[1, 2], [3, 4]])
        b = Tensor([0.5, 0.5])
        result = linear_transform(x, W, b)
        assert result["pass"]

    def test_flatten(self):
        from math4py.tensor.theorem import flatten_transform
        from math4py.tensor import Tensor

        x = Tensor(np.random.randn(2, 3, 4))
        result = flatten_transform(x)
        assert result["pass"]

    def test_cat(self):
        from math4py.tensor.theorem import cat_transform
        from math4py.tensor import Tensor

        a = Tensor([[1, 2]])
        b = Tensor([[3, 4]])
        result = cat_transform((a, b), 0)
        assert result["pass"]

    def test_stack(self):
        from math4py.tensor.theorem import stack_transform
        from math4py.tensor import Tensor

        a = Tensor([1, 2])
        b = Tensor([3, 4])
        result = stack_transform((a, b), 0)
        assert result["pass"]

    def test_reshape(self):
        from math4py.tensor.theorem import reshape_transform
        from math4py.tensor import Tensor

        x = Tensor([[1, 2, 3, 4]])
        result = reshape_transform(x, (2, 2))
        assert result["pass"]
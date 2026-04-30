"""Test tensor algebra module."""

import pytest
import numpy as np
from math4py.differential_geometry.tensor_algebra import (
    Tensor, tensor_product, contract, raise_index, lower_index,
    metric_tensor, inverse_metric, kronecker_delta,
)


class TestTensorCreation:
    def test_scalar_tensor(self):
        """Scalar (rank 0) tensor."""
        t = Tensor(3.14, [], 2)
        assert t.rank == 0
        assert t.data == 3.14

    def test_vector_tensor(self):
        """Vector (rank 1) tensor."""
        t = Tensor([1.0, 2.0], ['u'], 2)
        assert t.rank == 1
        assert t.shape == (2,)

    def test_matrix_tensor(self):
        """Matrix (rank 2) tensor."""
        data = [[1.0, 0.0], [0.0, 1.0]]
        t = Tensor(data, ['u', 'd'], 2)
        assert t.rank == 2
        assert t.shape == (2, 2)


class TestTensorArithmetic:
    def test_add_same_indices(self):
        """Add tensors with same indices."""
        t1 = Tensor([1.0, 2.0], ['u'], 2)
        t2 = Tensor([3.0, 4.0], ['u'], 2)
        result = t1 + t2
        assert result.data[0] == 4.0
        assert result.data[1] == 6.0

    def test_sub_same_indices(self):
        """Subtract tensors with same indices."""
        t1 = Tensor([5.0, 7.0], ['d'], 2)
        t2 = Tensor([1.0, 2.0], ['d'], 2)
        result = t1 - t2
        assert result.data[0] == 4.0

    def test_mul_scalar(self):
        """Multiply tensor by scalar."""
        t = Tensor([1.0, 2.0], ['u'], 2)
        result = t * 3.0
        assert result.data[0] == 3.0
        assert result.data[1] == 6.0


class TestTensorProduct:
    def test_vector_tensor_product(self):
        """Tensor product of two vectors."""
        v1 = Tensor([1.0, 2.0], ['u'], 2)
        v2 = Tensor([3.0, 4.0], ['d'], 2)
        result = v1.tensor_product(v2)
        # 結果為 (1,1) 型張量，形狀 (2,2)
        assert result.rank == 2
        assert result.indices == ['u', 'd']
        assert result.shape == (2, 2)
        assert result.data[0, 0] == 3.0  # 1*3
        assert result.data[0, 1] == 4.0  # 1*4


class TestContraction:
    def test_contract_matrix(self):
        """Contract a (1,1) tensor (trace)."""
        data = [[1.0, 2.0], [3.0, 4.0]]
        t = Tensor(data, ['u', 'd'], 2)
        result = t.contract(0, 1)
        # 縮並後為純量
        assert result.rank == 0
        assert abs(float(result.data) - 5.0) < 1e-10  # trace = 1+4 = 5

    def test_contract_invalid_indices(self):
        """Cannot contract same type indices."""
        data = [[1.0, 2.0], [3.0, 4.0]]
        t = Tensor(data, ['u', 'u'], 2)
        with pytest.raises(ValueError):
            t.contract(0, 1)


class TestIndexRaisingLowering:
    def test_raise_index(self):
        """Raise a covariant index."""
        g_inv = np.array([[1.0, 0.0], [0.0, 1.0]])  # 歐幾里得度規
        v = Tensor([1.0, 2.0], ['d'], 2)
        result = v.raise_index(0, g_inv)
        assert result.indices == ['u']
        assert result.data[0] == 1.0

    def test_lower_index(self):
        """Lower a contravariant index."""
        g = np.array([[1.0, 0.0], [0.0, 1.0]])
        v = Tensor([3.0, 4.0], ['u'], 2)
        result = v.lower_index(0, g)
        assert result.indices == ['d']
        assert result.data[0] == 3.0

    def test_raise_lower_inverse(self):
        """Raise then lower should return original."""
        g = np.array([[2.0, 0.0], [0.0, 3.0]])
        g_inv = np.linalg.inv(g)
        v = Tensor([1.0, 2.0], ['d'], 2)
        v_up = v.raise_index(0, g_inv)
        v_down = v_up.lower_index(0, g)
        assert abs(v_down.data[0] - v.data[0]) < 1e-10
        assert abs(v_down.data[1] - v.data[1]) < 1e-10


class TestMetricTensor:
    def test_euclidean_metric(self):
        """Euclidean metric tensor."""
        g = metric_tensor(dim=3, signature="euclidean")
        assert g.shape == (3, 3)
        assert g[0, 0] == 1.0
        assert g[1, 1] == 1.0
        assert g[2, 2] == 1.0

    def test_minkowski_metric(self):
        """Minkowski metric tensor (relativity)."""
        g = metric_tensor(dim=4, signature="minkowski")
        assert g[0, 0] == -1.0  # time component
        assert g[1, 1] == 1.0   # space components
        assert g[2, 2] == 1.0

    def test_inverse_metric(self):
        """Inverse of metric tensor."""
        g = metric_tensor(dim=2, signature="euclidean")
        g_inv = inverse_metric(g)
        identity = g @ g_inv
        assert abs(identity[0, 0] - 1.0) < 1e-10
        assert abs(identity[1, 1] - 1.0) < 1e-10


class TestKroneckerDelta:
    def test_kronecker_delta(self):
        """Kronecker delta δ^μ_ν."""
        delta = kronecker_delta(dim=3)
        assert delta.shape == (3, 3)
        assert delta[0, 0] == 1.0
        assert delta[1, 1] == 1.0
        assert delta[0, 1] == 0.0

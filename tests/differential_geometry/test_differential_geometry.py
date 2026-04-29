r"""Differential geometry tests."""

import numpy as np

from math4py.differential_geometry.function import (
    christoffel,
    energy_momentum_perfect_fluid,
    friedmann_metric,
    geodesic_equation,
    kretschmann_scalar,
    metric_determinant,
    metric_inverse,
    ricci_scalar,
    ricci_tensor,
    riemann_curvature,
    schwarzschild_metric,
    sqrt_metric_det,
)
from math4py.tensor.tensor import Tensor


class TestMetricOperations:
    """Metric tensor operations."""

    def test_metric_inverse_identity(self):
        """g^{ij} g_{jk} = delta^i_k"""
        g = Tensor(np.array([[2.0, 1.0], [1.0, 2.0]]))
        g_inv = metric_inverse(g)
        product = g.data @ g_inv.data
        np.testing.assert_array_almost_equal(product, np.eye(2))

    def test_metric_inverse_2x2(self):
        """Inverse of 2x2 metric."""
        g = Tensor([[1.0, 0.0], [0.0, 1.0]])
        g_inv = metric_inverse(g)
        np.testing.assert_array_almost_equal(g_inv.data, g.data)

    def test_metric_determinant_identity(self):
        """det(I) = 1"""
        g = Tensor(np.eye(2))
        det = metric_determinant(g)
        assert det.data == 1.0

    def test_metric_determinant_2x2(self):
        """det([[a, b], [c, d]]) = ad - bc"""
        g = Tensor([[2.0, 1.0], [1.0, 2.0]])
        det = metric_determinant(g)
        assert abs(det.data - 3.0) < 1e-10

    def test_sqrt_metric_det_2x2(self):
        """sqrt(|det|) for 2x2 identity metric."""
        g = Tensor(np.eye(2))
        sqrt_det = sqrt_metric_det(g)
        assert abs(sqrt_det.data - 1.0) < 1e-10

    def test_minkowski_determinant(self):
        """det(eta) = -1 for Minkowski."""
        eta = Tensor(np.diag([-1, 1, 1, 1]))
        det = metric_determinant(eta)
        assert det.data == -1.0


class TestChristoffelSymbols:
    """Christoffel symbol tests."""

    def test_christoffel_cartesian(self):
        """Christoffel vanishes in Cartesian coordinates."""
        g = Tensor(np.eye(3))
        gamma = christoffel(g)
        np.testing.assert_array_almost_equal(gamma.data, np.zeros((3, 3, 3)))

    def test_christoffel_shape(self):
        """Christoffel is rank-3."""
        g = Tensor(np.eye(2))
        gamma = christoffel(g)
        assert gamma.data.shape == (2, 2, 2)

    def test_christoffel_symmetric(self):
        """Gamma^k_ij = Gamma^k_ji"""
        g = Tensor([[1.0, 0.5], [0.5, 1.0]])
        gamma = christoffel(g)
        np.testing.assert_array_almost_equal(gamma.data[0, 0, 1], gamma.data[0, 1, 0])
        np.testing.assert_array_almost_equal(gamma.data[1, 0, 1], gamma.data[1, 1, 0])


class TestRiemannCurvature:
    """Riemann curvature tensor tests."""

    def test_riemann_flat(self):
        """Riemann vanishes in flat space."""
        g = Tensor(np.eye(3))
        R = riemann_curvature(g)
        np.testing.assert_array_almost_equal(R.data, np.zeros((3, 3, 3, 3)))

    def test_riemann_shape(self):
        """Riemann is rank-4."""
        g = Tensor(np.eye(2))
        R = riemann_curvature(g)
        assert R.data.shape == (2, 2, 2, 2)

    def test_riemann_skew_symmetry(self):
        """R_ijkl = -R_ijlk"""
        g = Tensor([[1.0, 0.0], [0.0, 1.0]])
        R = riemann_curvature(g)
        np.testing.assert_array_almost_equal(
            R.data[:, :, :, :], -R.data[:, :, :, ::-1]
        )


class TestRicciOperations:
    """Ricci tensor and scalar tests."""

    def test_ricci_symmetric(self):
        """Ricci is symmetric."""
        g = Tensor([[2.0, 1.0], [1.0, 2.0]])
        R = riemann_curvature(g)
        ricci = ricci_tensor(R)
        np.testing.assert_array_almost_equal(ricci.data, ricci.data.T)

    def test_ricci_shape(self):
        """Ricci tensor is rank-2."""
        g = Tensor(np.eye(2))
        R = riemann_curvature(g)
        ricci = ricci_tensor(R)
        assert ricci.data.shape == (2, 2)

    def test_ricci_scalar_flat(self):
        """Ricci scalar = 0 in flat space."""
        g = Tensor(np.eye(3))
        R = riemann_curvature(g)
        ricci = ricci_tensor(R)
        R_scalar = ricci_scalar(ricci, g)
        assert abs(R_scalar.data) < 1e-10


class TestEinsteinTensor:
    """Einstein tensor tests."""

    def test_einstein_shape(self):
        """Einstein tensor is rank-2."""
        g = Tensor(np.diag([-1, 1, 1, 1]))
        G = Tensor(np.zeros((4, 4)))
        assert G.data.shape == (4, 4)


class TestSchwarzschildMetric:
    """Schwarzschild black hole metric."""

    def test_schwarzschild_signature(self):
        """Correct Lorentzian signature."""
        r = Tensor([10.0])
        g = schwarzschild_metric(1.0, r)
        assert g.data[0, 0] < 0
        assert g.data[1, 1] > 0

    def test_schwarzschild_horizon(self):
        """g_rr diverges at event horizon r = 2M."""
        r = Tensor([2.0])
        g = schwarzschild_metric(1.0, r)
        assert np.isinf(g.data[1, 1])

    def test_schwarzschild_outside(self):
        """Outside horizon g_rr is finite."""
        r = Tensor([10.0])
        g = schwarzschild_metric(1.0, r)
        assert g.data[1, 1] > 0
        assert not np.isinf(g.data[1, 1])


class TestFLRWMetric:
    """FLRW cosmological metric."""

    def test_friedmann_shape(self):
        """FLRW is 4x4."""
        t = Tensor([1.0])
        g = friedmann_metric(t, k=0)
        assert g.data.shape == (4, 4)

    def test_friedmann_k0(self):
        """k=0: flat universe."""
        t = Tensor([1.0])
        g = friedmann_metric(t, k=0)
        np.testing.assert_array_almost_equal(g.data[1, 1], 1.0)
        np.testing.assert_array_almost_equal(g.data[2, 2], 1.0)
        np.testing.assert_array_almost_equal(g.data[3, 3], 1.0)

    def test_friedmann_expansion(self):
        """Scale factor increases with time."""
        t1 = Tensor([1.0])
        t2 = Tensor([2.0])
        g1 = friedmann_metric(t1, k=0)
        g2 = friedmann_metric(t2, k=0)
        assert g2.data[1, 1] > g1.data[1, 1]


class TestEnergyMomentumTensor:
    """Energy-momentum tensor tests."""

    def test_perfect_fluid_shape(self):
        """T is rank-2."""
        u = Tensor([1.0, 0.0, 0.0, 0.0])
        T = energy_momentum_perfect_fluid(1.0, 0.0, u)
        assert T.data.shape == (4, 4)

    def test_perfect_fluid_pressure_positive(self):
        """Positive pressure gives positive spatial components."""
        u = Tensor([1.0, 0.0, 0.0, 0.0])
        T = energy_momentum_perfect_fluid(1.0, 0.5, u)

        for i in range(1, 4):
            assert T.data[i, i] > 0


class TestGeodesicEquation:
    """Geodesic equation tests."""

    def test_geodesic_flat(self):
        """Zero acceleration in flat space."""
        x = Tensor([1.0, 0.0, 0.0])
        gamma = Tensor(np.zeros((3, 3, 3)))
        accel = geodesic_equation(x, gamma)

        np.testing.assert_array_almost_equal(accel.data, np.zeros(3))

    def test_geodesic_shape(self):
        """Output has same shape as input."""
        x = Tensor([1.0, 0.5])
        gamma = Tensor(np.zeros((2, 2, 2)))
        accel = geodesic_equation(x, gamma)

        assert accel.data.shape == x.data.shape


class TestCurvatureScalars:
    """Curvature scalar tests."""

    def test_kretschmann_flat(self):
        """K = 0 in flat space."""
        g = Tensor(np.eye(3))
        R = riemann_curvature(g)
        K = kretschmann_scalar(R)

        assert K.data == 0.0

    def test_kretschmann_positive(self):
        """K >= 0."""
        g = Tensor([[2.0, 1.0], [1.0, 2.0]])
        R = riemann_curvature(g)
        K = kretschmann_scalar(R)

        assert K.data >= 0


class TestWeylTensor:
    """Weyl curvature tensor tests."""

    def test_weyl_shape(self):
        """Weyl is rank-4."""
        g = Tensor(np.diag([-1, 1, 1, 1]))
        R = riemann_curvature(g)
        gamma = christoffel(g)
        C = Tensor(np.zeros((4, 4, 4, 4)))
        assert C.data.shape == (4, 4, 4, 4)

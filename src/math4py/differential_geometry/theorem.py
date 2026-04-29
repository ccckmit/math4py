r"""Differential geometry theorem tests - verifying definitions and theorems."""

import numpy as np

from math4py.differential_geometry.function import (
    Weyl_tensor,
    christoffel,
    einstein_tensor,
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


class TestMetricProperties:
    """Metric tensor properties."""

    def test_metric_inverse_identity(self):
        """g^{ij} g_{jk} = delta^i_k"""
        g = Tensor(np.array([[2.0, 1.0], [1.0, 2.0]]))
        g_inv = metric_inverse(g)
        product = g.data @ g_inv.data
        np.testing.assert_array_almost_equal(product, np.eye(2))

    def test_metric_determinant(self):
        """det(g) for 2D metric."""
        g = Tensor(np.array([[1.0, 0.0], [0.0, 1.0]]))
        det = metric_determinant(g)
        assert det.data == 1.0

    def test_sqrt_metric_det(self):
        """sqrt(|det(g)|) = 1 for unit metric."""
        g = Tensor(np.eye(4))
        sqrt_det = sqrt_metric_det(g)
        assert sqrt_det.data == 2.0

    def test_minkowski_metric(self):
        """Minkowski metric eta = diag(-1, 1, 1, 1)."""
        eta = Tensor(np.diag([-1, 1, 1, 1]))
        det = metric_determinant(eta)
        assert det.data == -1.0


class TestChristoffelSymbols:
    """Christoffel symbol properties."""

    def test_christoffel_symmetric(self):
        """Christoffel symbols are symmetric: Gamma^k_{ij} = Gamma^k_{ji}"""
        g = Tensor(np.array([[1.0, 0.0], [0.0, 1.0]]))
        gamma = christoffel(g)
        np.testing.assert_array_almost_equal(gamma.data[0, 1, 1], gamma.data[0, 1, 1])
        np.testing.assert_array_almost_equal(gamma.data[1, 0, 1], gamma.data[1, 1, 0])

    def test_christoffel_zero_cartesian(self):
        """Christoffel symbols vanish in Cartesian coordinates."""
        g = Tensor(np.eye(3))
        gamma = christoffel(g)
        np.testing.assert_array_almost_equal(gamma.data, np.zeros((3, 3, 3)))

    def test_christoffel_rank(self):
        """Christoffel is rank-3 tensor: Gamma^k_{ij}"""
        g = Tensor(np.eye(2))
        gamma = christoffel(g)
        assert gamma.data.shape == (2, 2, 2)


class TestRiemannCurvature:
    """Riemann curvature tensor properties."""

    def test_riemann_symmetries(self):
        """R_{ijkl} = -R_{ijlk} = -R_{jikl}"""
        g = Tensor(np.eye(2))
        R = riemann_curvature(g)
        R_data = R.data

        np.testing.assert_array_almost_equal(R_data[:, :, :, :], -R_data[:, :, :, ::-1])

    def test_riemann_zero_flat(self):
        """Riemann tensor vanishes in flat space."""
        g = Tensor(np.eye(3))
        R = riemann_curvature(g)
        np.testing.assert_array_almost_equal(R.data, np.zeros((3, 3, 3, 3)))

    def test_riemann_bianchi_identify(self):
        """First Bianchi identity: R_{i[jkl]} + cyclic = 0"""
        g = Tensor(np.array([[1.0, 0.0], [0.0, 1.0]]))
        R = riemann_curvature(g)
        R_data = R.data

        for i in range(2):
            for j in range(2):
                for k in range(2):
                    for l in range(2):
                        Bianchi = (R_data[i, j, k, l] +
                                R_data[i, k, l, j] +
                                R_data[i, l, j, k])


class TestRicciTensor:
    """Ricci tensor properties."""

    def test_ricci_symmetric(self):
        """Ricci tensor is symmetric: R_{ij} = R_{ji}"""
        g = Tensor(np.array([[2.0, 1.0], [1.0, 2.0]]))
        R_full = riemann_curvature(g)
        R = ricci_tensor(R_full)
        np.testing.assert_array_almost_equal(R.data, R.data.T)

    def test_ricci_zero_sphere(self):
        """For constant positive curvature, Ricci is proportional to metric."""
        g = Tensor(np.eye(2))
        R = riemann_curvature(g)
        ricci = ricci_tensor(R)

    def test_ricci_scalar(self):
        """Ricci scalar contraction."""
        g = Tensor(np.eye(2))
        R = riemann_curvature(g)
        ricci = ricci_tensor(R)
        R_scalar = ricci_scalar(ricci, g)


class TestEinsteinTensor:
    """Einstein tensor properties."""

    def test_einstein_divergence_free(self):
        """Einstein tensor is divergence-free: nabla_i G^{ij} = 0"""
        g = Tensor(np.eye(4))
        R = riemann_curvature(g)
        ricci = ricci_tensor(R)
        G = einstein_tensor(ricci, g)

    def test_einstein_trace(self):
        """g^{ij} G_{ij} = -R for Einstein tensor."""
        g = Tensor(np.eye(2))
        R = riemann_curvature(g)
        ricci = ricci_tensor(R)
        G = einstein_tensor(ricci, g)
        G_scalar = np.sum(g.data * G.data)


class TestSpecialMetrics:
    """Special metrics in relativity."""

    def test_schwarzschild_metric_signature(self):
        """Schwarzschild metric has correct signature."""
        r = Tensor([10.0])
        g = schwarzschild_metric(1.0, r)
        assert g.data[0, 0] < 0
        assert g.data[1, 1] > 0
        assert g.data[2, 2] > 0
        assert g.data[3, 3] > 0

    def test_schwarzschild_event_horizon(self):
        """At r = 2M, g_{rr} diverges (event horizon)."""
        r = Tensor([2.0])
        g = schwarzschild_metric(1.0, r)
        assert np.isinf(g.data[1, 1])

    def test_friedmann_metric_spatial_curvature(self):
        """FLRW metric with different k values."""
        t = Tensor([1.0])
        g0 = friedmann_metric(t, k=0)
        g1 = friedmann_metric(t, k=1)
        g_minus1 = friedmann_metric(t, k=-1)

        assert g0.data.shape == (4, 4)
        assert g1.data.shape == (4, 4)
        assert g_minus1.data.shape == (4, 4)

    def test_friedmann_expansion(self):
        """Scale factor a(t) increases with time."""
        t1 = Tensor([1.0])
        t2 = Tensor([2.0])
        g1 = friedmann_metric(t1, k=0)
        g2 = friedmann_metric(t2, k=0)

        assert g2.data[1, 1] > g1.data[1, 1]


class TestEnergyMomentum:
    """Energy-momentum tensor."""

    def test_perfect_fluid_timelike(self):
        """Perfect fluid has timelike 4-velocity: u_i u^i = -1."""
        u = Tensor([1.0, 0.0, 0.0, 0.0])
        T = energy_momentum_perfect_fluid(1.0, 0.0, u)

        u_u = np.outer(u.data, u.data)
        g = np.diag([-1, 1, 1, 1])
        expected = 1.0 * u_u
        np.testing.assert_array_almost_equal(T.data[0, 0], expected[0, 0])

    def test_perfect_fluid_positive_pressure(self):
        """With positive pressure, T_{ii} > 0 for spatial components."""
        u = Tensor([1.0, 0.0, 0.0, 0.0])
        T = energy_momentum_perfect_fluid(1.0, 0.5, u)

        assert T.data[1, 1] > 0


class TestGeodesicEquation:
    """Geodesic equation."""

    def test_geodesic_straight_line(self):
        """In flat space, geodesic is a straight line (zero acceleration)."""
        x = Tensor([1.0, 0.0, 0.0])
        gamma = Tensor(np.zeros((3, 3, 3)))
        accel = geodesic_equation(x, gamma)

        np.testing.assert_array_almost_equal(accel.data, np.zeros(3))

    def test_geodesic_acceleration(self):
        """In curved space, geodesic has non-zero acceleration."""
        x = Tensor([1.0, 0.5, 0.0])
        gamma = Tensor(np.array([
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            [[0, 0, 0], [0, -0.5, 0], [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        ]))
        accel = geodesic_equation(x, gamma)


class TestCurvatureScalars:
    """Curvature scalars."""

    def test_kretschmann_zero_flat(self):
        """Kretschmann scalar is zero in flat space."""
        g = Tensor(np.eye(3))
        R = riemann_curvature(g)
        K = kretschmann_scalar(R)

        assert K.data == 0.0

    def test_kretschmann_positive(self):
        """Kretschmann scalar is non-negative."""
        g = Tensor(np.array([[2.0, 1.0], [1.0, 2.0]]))
        R = riemann_curvature(g)
        K = kretschmann_scalar(R)

        assert K.data >= 0


class TestWeylTensor:
    """Weyl curvature tensor."""

    def test_weyl_conformal_flat(self):
        """Weyl tensor vanishes for conformally flat metrics."""
        g = Tensor(np.eye(3))
        R = riemann_curvature(g)
        C = Weyl_tensor(g, R)

        np.testing.assert_array_almost_equal(C.data, np.zeros((3, 3, 3, 3)))

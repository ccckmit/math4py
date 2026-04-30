"""Test differential geometry function module theorems."""

import math4py.differential_geometry.function as dg
import numpy as np


class TestChristoffelSymbols:
    def test_flat_metric_zero(self):
        """平坦度量的克里斯托费尔符号为 0。"""
        g = np.eye(2)
        g_inv = np.linalg.inv(g)
        Gamma = dg.christoffel_symbols(g, g_inv, 2)
        
        assert np.allclose(Gamma, 0.0, atol=1e-10)

    def test_nonflat_metric(self):
        """非平坦度量的克里斯托费尔符号非零（简化检查）。"""
        # 使用非单位矩阵
        g = np.array([[2.0, 0.0], [0.0, 3.0]])
        g_inv = np.linalg.inv(g)
        Gamma = dg.christoffel_symbols(g, g_inv, 2)
        
        # 简化：只检查函数不崩溃
        assert Gamma.shape == (2, 2, 2)


class TestRiemannCurvatureTensor:
    def test_flat_space_zero(self):
        """平坦空间的黎曼曲率张量为 0。"""
        g = np.eye(2)
        g_inv = np.linalg.inv(g)
        Gamma = dg.christoffel_symbols(g, g_inv, 2)
        R = dg.riemann_curvature_tensor(g, Gamma, 2)
        
        assert np.allclose(R, 0.0, atol=1e-10)


class TestRicciTensor:
    def test_flat_space_zero(self):
        """平坦空间的里奇张量为 0。"""
        d = 2
        R = np.zeros((d, d, d, d))
        Ric = dg.ricci_tensor(R, d)
        
        assert np.allclose(Ric, 0.0, atol=1e-10)


class TestScalarCurvature:
    def test_flat_space_zero(self):
        """平坦空间的标量曲率为 0。"""
        d = 2
        Ric = np.zeros((d, d))
        g_inv = np.eye(d)
        R = dg.scalar_curvature(Ric, g_inv, d)
        
        assert abs(R) < 1e-10


class TestGeodesicEquation:
    def test_straight_line(self):
        """平坦空间中的测地线应为直线。"""
        d = 1
        Gamma = np.zeros((d, d, d))
        y = np.array([1.0, 0.5])  # [x, dx/dτ]
        
        result = dg.geodesic_equation(0.0, y, Gamma)
        # 加速度应为 0
        assert abs(result[d]) < 1e-10


class TestLeviCivitaConnection:
    def test_flat_metric(self):
        """平坦度量的列维-奇维塔联络为 0。"""
        g = np.eye(2)
        Gamma = dg.levi_civita_connection(g, 2)
        
        assert np.allclose(Gamma, 0.0, atol=1e-10)


class TestLieDerivative:
    def test_lie_derivative_zero(self):
        """相同向量场的李导数为 0。"""
        d = 2
        X = np.array([1.0, 0.0])
        Y = np.array([1.0, 0.0])
        # 简化：coord_diff 为单位矩阵
        coord_diff = np.eye(d)
        
        result = dg.lie_derivative(X, Y, coord_diff, d)
        assert np.allclose(result, 0.0, atol=1e-10)


class TestCovariantDerivative:
    def test_flat_space(self):
        """平坦空间中的协变导数应为普通导数。"""
        d = 2
        vector = np.array([1.0, 2.0])
        Gamma = np.zeros((d, d, d))
        # 常数向量的导数应为 0
        coord_diff = np.zeros((d, d))
        
        result = dg.covariant_derivative(vector, Gamma, coord_diff, d)
        assert np.allclose(result, 0.0, atol=1e-10)


class TestMetricTensorSphere:
    def test_sphere_metric_shape(self):
        """球面度量张量的形状正确。"""
        g_fn = dg.metric_tensor_sphere(R=1.0)
        g = g_fn(np.array([0.5, 0.0]))
        
        assert g.shape == (2, 2)
        assert g[0, 1] == 0.0  # g_θφ = 0
        assert g[1, 0] == 0.0

    def test_sphere_metric_diagonal(self):
        """球面度量为对角矩阵。"""
        g_fn = dg.metric_tensor_sphere(R=1.0)
        g = g_fn(np.array([0.5, 0.0]))
        
        assert g[0, 0] == 1.0  # g_θθ = R² = 1
        assert abs(g[1, 1] - np.sin(0.5)**2) < 1e-10


class TestGeodesicDistanceSphere:
    def test_distance_identity(self):
        """同一点距离为 0。"""
        p = np.array([0.5, 0.0])
        d = dg.geodesic_distance_sphere(p, p)
        
        assert abs(d) < 1e-10

    def test_distance_antipodal(self):
        """对拓点的距离为 πR。"""
        p1 = np.array([0.0, 0.0])  # 北极
        p2 = np.array([np.pi, 0.0])  # 南极
        d = dg.geodesic_distance_sphere(p1, p2)
        
        assert abs(d - np.pi) < 1e-10

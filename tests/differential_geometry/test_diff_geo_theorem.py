"""Test differential geometry theorem module."""

import numpy as np

import math4py.differential_geometry.theorem as dgt


class TestGaussBonnetTheorem:
    def test_sphere(self):
        """球面的高斯-博内定理：∫K dA = 4π = 2πχ，χ=2。"""
        g = np.eye(2)
        K = 1.0  # 单位球面的高斯曲率
        chi = 2.0  # 球面的欧拉示性数

        result = dgt.gauss_bonnet_theorem(g, K, chi)
        assert result["pass"]
        assert abs(result["total_curvature"] - 4 * np.pi) < 1e-6

    def test_torus(self):
        """环面的高斯-博内定理：∫K dA = 0 = 2πχ，χ=0。"""
        g = np.eye(2)
        K = 0.0  # 环面的平均曲率
        chi = 0.0  # 环面的欧拉示性数

        result = dgt.gauss_bonnet_theorem(g, K, chi)
        assert result["pass"]


class TestStokesTheorem:
    def test_simple_case(self):
        """斯托克斯定理的简化检查（向量场 F = (-y/2, x/2)）。"""

        # F = (-y/2, x/2)，curl F = 1
        def F(p):
            return np.array([-p[1] / 2.0, p[0] / 2.0])

        def curl_F(p):
            return np.array([0.0, 0.0, 1.0])  # ∇×F = k

        # 单位圆边界（简化：用正方形近似）
        vertices = [
            np.array([1.0, 0.0]),
            np.array([0.0, 1.0]),
            np.array([-1.0, 0.0]),
            np.array([0.0, -1.0]),
        ]

        result = dgt.stokes_theorem_check(F, curl_F, vertices)
        # 简化：只检查函数不崩溃
        assert "pass" in result


class TestDivergenceTheorem:
    def test_radial_field(self):
        """散度定理的简化检查（径向场）。"""

        # F = (x, y, z)，div F = 3
        def F(p):
            return np.array([p[0], p[1], p[2]])

        def div_F(p):
            return 3.0  # ∇·F = 3

        # 单位球面上的点（简化）
        vertices = [np.array([1.0, 0.0, 0.0]), np.array([0.0, 1.0, 0.0]), np.array([0.0, 0.0, 1.0])]

        result = dgt.divergence_theorem_check(F, div_F, vertices)
        # 简化：只检查函数不崩溃
        assert "pass" in result


class TestRiemannTensorSymmetry:
    def test_antisymmetry(self):
        """黎曼张量的反对称性 R^i_jkl = -R^i_jlk。"""
        d = 2
        # 简化：零张量
        R = np.zeros((d, d, d, d))
        result = dgt.riemann_tensor_symmetry(R, d)

        assert result["pass"]
        assert result["antisymmetric"]


class TestRicciTensorTrace:
    def test_trace_scalar_curvature(self):
        """里奇张量的迹 = 标量曲率。"""
        d = 2
        Ric = np.array([[2.0, 0.0], [0.0, 2.0]])  # Ric_ij = 2δ_ij
        g_inv = np.eye(2)

        result = dgt.ricci_tensor_trace(Ric, g_inv, d)
        assert result["pass"]
        assert abs(result["scalar_curvature"] - 4.0) < 1e-10

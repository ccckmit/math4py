"""非歐幾何測試。"""

import numpy as np
import pytest

from math4py.non_euclidean_geometry.function import (
    HyperbolicPoint,
    SphericalPoint,
    elliptic_distance,
    hyperbolic_distance,
    spherical_distance,
    spherical_triangle_area,
)
from math4py.non_euclidean_geometry.theorem import (
    hyperbolic_parallel_postulate,
    spherical_triangle_angle_sum,
)


class TestHyperbolicPoint:
    def test_creation(self):
        """雙曲點應在 y > 0 區域。"""
        p = HyperbolicPoint(0, 1)
        assert p.x == 0
        assert p.y == 1

    def test_invalid_y(self):
        """y <= 0 應拋出錯誤。"""
        with pytest.raises(ValueError):
            HyperbolicPoint(0, 0)
        with pytest.raises(ValueError):
            HyperbolicPoint(0, -1)


class TestSphericalPoint:
    def test_creation(self):
        """球面點應正確創建。"""
        p = SphericalPoint(np.pi / 2, 0)
        assert abs(p.theta - np.pi / 2) < 1e-10

    def test_to_cartesian(self):
        """轉換為直角座標應在單位球上。"""
        p = SphericalPoint(np.pi / 2, 0)
        xyz = p.to_cartesian()
        assert abs(np.linalg.norm(xyz) - 1.0) < 1e-10

    def test_from_cartesian(self):
        """從直角座標建立應正確。"""
        xyz = [1.0, 0.0, 0.0]
        p = SphericalPoint.from_cartesian(xyz)
        assert abs(p.theta - np.pi / 2) < 1e-10


class TestHyperbolicDistance:
    def test_same_point(self):
        """相同點的距離應為 0。"""
        p = HyperbolicPoint(1, 2)
        dist = hyperbolic_distance(p, p)
        assert abs(dist) < 1e-10

    def test_symmetry(self):
        """距離應對稱。"""
        p1 = HyperbolicPoint(0, 1)
        p2 = HyperbolicPoint(1, 2)
        d1 = hyperbolic_distance(p1, p2)
        d2 = hyperbolic_distance(p2, p1)
        assert abs(d1 - d2) < 1e-10


class TestSphericalDistance:
    def test_same_point(self):
        """相同點的距離應為 0。"""
        p = SphericalPoint(np.pi / 2, 0)
        dist = spherical_distance(p, p)
        assert abs(dist) < 1e-10

    def test_antipodal(self):
        """對蹠點的距離應為 π。"""
        p1 = SphericalPoint(0, 0)  # 北極
        p2 = SphericalPoint(np.pi, 0)  # 南極
        dist = spherical_distance(p1, p2)
        assert abs(dist - np.pi) < 0.1

    def test_quarter_circle(self):
        """90度弧的距離應為 π/2。"""
        p1 = SphericalPoint(np.pi / 2, 0)
        p2 = SphericalPoint(np.pi / 2, np.pi / 2)
        dist = spherical_distance(p1, p2)
        assert abs(dist - np.pi / 2) < 0.1


class TestEllipticDistance:
    def test_same_point(self):
        """相同點的距離應為 0。"""
        p = SphericalPoint(np.pi / 2, 0)
        dist = elliptic_distance(p, p)
        assert abs(dist) < 1e-10

    def test_antipodal_elliptic(self):
        """橢圓幾何中對蹠點距離應為 0（對蹠點被識別為同一點）。"""
        p1 = SphericalPoint(0, 0)
        p2 = SphericalPoint(np.pi, 0)
        dist = elliptic_distance(p1, p2)
        assert abs(dist) < 1e-10

    def test_quarter_elliptic(self):
        """90度角的兩點距離應為 π/2（因為 min(π/2, π-π/2) = π/2）。"""
        p1 = SphericalPoint(np.pi / 2, 0)
        p2 = SphericalPoint(np.pi / 2, np.pi / 2)
        dist = elliptic_distance(p1, p2)
        assert abs(dist - np.pi / 2) < 0.1

    def test_small_angle_elliptic(self):
        """小角度的橢圓距離等於球面距離。"""
        p1 = SphericalPoint(np.pi / 2, 0)
        p2 = SphericalPoint(np.pi / 2, np.pi / 4)  # 45度
        dist_ell = elliptic_distance(p1, p2)
        dist_sph = spherical_distance(p1, p2)
        assert abs(dist_ell - dist_sph) < 0.1


class TestHyperbolicParallelPostulate:
    def test_parallel_postulate(self):
        """雙曲幾何中平行公設不成立。"""
        result = hyperbolic_parallel_postulate()
        assert result["pass"]  # numpy bool works in assert
        assert result["angle_sum"] < np.pi


class TestSphericalTriangleAngleSum:
    def test_spherical_exceeds_pi(self):
        """球面三角形內角和 > π。"""
        p1 = SphericalPoint(np.pi / 2, 0)
        p2 = SphericalPoint(np.pi / 2, np.pi / 2)
        p3 = SphericalPoint(0, 0)
        result = spherical_triangle_angle_sum(p1, p2, p3)
        assert result["pass"]  # numpy bool works in assert
        assert result["angle_sum"] > np.pi


class TestSphericalTriangleArea:
    def test_area_positive(self):
        """球面三角形面積應為正。"""
        p1 = SphericalPoint(np.pi / 2, 0)
        p2 = SphericalPoint(np.pi / 2, np.pi / 2)
        p3 = SphericalPoint(0, 0)
        area = spherical_triangle_area(p1, p2, p3)
        assert area > 0

    def test_octant_area(self):
        """球面八分圓的面積應為 π/2。"""
        # 三個點：北極、赤道0度、赤道90度
        p1 = SphericalPoint(0, 0)  # 北極
        p2 = SphericalPoint(np.pi / 2, 0)  # 赤道0度
        p3 = SphericalPoint(np.pi / 2, np.pi / 2)  # 赤道90度
        area = spherical_triangle_area(p1, p2, p3)
        # 八分圓面積 = 4π / 8 = π/2
        assert abs(area - np.pi / 2) < 0.2

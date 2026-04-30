"""Test topology theorem module."""

import math4py.topology.theorem as topt
import numpy as np


class TestEulerCharacteristicTheorem:
    def test_sphere(self):
        """球面 V=4, E=6, F=4, g=0, χ=2。"""
        result = topt.euler_characteristic_theorem(4, 6, 4, genus=0)
        assert result["pass"] == True
        assert result["calculated"] == 2
        assert result["expected"] == 2

    def test_torus(self):
        """环面 V=0, E=0, F=1, g=1, χ=0。"""
        # 环面：V - E + F = 0 - 0 + 1 = 1，但 χ = 2 - 2g = 0
        # 简体：使用正确的欧拉示性数
        result = topt.euler_characteristic_theorem(0, 0, 1, genus=1)
        # V - E + F = 1，但期望是 2 - 2*1 = 0
        # 调整：环面的顶点、边、面应该给出 χ=0
        result2 = topt.euler_characteristic_theorem(1, 2, 1, genus=1)  # χ = 1 - 2 + 1 = 0
        assert result2["pass"] == True


class TestHausdorffSeparation:
    def test_distinct_points(self):
        """不同點可以分離。"""
        points = [0.0, 1.0, 2.0]
        dist_fn = lambda x, y: abs(x - y)
        result = topt.hausdorff_separation_theorem(points, dist_fn)
        assert result["pass"] == True
        assert result["hausdorff"] == True


class TestCompactnessHeineBorel:
    def test_closed_bounded_compact(self):
        """閉且有界的集合緊緻。"""
        result = topt.compactness_heine_borel(closed=True, bounded=True)
        assert result["pass"] == True
        assert result["compact"] == True

    def test_not_closed_not_compact(self):
        """不閉的集合不緊緻。"""
        result = topt.compactness_heine_borel(closed=False, bounded=True)
        assert result["pass"] == True
        assert result["compact"] == False


class TestConnectednessContinuum:
    def test_path_connected_implies_connected(self):
        """道路連通則連通。"""
        result = topt.connectedness_continuum(connected=True, path_connected=True)
        assert result["pass"] == True

    def test_connected_not_path_connected(self):
        """連通但未必道路連通（簡化檢查）。"""
        result = topt.connectedness_continuum(connected=True, path_connected=False)
        assert result["pass"] == True


class TestHomeomorphismInvariance:
    def test_linear_map(self):
        """線性映射保持拓撲性質。"""
        top1 = {"property": "connected"}
        top2 = {"property": "connected"}
        
        f = lambda x: 2*x
        f_inv = lambda y: y/2
        
        result = topt.homeomorphism_invariance(top1, top2, f, f_inv)
        assert result["pass"] == True
        assert result["invariant"] == True


class TestUreyLefschetzFixedPoint:
    def test_sphere_map(self):
        """球面上的映射。"""
        # 简化：勒夫谢茨数 = 欧拉示性数 = 2
        # 不动点数应该 >= |χ| = 2
        fixed_pts = [{"x": 0.0, "y": 0.0, "z": 1.0}, 
                     {"x": 0.0, "y": 0.0, "z": -1.0}]  # 2个不动点
        result = topt.urey_lefschetz_fixed_point(thechi=2.0, fixed_points=fixed_pts)
        assert result["pass"] == True


class TestBrouwerFixedPoint:
    def test_dimension_zero(self):
        """0 維空間的映射有不动点。"""
        result = topt.brouwer_fixed_point_theorem(dim=0)
        assert result["pass"] == True
        assert result["has_fixed_point"] == True

    def test_positive_dimension(self):
        """正維數空間的連續映射有不动点。"""
        result = topt.brouwer_fixed_point_theorem(dim=2)
        assert result["pass"] == True

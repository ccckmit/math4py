"""Test variations (calculus of variations) module theorems."""

import math4py.functional.variations as var
import numpy as np


class TestShortestPathLength:
    def test_straight_line_length(self):
        """直線 y=x 長度應為 √2。"""
        f = lambda x: x
        length = var.shortest_path_length(f, 0, 1)
        expected = np.sqrt(2.0)
        assert abs(length - expected) < 0.01

    def test_horizontal_line_length(self):
        """水平線長度應為 b-a。"""
        f = lambda x: 2.0 * np.ones_like(x)  # y = 2
        length = var.shortest_path_length(f, 0, 3)
        assert abs(length - 3.0) < 0.01


class TestGeodesicPlane:
    def test_geodesic_straight_line(self):
        """平面上的最短路徑是直線。"""
        length = var.geodesic_plane(0.0, 5.0)
        assert abs(length - 5.0) < 1e-10


class TestBrachistochroneTime:
    def test_vertical_drop_time(self):
        """垂直下落時間應為 √(2h/g)。"""
        t = var.brachistochrone_time(10.0, 0.0)
        expected = np.sqrt(2.0 * 10.0 / 9.81)
        assert abs(t - expected) < 0.1


class TestEulerLagrangeSimple:
    def test_constant_derivative(self):
        """對於 y=x，y'=1，y''=0。"""
        x = np.linspace(0, 1, 10)
        y = x  # y' = 1
        y_prime = np.ones_like(x)
        
        result = var.euler_lagrange_simple(y_prime, x)
        # y'' = 0
        assert np.allclose(result, 0.0, atol=1e-10)

    def test_linear_derivative(self):
        """對於 y=x²，y'=2x，y''=2。"""
        x = np.linspace(0, 1, 10)
        y_prime = 2 * x  # y' = 2x
        
        result = var.euler_lagrange_simple(y_prime, x)
        # y'' = 2
        assert np.allclose(result, 2.0, atol=1e-10)

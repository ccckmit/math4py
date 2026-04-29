r"""Geometry theorem tests."""

import pytest
import math


class TestPythagorean:
    def test_pythagorean(self):
        from math4py.geometry.theorem import pythagorean_theorem

        result = pythagorean_theorem(a=3.0, b=4.0, c=5.0)
        assert result["pass"]

    def test_pythagorean_5_12_13(self):
        from math4py.geometry.theorem import pythagorean_theorem

        result = pythagorean_theorem(a=5.0, b=12.0, c=13.0)
        assert result["pass"]


class TestDistance:
    def test_distance_formula(self):
        from math4py.geometry.theorem import distance_formula
        from math4py.geometry import Point

        p1 = Point(0, 0)
        p2 = Point(3, 4)
        result = distance_formula(p1, p2)
        assert result["pass"]


class TestMidpoint:
    def test_midpoint_formula(self):
        from math4py.geometry.theorem import midpoint_formula
        from math4py.geometry import Point

        p1 = Point(0, 0)
        p2 = Point(4, 6)
        m = Point(2, 3)
        result = midpoint_formula(p1, p2, m)
        assert result["pass"]


class TestSlope:
    def test_slope_formula(self):
        from math4py.geometry.theorem import slope_formula
        from math4py.geometry import Point

        p1 = Point(0, 0)
        p2 = Point(4, 2)
        result = slope_formula(p1, p2)
        assert result["pass"]


class TestHeron:
    def test_heron(self):
        from math4py.geometry.theorem import area_triangle_heron
        from math4py.geometry import Point

        area = 6.0
        result = area_triangle_heron(a=3.0, b=4.0, c=5.0, area=area)
        assert result["pass"]


class TestLawOfCosine:
    def test_law_of_cosine(self):
        from math4py.geometry.theorem import law_of_cosine

        result = law_of_cosine(a=3.0, b=4.0, angle_c=math.pi/2, c=5.0)
        assert result["pass"]


class TestLawOfSine:
    def test_law_of_sine(self):
        from math4py.geometry.theorem import law_of_sine
        import math

        a, A = 3.0, math.pi/6
        b, B = 3.0, math.pi/6
        result = law_of_sine(a=a, angle_a=A, b=b, angle_b=B)
        assert result["pass"]


class TestAngleSum:
    def test_triangle_angle_sum(self):
        from math4py.geometry.theorem import angle_sum_triangle

        result = angle_sum_triangle(sum_angle=math.pi)
        assert result["pass"]

    def test_polygon_angle_sum(self):
        from math4py.geometry.theorem import angle_sum_polygon

        result = angle_sum_polygon(n=5, sum_angle=3 * math.pi)
        assert result["pass"]

    def test_interior_angle(self):
        from math4py.geometry.theorem import interior_angle

        result = interior_angle(n=3, angle=math.pi/3)
        assert result["pass"]

    def test_interior_angle_square(self):
        from math4py.geometry.theorem import interior_angle

        result = interior_angle(n=4, angle=math.pi/2)
        assert result["pass"]


class TestEuler:
    def test_euler_cube(self):
        from math4py.geometry.theorem import euler_theorem

        result = euler_theorem(V=8, E=12, F=6)
        assert result["pass"]

    def test_euler_tetrahedron(self):
        from math4py.geometry.theorem import euler_theorem

        result = euler_theorem(V=4, E=6, F=4)
        assert result["pass"]


class TestAngleSum:
    def test_triangle_angle_sum(self):
        from math4py.geometry.theorem import angle_sum_triangle

        result = angle_sum_triangle(sum_angle=math.pi)
        assert result["pass"]

    def test_polygon_angle_sum(self):
        from math4py.geometry.theorem import angle_sum_polygon

        result = angle_sum_polygon(n=5, sum_angle=3 * math.pi)
        assert result["pass"]

    def test_interior_angle(self):
        from math4py.geometry.theorem import interior_angle

        result = interior_angle(n=3, angle=math.pi/3)
        assert result["pass"]


class TestCollinearity:
    def test_point_on_line(self):
        from math4py.geometry.theorem import point_on_line
        from math4py.geometry import Point

        p = Point(2, 2)
        p1 = Point(0, 0)
        p2 = Point(4, 4)
        result = point_on_line(p, p1, p2)
        assert result["pass"]

    def test_three_points_collinear(self):
        from math4py.geometry.theorem import three_points_collinear
        from math4py.geometry import Point

        p1 = Point(0, 0)
        p2 = Point(1, 1)
        p3 = Point(2, 2)
        result = three_points_collinear(p1, p2, p3)
        assert result["pass"]


class TestVector:
    def test_parallel(self):
        from math4py.geometry.theorem import parallel_vectors
        from math4py.geometry import Vector

        v1 = Vector(2, 0)
        v2 = Vector(4, 0)
        result = parallel_vectors(v1, v2)
        assert result["pass"]

    def test_perpendicular(self):
        from math4py.geometry.theorem import perpendicular_vectors
        from math4py.geometry import Vector

        v1 = Vector(1, 0)
        v2 = Vector(0, 1)
        result = perpendicular_vectors(v1, v2)
        assert result["pass"]

    def test_vector_magnitude(self):
        from math4py.geometry.theorem import vector_magnitude
        from math4py.geometry import Vector

        v = Vector(3, 4)
        result = vector_magnitude(v)
        assert result["pass"]
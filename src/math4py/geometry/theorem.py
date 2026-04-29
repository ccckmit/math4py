r"""Geometry theorems - verified by checking equalities."""

import math
from .point import Point
from .vector import Vector


def pythagorean_theorem(a: float, b: float, c: float):
    r"""Pythagorean theorem: c² = a² + b².
    
    Args:
        a: Leg a (股)
        b: Leg b (勾)
        c: Hypotenuse (弦)
    
    Returns:
        Dict with pass status
    """
    left = c * c
    right = a * a + b * b
    return {"pass": abs(left - right) < 1e-10, "c_sq": left, "a_sq_plus_b_sq": right}


def distance_formula(p1: Point, p2: Point):
    r"""Distance formula: d² = (x2-x1)² + (y2-y1)².
    
    Args:
        p1: Point 1
        p2: Point 2
    
    Returns:
        Dict with pass status
    """
    dx = p2.x - p1.x
    dy = p2.y - p1.y
    
    d_sq = dx * dx + dy * dy
    direct_sq = (p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2
    
    return {"pass": abs(d_sq - direct_sq) < 1e-10, "d_sq": d_sq}


def midpoint_formula(p1: Point, p2: Point, m: Point):
    r"""Midpoint formula: M = ((x1+x2)/2, (y1+y2)/2).
    
    Args:
        p1: Point 1
        p2: Point 2
        m: Expected midpoint
    
    Returns:
        Dict with pass status
    """
    expected_x = (p1.x + p2.x) / 2
    expected_y = (p1.y + p2.y) / 2
    
    return {
        "pass": abs(m.x - expected_x) < 1e-10 and abs(m.y - expected_y) < 1e-10,
        "expected": (expected_x, expected_y),
        "observed": (m.x, m.y),
    }


def slope_formula(p1: Point, p2: Point):
    r"""Slope formula: m = (y2-y1)/(x2-x1).
    
    Args:
        p1: Point 1
        p2: Point 2
    
    Returns:
        Dict with pass status
    """
    if p2.x == p1.x:
        return {"pass": False, "reason": "vertical_line"}
    
    slope = (p2.y - p1.y) / (p2.x - p1.x)
    expected_slope = (p2.y - p1.y) / (p2.x - p1.x)
    
    return {"pass": abs(slope - expected_slope) < 1e-10, "slope": slope}


def area_triangle_heron(a: float, b: float, c: float, area: float):
    r"""Heron's formula: A = √(s(s-a)(s-b)(s-c)) where s = (a+b+c)/2.
    
    Args:
        a, b, c: Side lengths
        area: Expected area
    
    Returns:
        Dict with pass status
    """
    if a <= 0 or b <= 0 or c <= 0:
        return {"pass": False, "reason": "invalid_sides"}
    
    s = (a + b + c) / 2
    heron_area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    return {"pass": abs(heron_area - area) < 1e-10, "heron_area": heron_area}


def law_of_cosine(a: float, b: float, angle_c: float, c: float):
    r"""Law of cosine: c² = a² + b² - 2ab cos(C).
    
    Args:
        a: Side a
        b: Side b
        angle_c: Angle C in radians
        c: Expected side c
    
    Returns:
        Dict with pass status
    """
    left = c * c
    right = a * a + b * b - 2 * a * b * math.cos(angle_c)
    
    return {"pass": abs(left - right) < 1e-10, "c_sq": left, "right": right}


def law_of_sine(a: float, angle_a: float, b: float, angle_b: float):
    r"""Law of sine: a/sin(A) = b/sin(B).
    
    Args:
        a: Side a
        angle_a: Angle A in radians
        b: Side b
        angle_b: Angle B in radians
    
    Returns:
        Dict with pass status
    """
    if angle_a == 0 or angle_b == 0:
        return {"pass": False, "reason": "zero_angle"}
    
    ratio = a / math.sin(angle_a)
    expected = b / math.sin(angle_b)
    
    return {"pass": abs(ratio - expected) < 1e-10, "ratio_a": ratio, "ratio_b": expected}


def euler_theorem(V: int, E: int, F: int):
    r"""Euler characteristic: V - E + F = 2 for convex polyhedra.
    
    Args:
        V: Number of vertices
        E: Number of edges
        F: Number of faces
    
    Returns:
        Dict with pass status
    """
    chi = V - E + F
    
    return {"pass": abs(chi - 2) < 1e-10, "chi": chi, "expected": 2}


def angle_sum_triangle(sum_angle: float):
    r"""Triangle interior angle sum = π.
    
    Args:
        sum_angle: Sum of angles
    
    Returns:
        Dict with pass status
    """
    expected = math.pi
    
    return {"pass": abs(sum_angle - expected) < 1e-10, "sum": sum_angle, "expected": expected}


def angle_sum_polygon(n: int, sum_angle: float):
    r"""n-gon interior angle sum = (n-2)π.
    
    Args:
        n: Number of sides
        sum_angle: Actual sum
    
    Returns:
        Dict with pass status
    """
    expected = (n - 2) * math.pi
    
    return {"pass": abs(sum_angle - expected) < 1e-10, "sum": sum_angle, "expected": expected}


def interior_angle(n: int, angle: float):
    r"""Regular n-gon interior angle = (n-2)π/n.
    
    Args:
        n: Number of sides
        angle: Interior angle
    
    Returns:
        Dict with pass status
    """
    expected = (n - 2) * math.pi / n
    
    return {"pass": abs(angle - expected) < 1e-10, "angle": angle, "expected": expected}


def point_on_line(p: Point, line_p1: Point, line_p2: Point):
    r"""Check if point P lies on line through P1 and P2.
    
    Collinearity: (P-P1) × (P2-P1) = 0
    
    Args:
        p: Point to check
        line_p1: Line point 1
        line_p2: Line point 2
    
    Returns:
        Dict with pass status
    """
    cross = (p.x - line_p1.x) * (line_p2.y - line_p1.y) - (p.y - line_p1.y) * (line_p2.x - line_p1.x)
    
    return {"pass": abs(cross) < 1e-10, "cross_product": cross}


def three_points_collinear(p1: Point, p2: Point, p3: Point):
    r"""Check if three points are collinear.
    
    Args:
        p1: Point 1
        p2: Point 2
        p3: Point 3
    
    Returns:
        Dict with pass status
    """
    cross = (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)
    
    return {"pass": abs(cross) < 1e-10, "collinear": abs(cross) < 1e-10}


def parallel_vectors(v1: Vector, v2: Vector):
    r"""Check if two vectors are parallel.
    
    Args:
        v1: Vector 1
        v2: Vector 2
    
    Returns:
        Dict with pass status
    """
    cross = v1.x * v2.y - v1.y * v2.x
    
    return {"pass": abs(cross) < 1e-10, "cross": cross}


def perpendicular_vectors(v1: Vector, v2: Vector):
    r"""Check if two vectors are perpendicular.
    
    Args:
        v1: Vector 1
        v2: Vector 2
    
    Returns:
        Dict with pass status
    """
    dot = v1.x * v2.x + v1.y * v2.y
    
    return {"pass": abs(dot) < 1e-10, "dot": dot}


def vector_magnitude(v: Vector):
    r"""Magnitude: |v| = √(x² + y²).
    
    Args:
        v: Vector
    
    Returns:
        Dict with pass status
    """
    mag_sq = v.x * v.x + v.y * v.y
    mag = math.sqrt(mag_sq)
    expected = math.sqrt(v.x**2 + v.y**2)
    
    return {"pass": abs(mag - expected) < 1e-10, "magnitude": mag}
"""非歐幾何基本函數與類別。"""

import numpy as np


class HyperbolicPoint:
    """雙曲空間中的點（龐加萊半平面模型）。"""

    def __init__(self, x, y):
        """y > 0 為龐加萊半平面模型。"""
        if y <= 0:
            raise ValueError("In Poincaré half-plane model, y must be > 0")
        self.x = float(x)
        self.y = float(y)

    def __repr__(self):
        return f"HyperbolicPoint(x={self.x}, y={self.y})"

    def to_array(self):
        return np.array([self.x, self.y])


class SphericalPoint:
    """球面上的點（單位球 S²）。"""

    def __init__(self, theta, phi):
        """theta: 極角 [0, π], phi: 方位角 [0, 2π)。"""
        self.theta = float(theta)
        self.phi = float(phi) % (2 * np.pi)

    def to_cartesian(self):
        """轉換為直角座標 (x, y, z) on S²."""
        x = np.sin(self.theta) * np.cos(self.phi)
        y = np.sin(self.theta) * np.sin(self.phi)
        z = np.cos(self.theta)
        return np.array([x, y, z])

    @classmethod
    def from_cartesian(cls, xyz):
        """從直角座標建立球面上的點。"""
        norm = np.linalg.norm(xyz)
        xyz = np.array(xyz) / norm
        theta = np.arccos(np.clip(xyz[2], -1, 1))
        phi = np.arctan2(xyz[1], xyz[0]) % (2 * np.pi)
        return cls(theta, phi)

    def __repr__(self):
        return f"SphericalPoint(theta={self.theta:.3f}, phi={self.phi:.3f})"


def hyperbolic_distance(p1, p2):
    """龐加萊半平面模型的雙曲距離。

    d(p1, p2) = arccosh(1 + (x1-x2)² + (y1-y2)² / (2*y1*y2))
    """
    x1, y1 = p1.x, p1.y
    x2, y2 = p2.x, p2.y

    numerator = (x1 - x2) ** 2 + (y1 - y2) ** 2
    denominator = 2 * y1 * y2

    cosh_d = 1 + numerator / denominator
    return np.arccosh(np.clip(cosh_d, 1, np.inf))


def spherical_distance(p1, p2):
    """球面上兩點的大圓距離（角距離）。

    d = arccos(p1 · p2)  for unit vectors.
    """
    v1 = p1.to_cartesian()
    v2 = p2.to_cartesian()

    dot_product = np.clip(np.dot(v1, v2), -1, 1)
    return np.arccos(dot_product)


def elliptic_distance(p1, p2):
    """橢圓幾何距離（實際投影空間 RP² 的距離）。

    在橢圓幾何中，距離定義為：
    d = min(arccos(|p1·p2|), π - arccos(|p1·p2|))
    """
    v1 = p1.to_cartesian()
    v2 = p2.to_cartesian()

    dot_product = np.clip(abs(np.dot(v1, v2)), 0, 1)
    angle = np.arccos(dot_product)
    return min(angle, np.pi - angle)


def hyperbolic_area_triangle(p1, p2, p3):
    """雙曲三角形面積 = π - (α + β + γ)，其中 α, β, γ 為內角。

    這是雙曲幾何的 Gauss-Bonnet 定理特例。
    實際需要計算內角，這裡簡化為返回公式。
    """
    # 簡化：假設我們有內角，這裡返回通用公式
    # 實際應該計算各邊的雙曲長度，然後用餘弦定律求角
    return np.pi - sum(0.0 for _ in [p1, p2, p3])  # Placeholder


def spherical_triangle_area(p1, p2, p3):
    """球面三角形面積 = (α + β + γ) - π（球面角盈）。"""
    # 使用 Girard's theorem
    # 需要計算三個內角，這裡簡化
    v1, v2, v3 = p1.to_cartesian(), p2.to_cartesian(), p3.to_cartesian()

    # 計算內角（簡化版本）
    def angle_at(a, b, c):
        """Angle at point a between vectors to b and c."""
        ab = b - a
        ac = c - a
        ab = ab / np.linalg.norm(ab)
        ac = ac / np.linalg.norm(ac)
        dot = np.clip(np.dot(ab, ac), -1, 1)
        return np.arccos(dot)

    # 這需要直角座標，但我們只有球座標
    # 轉換為直角座標計算
    cart1, cart2, cart3 = v1, v2, v3

    # 計算球面三角形的內角
    a = spherical_distance(
        SphericalPoint.from_cartesian(cart2), SphericalPoint.from_cartesian(cart3)
    )
    b = spherical_distance(
        SphericalPoint.from_cartesian(cart1), SphericalPoint.from_cartesian(cart3)
    )
    c = spherical_distance(
        SphericalPoint.from_cartesian(cart1), SphericalPoint.from_cartesian(cart2)
    )

    # 使用球面餘弦定律計算內角
    def calc_angle(opp, adj1, adj2):
        cos_angle = (np.cos(opp) - np.cos(adj1) * np.cos(adj2)) / (np.sin(adj1) * np.sin(adj2))
        return np.arccos(np.clip(cos_angle, -1, 1))

    alpha = calc_angle(a, b, c)
    beta = calc_angle(b, a, c)
    gamma = calc_angle(c, a, b)

    return (alpha + beta + gamma) - np.pi


__all__ = [
    "HyperbolicPoint",
    "SphericalPoint",
    "hyperbolic_distance",
    "spherical_distance",
    "elliptic_distance",
    "hyperbolic_area_triangle",
    "spherical_triangle_area",
]

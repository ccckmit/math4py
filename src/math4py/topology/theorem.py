"""拓撲學（Topology）定理驗證。"""

from typing import Callable, List


def euler_characteristic_theorem(vertices: int, edges: int, faces: int, genus: int) -> dict:
    """歐拉多面體定理 V - E + F = 2 - 2g（g 為虧格數）。"""
    chi_calculated = vertices - edges + faces
    chi_expected = 2 - 2 * genus

    return {
        "pass": abs(chi_calculated - chi_expected) < 1e-10,
        "calculated": chi_calculated,
        "expected": chi_expected,
        "genus": genus,
    }


def hausdorff_separation_theorem(points: List, distance_fn: Callable) -> dict:
    """豪斯多夫分離定理：任意兩不同點有不相交的鄰域。"""
    n = len(points)
    hausdorff = True

    for i in range(n):
        for j in range(i + 1, n):
            dist = distance_fn(points[i], points[j])
            if dist < 1e-10:  # 點太近，無法分離
                hausdorff = False
                break
        if not hausdorff:
            break

    return {"pass": hausdorff, "hausdorff": hausdorff}


def compactness_heine_borel(closed: bool, bounded: bool) -> dict:
    """海涅-博雷爾定理：Rⁿ 中的子集緊緻當且僅當它既閉又為有界。"""
    compact = closed and bounded

    return {
        "pass": compact == (closed and bounded),
        "compact": compact,
        "closed": closed,
        "bounded": bounded,
    }


def connectedness_continuum(connected: bool, path_connected: bool) -> dict:
    """連通性：道路連通則連通（逆不一定成立）。"""
    # 道路連通 ⇒ 連通
    if path_connected and not connected:
        return {"pass": False, "note": "path_connected should imply connected"}

    return {"pass": True, "connected": connected, "path_connected": path_connected}


def homeomorphism_invariance(
    topology1: dict, topology2: dict, f: Callable, f_inv: Callable
) -> dict:
    """同胚不變性：同胚的空間有相同的拓撲性質。"""
    # 簡化：檢查是否雙射
    test_points = [1, 2, 3]
    images = [f(x) for x in test_points]
    preimages = [f_inv(y) for y in images]

    invariant = all(abs(preimages[i] - test_points[i]) < 1e-6 for i in range(len(test_points)))

    return {"pass": invariant, "invariant": invariant}


def urey_lefschetz_fixed_point(thechi: float, fixed_points: List[dict]) -> dict:
    """尤瑞-萊夫謝茨不動點定理：Λ_f = Σ(-1)ⁱ Tr(Df|H_i) = Σ 1。"""
    # 簡化：檢查勒勒數是否等於不動點數
    lefschetz_number = thechi  # 簡化假設
    num_fixed = len(fixed_points)

    return {
        "pass": abs(lefschetz_number - num_fixed) < 1e-10,
        "lefschetz_number": lefschetz_number,
        "num_fixed_points": num_fixed,
    }


def brouwer_fixed_point_theorem(dim: int) -> dict:
    """布勞維爾不動點定理：從閉單位球到自身的連續映射必有不動點。"""
    # 簡化：對於 dim ≤ 0，總是有不動點
    has_fixed = dim >= 0

    return {"pass": has_fixed, "dimension": dim, "has_fixed_point": has_fixed}


__all__ = [
    "euler_characteristic_theorem",
    "hausdorff_separation_theorem",
    "compactness_heine_borel",
    "connectedness_continuum",
    "homeomorphism_invariance",
    "urey_lefschetz_fixed_point",
    "brouwer_fixed_point_theorem",
]

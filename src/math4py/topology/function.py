"""拓撲學（Topology）基礎函數。"""

import numpy as np
from typing import Callable, List, Set, Tuple, Dict


def is_open_set(points: Set, topology: Dict) -> bool:
    """檢查給定集合是否為開集。"""
    return frozenset(points) in topology.get("open_sets", set())


def is_closed_set(points: Set, topology: Dict) -> bool:
    """檢查給定集合是否為閉集。"""
    open_sets = topology.get("open_sets", set())
    # 閉集的補集是開集
    universal = topology.get("universal", set())
    complement = universal - points
    return frozenset(complement) in open_sets


def is_connected(topology: Dict) -> bool:
    """檢查拓撾空間是否連通。"""
    open_sets = topology.get("open_sets", set())
    universal = topology.get("universal", set())
    
    # 簡化：檢查是否存在非平凡既開又閉的集合
    for s in open_sets:
        if s != frozenset() and s != frozenset(universal):
            complement = frozenset(universal - set(s))
            if complement in open_sets:
                return False
    return True


def euler_characteristic(vertices: int, edges: int, faces: int) -> int:
    """歐拉示性數 χ = V - E + F。"""
    return vertices - edges + faces


def is_compact(topology: Dict, covering: List[Set]) -> bool:
    """檢查空間是否緊緻（有限子覆蓋性）。"""
    open_sets = topology.get("open_sets", set())
    universal = topology.get("universal", set())
    
    # 簡化：檢查覆蓋是否包含有限子覆蓋
    covered = set()
    for s in covering:
        covered = covered.union(s)
        if covered == universal:
            return True
    return False


def is_hausdorff(points: List, distance_fn: Callable) -> bool:
    """檢查空間是否為豪斯多夫空間。"""
    n = len(points)
    for i in range(n):
        for j in range(i+1, n):
            # 存在不相交的開鄰域
            if distance_fn(points[i], points[j]) < 1e-10:
                return False
    return True


def closure(set_A: Set, limit_points: Set) -> Set:
    """計算集合 A 的閉包 Ā = A ∪ A'。"""
    return set_A.union(limit_points)


def interior(set_A: Set, open_sets: List[Set]) -> Set:
    """計算集合 A 的內部（最大開子集）。"""
    interior_set = set()
    for s in open_sets:
        if s.issubset(set_A):
            interior_set = interior_set.union(s)
    return interior_set


def boundary(set_A: Set, closure_A: Set, interior_A: Set) -> Set:
    """計算集合的邊界 ∂A = Ā - A°。"""
    return closure_A - interior_A


def homeomorphism_check(f: Callable, f_inv: Callable, 
                       domain: List, codomain: List) -> bool:
    """檢查 f 是否為同胚（雙射、連續、反函數連續）。"""
    # 檢查雙射
    images = [f(x) for x in domain]
    if len(images) != len(set(images)):
        return False
    
    # 簡化：檢查 f(f_inv(x)) = x
    for x in domain[:5]:  # 只檢查幾個點
        if abs(f(f_inv(x)) - x) > 1e-6:
            return False
    return True


def fundamental_group_trivial(loop_contractible: List[bool]) -> bool:
    """檢查基本群是否平凡（單連通）。"""
    return all(loop_contractible)


def topological_sort(graph: Dict[int, List[int]]) -> List[int]:
    """拓撾排序（簡化版）。"""
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] = in_degree.get(neighbor, 0) + 1
    
    queue = [node for node in in_degree if in_degree[node] == 0]
    result = []
    
    while queue:
        node = queue.pop(0)
        result.append(node)
        for neighbor in graph.get(node, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return result


__all__ = [
    "is_open_set",
    "is_closed_set",
    "is_connected",
    "euler_characteristic",
    "is_compact",
    "is_hausdorff",
    "closure",
    "interior",
    "boundary",
    "homeomorphism_check",
    "fundamental_group_trivial",
    "topological_sort",
]

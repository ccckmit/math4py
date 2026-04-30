"""Test topology function module theorems."""

import math4py.topology.function as top


class TestOpenSet:
    def test_trivial_open(self):
        """空集合與全集是開集。"""
        topology = {"open_sets": {frozenset(), frozenset({1, 2, 3})}, "universal": {1, 2, 3}}
        assert top.is_open_set(set(), topology)
        assert top.is_open_set({1, 2, 3}, topology)

    def test_non_open(self):
        """{1} 不在開集族中。"""
        topology = {"open_sets": {frozenset(), frozenset({1, 2, 3})}, "universal": {1, 2, 3}}
        assert not top.is_open_set({1}, topology)


class TestClosedSet:
    def test_complement_open(self):
        """開集的補集是閉集。"""
        topology = {
            "open_sets": {frozenset(), frozenset({1, 2}), frozenset({1, 2, 3})},
            "universal": {1, 2, 3},
        }
        # {3} 的補集是 {1, 2}，是開集，所以 {3} 是閉集
        assert top.is_closed_set({3}, topology)


class TestConnected:
    def test_connected_space(self):
        """只有空集合與全集的空間是連通的。"""
        topology = {"open_sets": {frozenset(), frozenset({1, 2, 3})}, "universal": {1, 2, 3}}
        assert top.is_connected(topology)

    def test_disconnected_space(self):
        """有非平凡既開又閉的集合則不連通。"""
        topology = {
            "open_sets": {frozenset(), frozenset({1}), frozenset({2, 3}), frozenset({1, 2, 3})},
            "universal": {1, 2, 3},
        }
        # {1} 既開又閉
        assert not top.is_connected(topology)


class TestEulerCharacteristic:
    def test_tetrahedron(self):
        """四面體 V=4, E=6, F=4, χ=2。"""
        chi = top.euler_characteristic(4, 6, 4)
        assert chi == 2

    def test_cube(self):
        """立方體 V=8, E=12, F=6, χ=2。"""
        chi = top.euler_characteristic(8, 12, 6)
        assert chi == 2


class TestCompact:
    def test_finite_cover(self):
        """有限覆蓋的空間是緊緻的（簡化）。"""
        topology = {
            "open_sets": {frozenset(), frozenset({1}), frozenset({2}), frozenset({1, 2})},
            "universal": {1, 2},
        }
        covering = [frozenset({1}), frozenset({2})]
        assert top.is_compact(topology, covering)


class TestHausdorff:
    def test_distinct_points(self):
        """不同點距離 > 0 滿足豪斯多夫。"""
        points = [0.0, 1.0, 2.0]

        def dist_fn(x, y):
            return abs(x - y)

        assert top.is_hausdorff(points, dist_fn)


class TestClosure:
    def test_closure_with_limit(self):
        """集合的閉包 = 集合 ∪ 極限點。"""
        A = {1, 2}
        limit_pts = {3}
        result = top.closure(A, limit_pts)
        assert result == {1, 2, 3}


class TestInterior:
    def test_interior_subset(self):
        """內部是集合的最大開子集。"""
        A = {1, 2, 3}
        open_sets = [frozenset(), frozenset({1}), frozenset({1, 2})]
        result = top.interior(A, open_sets)
        assert result.issubset(A)


class TestBoundary:
    def test_boundary_empty_interior(self):
        """內部為空時，邊界 = 閉包。"""
        A = {1, 2}
        closure_A = {1, 2, 3}
        interior_A = set()
        result = top.boundary(A, closure_A, interior_A)
        assert result == {1, 2, 3}


class TestHomeomorphism:
    def test_identity_map(self):
        """恆等映射是同胚。"""

        def f(x):
            return x

        def f_inv(x):
            return x

        domain = [1, 2, 3]
        codomain = [1, 2, 3]
        assert top.homeomorphism_check(f, f_inv, domain, codomain)


class TestFundamentalGroup:
    def test_simply_connected(self):
        """單連通空間的基本群平凡。"""
        loops = [True, True, True]  # 所有迴路可收縮
        assert top.fundamental_group_trivial(loops)


class TestTopologicalSort:
    def test_dag_sort(self):
        """有向無環圖的拓撲排序。"""
        graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
        result = top.topological_sort(graph)
        # 檢查順序是否合法
        pos = {node: i for i, node in enumerate(result)}
        for node in graph:
            for neighbor in graph[node]:
                assert pos[node] < pos[neighbor]

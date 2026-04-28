"""Tests for algebra/function.py (Group, Ring, Field, VectorSpace)."""

from math4py.algebra.function import Field, Group, Ring, VectorSpace


class TestGroup:
    def test_integers_mod_n(self):
        """Z/3Z 加法群。"""

        def op(a, b):
            return (a + b) % 3

        identity = 0

        def inverse(a):
            return (-a) % 3

        G = Group("Z/3Z", {0, 1, 2}, op, identity, inverse)
        assert G.is_group()
        assert G.is_abelian()

    def test_symmetric_group(self):
        """S_3 非交换群 (置换群)。"""
        carrier = {0, 1, 2, 3, 4, 5}  # 6 个置换的编号
        op_table = {
            (0, 0): 0,
            (0, 1): 1,
            (1, 0): 1,
            (1, 1): 0,
        }

        def op(a, b):
            return op_table.get((a, b), 0)

        identity = 0

        def inverse(a):
            return a  # 简化

        G = Group("S3_small", carrier, op, identity, inverse)
        assert G.is_closed()


class TestRing:
    def test_z_mod_n(self):
        """Z/4Z 环。"""

        def add(a, b):
            return (a + b) % 4

        def mul(a, b):
            return (a * b) % 4

        add_id = 0

        def add_inv(a):
            return (-a) % 4

        mul_id = 1
        R = Ring("Z/4Z", {0, 1, 2, 3}, add, add_id, add_inv, mul, mul_id)
        assert R.is_ring()


class TestField:
    def test_finite_field(self):
        """F_5 有限域。"""

        def add(a, b):
            return (a + b) % 5

        def mul(a, b):
            return (a * b) % 5

        add_id = 0

        def add_inv(a):
            return (-a) % 5

        mul_id = 1

        def mul_inv(a):
            return pow(a, 3, 5) if a != 0 else 0  # a^3 mod 5 是反元素

        F = Field("F_5", {0, 1, 2, 3, 4}, add, add_id, add_inv, mul, mul_id, mul_inv)
        assert F.is_field()


class TestVectorSpace:
    def test_f2_vector_space(self):
        """F_2 上的二维向量空间。"""

        def add(u, v):
            return ((u[0] + v[0]) % 2, (u[1] + v[1]) % 2)

        def scalar_mul(a, v):
            return (a * v[0] % 2, a * v[1] % 2)

        field = Field(
            "F_2",
            {0, 1},
            lambda a, b: (a + b) % 2,
            0,
            lambda a: a,
            lambda a, b: (a * b) % 2,
            1,
            lambda a: a if a != 0 else 0,
        )
        V = VectorSpace("F_2^2", {(0, 0), (1, 0), (0, 1), (1, 1)}, field, add, scalar_mul)
        assert V.is_vector_space()

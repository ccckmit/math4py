r"""Galois theory theorem tests."""


class TestGaloisSolvability:
    def test_quadratic_solvable(self):
        from math4py.algebra.galois_theory import galois_theorem_solvable

        coeffs = [1, 0, -1]
        result = galois_theorem_solvable(coeffs)
        assert result["pass"]
        assert result["degree"] == 2

    def test_cubic_solvable(self):
        from math4py.algebra.galois_theory import galois_theorem_solvable

        coeffs = [1, 0, 0, 0]
        result = galois_theorem_solvable(coeffs)
        assert result["pass"]
        assert result["degree"] == 3

    def test_quartic_solvable(self):
        from math4py.algebra.galois_theory import galois_theorem_solvable

        coeffs = [1, 0, 0, 0, 0]
        result = galois_theorem_solvable(coeffs)
        assert result["pass"]
        assert result["degree"] == 4

    def test_quintic_not_solvable(self):
        from math4py.algebra.galois_theory import galois_theorem_solvable

        coeffs = [1, 0, 0, 0, 0, 0]
        result = galois_theorem_solvable(coeffs)
        assert not result["pass"]
        assert result["degree"] == 5


class TestSeparablePolynomial:
    def test_quadratic_separable(self):
        from math4py.algebra.galois_theory import separable_polynomial_theorem

        coeffs = [1, 0, -1]
        result = separable_polynomial_theorem(coeffs)
        assert result["pass"]


class TestDiscriminant:
    def test_quadratic_discriminant(self):
        from math4py.algebra.galois_theory import discriminant_quadratic_theorem

        a, b, c = 1, 0, -1
        result = discriminant_quadratic_theorem(a, b, c)
        assert result["pass"]
        assert result["discriminant"] == 4


class TestGroupOrders:
    def test_symmetric_group_order(self):
        from math4py.algebra.galois_theory import symmetric_group_order_theorem

        result = symmetric_group_order_theorem(3)
        assert result["pass"]
        assert result["order"] == 6

    def test_alternating_group_order(self):
        from math4py.algebra.galois_theory import alternating_group_order_theorem

        result = alternating_group_order_theorem(3)
        assert result["pass"]
        assert result["order"] == 3


class TestCyclicGroup:
    def test_cyclic_group_order(self):
        from math4py.algebra.galois_theory import cyclic_group_theorem

        result = cyclic_group_theorem(6, 3)
        assert result["divides"]


class TestFunctionAPI:
    def test_polynomial_degree(self):
        from math4py.algebra.galois_theory import polynomial_degree

        assert polynomial_degree([1, 2, 3]) == 2

    def test_discriminant_quadratic(self):
        from math4py.algebra.galois_theory import discriminant_quadratic

        assert discriminant_quadratic(1, 0, -1) == 4

    def test_galois_group_solvable(self):
        from math4py.algebra.galois_theory import galois_group_solvable

        assert galois_group_solvable([1, 0, 0, 0])

    def test_symetric_group_order(self):
        from math4py.algebra.galois_theory import symetric_group_order

        assert symetric_group_order(3) == 6

    def test_alternating_group_order(self):
        from math4py.algebra.galois_theory import alternating_group_order

        assert alternating_group_order(3) == 3

    def test_quadratic_formula(self):
        from math4py.algebra.galois_theory import quadratic_formula

        r1, r2 = quadratic_formula(1, 0, -1)
        assert r1 == complex(1, 0) or r1 == complex(-1, 0)

    def test_solvable_by_radicals(self):
        from math4py.algebra.galois_theory import solvable_by_radicals

        result = solvable_by_radicals([1, 0, 0, 0])
        assert result["solvable"]

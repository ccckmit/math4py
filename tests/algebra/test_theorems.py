"""Tests for algebra/theorem.py (complex number theorems)."""

from math4py.algebra.theorem import (
    complex_argument_properties,
    complex_modulus_properties,
    euler_formula,
    fundamental_theorem_of_algebra,
)


class TestComplexTheorems:
    def test_modulus_properties(self):
        assert complex_modulus_properties(complex(3, 4))

    def test_argument_properties(self):
        assert complex_argument_properties(complex(1, 1))

    def test_euler_formula(self):
        assert euler_formula()

    def test_fundamental_theorem_of_algebra(self):
        assert fundamental_theorem_of_algebra()

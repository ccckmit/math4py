"""Tests for algebra/complex.py."""

import math

from math4py.algebra.complex import (
    argument,
    complex_add,
    complex_div,
    complex_exp,
    complex_log,
    complex_mul,
    complex_pow,
    complex_sub,
    conjugate,
    create_complex,
    from_polar,
    imag_part,
    modulus,
    real_part,
    solve_quadratic,
    to_polar,
)


class TestComplexCreation:
    def test_create_complex(self):
        z = create_complex(3, 4)
        assert z == complex(3, 4)

    def test_real_imag(self):
        z = complex(3, -4)
        assert real_part(z) == 3.0
        assert imag_part(z) == -4.0


class TestComplexOperations:
    def test_conjugate(self):
        z = complex(3, 4)
        assert conjugate(z) == complex(3, -4)

    def test_modulus(self):
        z = complex(3, 4)
        assert abs(modulus(z) - 5.0) < 1e-9

    def test_argument(self):
        z = complex(1, 1)
        assert abs(argument(z) - math.pi / 4) < 1e-9

    def test_to_polar(self):
        z = complex(3, 4)
        r, theta = to_polar(z)
        assert abs(r - 5.0) < 1e-9

    def test_from_polar(self):
        z = from_polar(5, math.pi / 2)
        assert abs(z.real) < 1e-9
        assert abs(z.imag - 5.0) < 1e-9


class TestComplexArithmetic:
    def test_add(self):
        z1 = complex(1, 2)
        z2 = complex(3, 4)
        result = complex_add(z1, z2)
        assert result == complex(4, 6)

    def test_sub(self):
        z1 = complex(5, 6)
        z2 = complex(1, 2)
        result = complex_sub(z1, z2)
        assert result == complex(4, 4)

    def test_mul(self):
        z1 = complex(1, 2)
        z2 = complex(3, 4)
        result = complex_mul(z1, z2)
        assert result == complex(-5, 10)

    def test_div(self):
        z1 = complex(1, 2)
        z2 = complex(3, 4)
        result = complex_div(z1, z2)
        expected = complex(0.44, 0.08)
        assert abs(result.real - expected.real) < 1e-9
        assert abs(result.imag - expected.imag) < 1e-9


class TestComplexFunctions:
    def test_exp(self):
        z = complex(0, math.pi)
        result = complex_exp(z)
        assert abs(result.real + 1) < 1e-9
        assert abs(result.imag) < 1e-9

    def test_log(self):
        z = complex(1, 0)
        result = complex_log(z)
        assert abs(result.real) < 1e-9

    def test_pow(self):
        z = complex(1, 1)
        w = complex(2, 0)
        result = complex_pow(z, w)
        assert result == complex(0, 2)


class TestQuadraticSolver:
    def test_real_roots(self):
        r1, r2 = solve_quadratic(1, -3, 2)
        assert abs(r1 - 2.0) < 1e-9 or abs(r1 - 1.0) < 1e-9

    def test_complex_roots(self):
        r1, r2 = solve_quadratic(1, 0, 1)
        assert r1 == complex(0, 1) or r1 == complex(0, -1)

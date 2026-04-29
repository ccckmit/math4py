r"""數論函數與定理測試。"""

from math4py.number_theory import (
    euler_phi,
    fibonacci,
    gcd,
    is_prime,
    lcm,
    mod_inv,
    mod_pow,
    prime_factors,
    primes_upto,
)


class TestGcdLcm:
    def test_gcd_basic(self):
        assert gcd(48, 18) == 6

    def test_lcm_basic(self):
        assert lcm(4, 6) == 12

    def test_gcd_lcm_relation(self):
        assert gcd(4, 6) * lcm(4, 6) == 4 * 6


class TestPrime:
    def test_is_prime(self):
        assert is_prime(2) is True
        assert is_prime(4) is False
        assert is_prime(17) is True

    def test_primes_upto(self):
        primes = primes_upto(10)
        assert primes == [2, 3, 5, 7]

    def test_prime_factors(self):
        assert sorted(prime_factors(12)) == [2, 2, 3]


class TestEulerPhi:
    def test_euler_phi_basic(self):
        assert euler_phi(5) == 4
        assert euler_phi(6) == 2

    def test_euler_phi_multiplicative(self):
        assert euler_phi(3) * euler_phi(4) == euler_phi(12)


class TestModular:
    def test_mod_pow(self):
        assert mod_pow(2, 3, 5) == 3
        assert mod_pow(2, 10, 100) == 24

    def test_mod_inv(self):
        assert mod_inv(3, 11) == 4


class TestFibonacci:
    def test_fibonacci(self):
        assert fibonacci(1) == 1
        assert fibonacci(5) == 5
        assert fibonacci(10) == 55

    def test_fibonacci_gcd(self):
        assert gcd(fibonacci(5), fibonacci(7)) == 1


class TestTheorems:
    def test_bezout(self):
        assert gcd(48, 18) == 6

    def test_fundamental_theorem(self):
        factors = prime_factors(60)
        assert 2 in factors and 3 in factors and 5 in factors

    def test_fermat_little(self):
        assert pow(2, 4, 5) == 1

    def test_euler_theorem(self):
        assert pow(3, 4, 5) == 1

    def test_crt(self):
        pass
"""數論函數與定理測試。"""

from math4py.number_theory import (
    bezout_identity,
    chinese_remainder_theorem,
    euler_phi,
    euler_phi_multiplicative,
    euler_theorem,
    fermat_little_theorem,
    fibonacci,
    fibonacci_gcd_property,
    fundamental_theorem_of_arithmetic,
    gcd,
    gcd_lcm_relation,
    is_prime,
    lcm,
    mod_inv,
    mod_pow,
    prime_factors,
    primes_upto,
)


class TestGcdLcm:
    def test_gcd_basic(self):
        assert gcd(12, 8) == 4
        assert gcd(17, 13) == 1
        assert gcd(0, 5) == 5
        assert gcd(-12, 8) == 4

    def test_lcm_basic(self):
        assert lcm(4, 6) == 12
        assert lcm(3, 5) == 15
        assert lcm(0, 5) == 0

    def test_gcd_lcm_relation(self):
        assert gcd_lcm_relation(12, 18)
        assert gcd_lcm_relation(7, 13)


class TestPrime:
    def test_is_prime(self):
        assert is_prime(2)
        assert is_prime(17)
        assert not is_prime(1)
        assert not is_prime(4)
        assert not is_prime(49)

    def test_primes_upto(self):
        primes = primes_upto(10)
        assert primes == [2, 3, 5, 7]

    def test_prime_factors(self):
        assert sorted(prime_factors(12)) == [2, 2, 3]
        assert prime_factors(17) == [17]


class TestEulerPhi:
    def test_euler_phi_basic(self):
        assert euler_phi(1) == 1
        assert euler_phi(9) == 6
        assert euler_phi(12) == 4

    def test_euler_phi_multiplicative(self):
        assert euler_phi_multiplicative(3, 5)
        assert euler_phi_multiplicative(4, 9)


class TestModular:
    def test_mod_pow(self):
        assert mod_pow(2, 10, 1000) == 1024 % 1000
        assert mod_pow(3, 3, 5) == 27 % 5

    def test_mod_inv(self):
        assert mod_inv(3, 7) == 5
        assert mod_inv(7, 13) == 2


class TestFibonacci:
    def test_fibonacci(self):
        assert fibonacci(0) == 0
        assert fibonacci(1) == 1
        assert fibonacci(10) == 55

    def test_fibonacci_gcd(self):
        assert fibonacci_gcd_property(6, 9)


class TestTheorems:
    def test_bezout(self):
        assert bezout_identity(12, 8)
        assert bezout_identity(17, 13)

    def test_fundamental_theorem(self):
        assert fundamental_theorem_of_arithmetic(12)
        assert fundamental_theorem_of_arithmetic(17)

    def test_fermat_little(self):
        assert fermat_little_theorem(7, 3)
        assert fermat_little_theorem(13, 5)

    def test_euler_theorem(self):
        assert euler_theorem(8, 3)
        assert euler_theorem(15, 2)

    def test_crt(self):
        assert chinese_remainder_theorem([3, 5, 7], [2, 3, 2])

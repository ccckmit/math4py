"""number_theory - 數論模組。"""

from .function import (
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

__all__ = [
    "gcd",
    "lcm",
    "is_prime",
    "primes_upto",
    "prime_factors",
    "euler_phi",
    "mod_pow",
    "mod_inv",
    "fibonacci",
]

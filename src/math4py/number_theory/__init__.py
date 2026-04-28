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
from .theorem import (
    bezout_identity,
    chinese_remainder_theorem,
    euler_phi_multiplicative,
    euler_theorem,
    fermat_little_theorem,
    fibonacci_gcd_property,
    fundamental_theorem_of_arithmetic,
    gcd_lcm_relation,
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
    "bezout_identity",
    "fundamental_theorem_of_arithmetic",
    "euler_phi_multiplicative",
    "fermat_little_theorem",
    "euler_theorem",
    "chinese_remainder_theorem",
    "gcd_lcm_relation",
    "fibonacci_gcd_property",
]

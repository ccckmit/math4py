"""數論定理與公理驗證。

以 pytest 測試形式驗證數論中的定義、公理與定理。
"""

from typing import List

from .function import (
    euler_phi,
    fibonacci,
    gcd,
    is_prime,
    lcm,
    mod_inv,
    mod_pow,
    prime_factors,
)


def bezout_identity(a: int, b: int) -> bool:
    """貝祖等式：存在整數 x, y 使 ax + by = gcd(a, b)。"""
    g = gcd(a, b)
    _, x, y = _extended_gcd(a, b)
    return a * x + b * y == g


def _extended_gcd(a: int, b: int):
    if b == 0:
        return abs(a), 1 if a > 0 else -1, 0
    g, x1, y1 = _extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1


def fundamental_theorem_of_arithmetic(n: int) -> bool:
    """算術基本定理：每個 >1 的整數可唯一分解為質數乘積 (忽略順序)。"""
    if n < 2:
        return True
    factors = prime_factors(n)
    product = 1
    for p in factors:
        if not is_prime(p):
            return False
        product *= p
    return product == n


def euler_phi_multiplicative(m: int, n: int) -> bool:
    """歐拉 φ 函數是積性函數：若 gcd(m, n)=1，則 φ(mn) = φ(m)φ(n)。"""
    if gcd(m, n) != 1:
        return True
    return euler_phi(m * n) == euler_phi(m) * euler_phi(n)


def fermat_little_theorem(p: int, a: int) -> bool:
    """費馬小定理：若 p 為質數且 gcd(a, p)=1，則 a^(p-1) ≡ 1 (mod p)。"""
    if not is_prime(p) or gcd(a, p) != 1:
        return True
    return mod_pow(a, p - 1, p) == 1


def euler_theorem(n: int, a: int) -> bool:
    """歐拉定理：若 gcd(a, n)=1，則 a^φ(n) ≡ 1 (mod n)。"""
    if gcd(a, n) != 1:
        return True
    return mod_pow(a, euler_phi(n), n) == 1


def chinese_remainder_theorem(m: List[int], a: List[int]) -> bool:
    """中國剩餘定理：若模數兩兩互質，則同餘方程組有解。
    此函數驗證：若解存在，則代入後皆成立。"""
    if len(m) != len(a) or len(m) < 2:
        return True
    for i in range(len(m)):
        for j in range(i + 1, len(m)):
            if gcd(m[i], m[j]) != 1:
                return True
    M = 1
    for mi in m:
        M *= mi
    x = 0
    for ai, mi in zip(a, m):
        Mi = M // mi
        inv = mod_inv(Mi, mi)
        x += ai * Mi * inv
    x %= M
    return all(x % mi == ai % mi for mi, ai in zip(m, a))


def gcd_lcm_relation(a: int, b: int) -> bool:
    """gcd(a, b) * lcm(a, b) = |ab|。"""
    if a == 0 or b == 0:
        return lcm(a, b) == 0
    return gcd(a, b) * lcm(a, b) == abs(a * b)


def fibonacci_gcd_property(m: int, n: int) -> bool:
    """gcd(F(m), F(n)) = F(gcd(m, n))，其中 F 為費波那契數。"""
    return gcd(fibonacci(m), fibonacci(n)) == fibonacci(gcd(m, n))


__all__ = [
    "bezout_identity",
    "fundamental_theorem_of_arithmetic",
    "euler_phi_multiplicative",
    "fermat_little_theorem",
    "euler_theorem",
    "chinese_remainder_theorem",
    "gcd_lcm_relation",
    "fibonacci_gcd_property",
]

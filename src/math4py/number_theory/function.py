"""數論函數：質數、最大公因數、最小公倍數、模運算等。"""

import math


def gcd(a: int, b: int) -> int:
    """最大公因數 ( Euclidean algorithm )。"""
    while b:
        a, b = b, a % b
    return abs(a)


def lcm(a: int, b: int) -> int:
    """最小公倍數。"""
    return abs(a * b) // gcd(a, b) if a and b else 0


def is_prime(n: int) -> bool:
    """判斷是否為質數。"""
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.isqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def primes_upto(n: int) -> list:
    """埃拉托斯特尼篩法，回傳 <= n 的所有質數。"""
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for p in range(2, int(math.isqrt(n)) + 1):
        if sieve[p]:
            for multiple in range(p * p, n + 1, p):
                sieve[multiple] = False
    return [i for i, is_p in enumerate(sieve) if is_p]


def prime_factors(n: int) -> list:
    """質因數分解，回傳質因數列表 (含重複)。"""
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        factors.append(n)
    return factors


def euler_phi(n: int) -> int:
    """歐拉 φ 函數：小於 n 且與 n 互質的正整數個數。"""
    if n < 1:
        return 0
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1 if p == 2 else 2
    if n > 1:
        result -= result // n
    return result


def mod_pow(a: int, b: int, m: int) -> int:
    """模冪運算：a^b mod m (binary exponentiation)。"""
    result = 1
    a %= m
    while b > 0:
        if b & 1:
            result = (result * a) % m
        a = (a * a) % m
        b >>= 1
    return result


def mod_inv(a: int, m: int) -> int:
    """模反元素：找 x 使 a*x ≡ 1 (mod m)，不存在時拋出 ValueError。"""
    g, x, _ = _extended_gcd(a, m)
    if g != 1:
        raise ValueError(f"No modular inverse for {a} mod {m}")
    return x % m


def _extended_gcd(a: int, b: int):
    """擴展歐幾里得算法，回傳 (gcd, x, y) 使 ax + by = gcd。"""
    if b == 0:
        return abs(a), 1 if a > 0 else -1, 0
    g, x1, y1 = _extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1


def fibonacci(n: int) -> int:
    """第 n 個費波那契數 (0-indexed: F(0)=0, F(1)=1)。"""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n < 2:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


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

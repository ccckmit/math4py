# number_theory/function.md

## 概述

數論函數模組，實現質數判斷、最大公因數、模運算、費波那契數等基礎數論工具。

## 數學原理

### 歐幾里得算法 (Euclidean Algorithm)
求最大公因數的核心算法，基於遞迴關係：
$$\gcd(a, b) = \gcd(b, a \bmod b)$$

### 質數判定
- 試除法：若 n > 3 不是質數，則必有因數 ≤ √n
- 只需檢查奇數，因為偶數早在前面被排除

### 埃拉托斯特尼篩法 (Sieve of Eratosthenes)
找出範圍內所有質數：標記每個質數的倍數為合數。

### 歐拉 φ 函數
$$\phi(n) = n \prod_{p|n}\left(1 - \frac{1}{p}\right)$$
歐拉 phi 函數計算小於 n 且與 n 互質的正整數個數。

### 模冪運算 (Binary Exponentiation)
$$a^b \bmod m$$ 
使用二分冪算法，將指數 b 視為二進位，每次將底數平方。

### 擴展歐幾里得算法
求 x, y 使 `ax + by = gcd(a, b)`，用於計算模反元素。

## 實作細節

| 函數 | 說明 |
|------|------|
| `gcd(a, b)` | 歐幾里得算法求最大公因數 |
| `lcm(a, b)` | 最小公倍數：\|ab\|/gcd(a,b) |
| `is_prime(n)` | O(√n) 試除法判斷質數 |
| `primes_upto(n)` | 埃拉托斯特尼篩法 O(n log log n) |
| `prime_factors(n)` | 質因數分解，返回質因數列表 |
| `euler_phi(n)` | 歐拉 φ 函數（積性函數） |
| `mod_pow(a, b, m)` | 快速模冪 O(log b) |
| `mod_inv(a, m)` | 模反元素（需 gcd(a,m)=1） |
| `fibonacci(n)` | 費波那契數（迭代版） |

## 使用方式

```python
from math4py.number_theory import gcd, is_prime, euler_phi

gcd(48, 18)          # 6
is_prime(17)         # True
euler_phi(12)        # 4
mod_pow(2, 10, 1000) # 24
```
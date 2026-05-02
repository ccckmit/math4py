# test_number_theory.py

## 概述 (Overview)

測試數論函數與定理，包含質數、GCD/LCM、費馬小定理、歐拉定理等。

## 測試內容 (Test Coverage)

### TestGcdLcm
- `test_gcd_basic`: 最大公因數 gcd(48,18) = 6
- `test_lcm_basic`: 最小公倍數 lcm(4,6) = 12
- `test_gcd_lcm_relation`: gcd(a,b) × lcm(a,b) = a × b

### TestPrime
- `test_is_prime`: 質數判定 is_prime(2)=True, is_prime(4)=False
- `test_primes_upto`: 質數列舉 primes_upto(10) = [2,3,5,7]
- `test_prime_factors`: 質因數分解 prime_factors(12) = [2,2,3]

### TestEulerPhi
- `test_euler_phi_basic`: 歐拉函數 φ(5)=4, φ(6)=2
- `test_euler_phi_multiplicative`: 乘法性 φ(mn) = φ(m)φ(n)（互質）

### TestModular
- `test_mod_pow`: 模指數運算 mod_pow(2,3,5) = 3
- `test_mod_inv`: 模反元素 mod_inv(3,11) = 4（因為 3×4 ≡ 1 mod 11）

### TestFibonacci
- `test_fibonacci`: 費波那契數列 fib(1)=1, fib(5)=5, fib(10)=55
- `test_fibonacci_gcd`: 費波那契數互質 gcd(F_m, F_n) = F_{gcd(m,n)}

### TestTheorems
- `test_bezout`: 貝茲定理（擴展歐幾里得算法）
- `test_fundamental_theorem`: 算術基本定理（質因數分解唯一性）
- `test_fermat_little`: 費馬小定理 a^{p-1} ≡ 1 mod p（p 為質數）
- `test_euler_theorem`: 歐拉定理 a^{φ(n)} ≡ 1 mod n（gcd(a,n)=1）
- `test_crt`: 中國剩餘定理

## 測試原理 (Testing Principles)

- **整除性**: 質數、合數、因數分解
- **歐幾里得算法**: 計算最大公因數的標準方法
- **模運算**: 同餘關係與密碼學基礎
- **費馬小定理**: 質數判定與 RSA 加密核心
- **歐拉函數**: 計數與正整數互質的整數數量
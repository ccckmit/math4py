# 概述

級數（Series）函數模組，提供泰勒級數、傅里葉級數、冪級數以及各種級數收斂性檢驗函數。

# 數學原理

## 泰勒級數 (Taylor Series)
$$f(x) = \sum_{k=0}^{\infty} \frac{f^{(k)}(a)}{k!}(x-a)^k$$

## 傅里葉級數 (Fourier Series)
週期為 $T = b-a$ 的函數可展開為：
$$f(x) \approx \frac{a_0}{2} + \sum_{n=1}^{\infty} \left( a_n \cos(n\omega x) + b_n \sin(n\omega x) \right)$$

其中 $\omega = \frac{2\pi}{T}$，係數為：
$$a_n = \frac{2}{T} \int_a^b f(x) \cos(n\omega x) dx$$
$$b_n = \frac{2}{T} \int_a^b f(x) \sin(n\omega x) dx$$

## 幾何級數 (Geometric Series)
$$S = a + ar + ar^2 + \cdots + ar^n = \begin{cases} a\frac{1-r^{n+1}}{1-r} & n \text{ 有限} \\ \frac{a}{1-r} & n \to \infty, |r| < 1 \end{cases}$$

## 調和級數 (Harmonic Series)
$$H_n = 1 + \frac{1}{2} + \frac{1}{3} + \cdots + \frac{1}{n}$$

交錯調和級數：
$$\sum_{k=1}^{\infty} \frac{(-1)^{k+1}}{k} = \ln(2)$$

## 收斂性檢驗

### 比值檢驗 (Ratio Test)
$$L = \lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right|$$
- $L < 1$: 收斂
- $L > 1$: 發散
- $L = 1$: 無法判定

### 根值檢驗 (Root Test)
$$L = \lim_{n \to \infty} \sqrt[n]{|a_n|}$$
- $L < 1$: 收斂
- $L > 1$: 發散
- $L = 1$: 無法判定

### 積分檢驗 (Integral Test)
若 $f(x) \geq 0$ 且遞減，則 $\sum_{n=1}^{\infty} f(n)$ 與 $\int_1^{\infty} f(x) dx$ 同時收斂或發散。

# 實作細節

## 傅里葉級數計算
```python
def fourier_series(f, a, b, n=10):
    T = b - a
    omega = 2 * np.pi / T
    x = np.linspace(a, b, 1000)
    y = f(x)
    a0 = (2.0 / T) * np.trapezoid(y, x)
    for k in range(1, n + 1):
        a_n.append((2.0 / T) * np.trapezoid(y * np.cos(k * omega * x), x))
        b_n.append((2.0 / T) * np.trapezoid(y * np.sin(k * omega * x), x))
    return a0, a_n, b_n
```

## 幾何級數
```python
def geometric_series(a, r, n=None):
    if n is None:
        if abs(r) >= 1:
            return float("inf")
        return a / (1.0 - r)
    return a * (1.0 - r**(n + 1)) / (1.0 - r)
```

## 比值檢驗
```python
def ratio_test(terms):
    ratios = [abs(terms[i + 1] / terms[i]) for i in range(len(terms) - 1) if terms[i] != 0]
    L = ratios[-1]
    if L < 1: return "convergent", L
    elif L > 1: return "divergent", L
    else: return "inconclusive", L
```

# 使用方式

```python
from math4py.calculus.series import fourier_series, geometric_series, ratio_test

# 傅里葉級數
f = lambda x: x
a0, a_n, b_n = fourier_series(f, 0, 2*np.pi, n=10)

# 幾何級數
sum_geo = geometric_series(1, 0.5, n=10)  # 有限項和
sum_inf = geometric_series(1, 0.5)         # 無窮級數

# 收斂性檢驗
terms = [1/n for n in range(1, 100)]
result, L = ratio_test(terms)  # "convergent"
```
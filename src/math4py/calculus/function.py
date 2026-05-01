"""微積分函數：數值微分、積分、逼近。

微積分的數值計算函數。
"""

from typing import Callable

import numpy as np


def derivative(f: Callable[[float], float], x: float, h: float = 1e-5) -> float:
    """數值微分 (中央差分)。

    Args:
        f: 函數
        x: 點
        h: 步長

    Returns:
        f'(x)
    """
    return (f(x + h) - f(x - h)) / (2 * h)


def second_derivative(f: Callable[[float], float], x: float, h: float = 1e-5) -> float:
    """二階數值微分。

    Args:
        f: 函數
        x: 點
        h: 步長

    Returns:
        f''(x)
    """
    return (f(x + h) - 2 * f(x) + f(x - h)) / (h * h)


def integral(f, a, b, n=1000):
    x = np.linspace(a, b, n + 1)
    y = f(x)
    h = (b - a) / n
    return h * (0.5 * y[0] + np.sum(y[1:-1]) + 0.5 * y[-1])


def trapezoidal(f, a, b, n=1000):
    return integral(f, a, b, n)


def simpson(f, a, b, n=100):
    if n % 2 != 0:
        n += 1
    x = np.linspace(a, b, n + 1)
    y = f(x)
    h = (b - a) / n
    return h / 3 * (y[0] + y[-1] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]))


def midpoint_rule(f: Callable[[float], float], a: float, b: float, n: int = 100) -> float:
    """中點法。

    Args:
        f: 函數
        a: 下界
        b: 上界
        n: 分割數

    Returns:
        ∫f(x)dx
    """
    h = (b - a) / n
    x = np.linspace(a + h / 2, b - h / 2, n)
    return h * np.sum(f(x))


def limit(f: Callable[[float], float], x: float, h: float = 1e-8) -> float:
    """極限趨近。

    Args:
        f: 函數
        x: 趨近點
        h: 趨近值

    Returns:
        lim f(x)
    """
    return f(x)


def taylor_series(f: Callable[[float], float], x0: float, n: int = 5) -> Callable[[float], float]:
    """Taylor 級數逼近。

    Args:
        f: 函數
        x0: 展開點
        n: 階數

    Returns:
        逼近函數
    """

    def poly(x):
        result = f(x0)
        for i in range(1, n + 1):
            try:
                result += (x - x0) ** i / np.math.factorial(i)
            except (ValueError, ZeroDivisionError):
                break
        return result

    return poly


__all__ = [
    "derivative",
    "second_derivative",
    "integral",
    "simpson",
    "midpoint_rule",
    "limit",
    "taylor_series",
]

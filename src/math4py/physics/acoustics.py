"""聲學（Acoustics）基礎函數。"""

import numpy as np

# 物理常數
SPEED_OF_SOUND = 343.0  # m/s (空氣中，20°C)
P0 = 101325.0  # 標準大氣壓 (Pa)


def sound_speed(gamma: float = 1.4, M: float = 0.02897, T: float = 293.15) -> float:
    """聲速 c = sqrt(γRT/M)。"""
    R = 8.314462618
    return np.sqrt(gamma * R * T / M)


def doppler_shift(
    f0: float, v_observer: float, v_source: float, c: float = SPEED_OF_SOUND
) -> float:
    """多普勒效應 f' = f0 * (c + v_o) / (c - v_s)。"""
    if c - v_source == 0:
        return float("inf")
    return f0 * (c + v_observer) / (c - v_source)


def sound_intensity(P: float, rho: float = 1.204, c: float = SPEED_OF_SOUND) -> float:
    """聲強 I = P² / (ρc)。"""
    if rho * c == 0:
        return 0.0
    return P**2 / (rho * c)


def decibel_level(I: float, I0: float = 1e-12) -> float:
    """分貝等級 L = 10 * log10(I/I0)。"""
    if I <= 0 or I0 <= 0:
        return float("-inf")
    return 10.0 * np.log10(I / I0)


def sound_wavelength(f: float, c: float = SPEED_OF_SOUND) -> float:
    """波長 λ = c/f。"""
    if f == 0:
        return float("inf")
    return c / f


def resonant_frequency(L: float, n: int = 1, c: float = SPEED_OF_SOUND) -> float:
    """開管共振頻率 f = n*c/(2L)。"""
    return n * c / (2.0 * L)


def beat_frequency(f1: float, f2: float) -> float:
    """拍頻 f_beat = |f1 - f2|。"""
    return abs(f1 - f2)


def sound_pressure_level(p: float, p0: float = 20e-6) -> float:
    """聲壓等級 Lp = 20 * log10(p/p0) dB。"""
    if p <= 0 or p0 <= 0:
        return float("-inf")
    return 20.0 * np.log10(p / p0)


__all__ = [
    "sound_speed",
    "doppler_shift",
    "sound_intensity",
    "decibel_level",
    "sound_wavelength",
    "resonant_frequency",
    "beat_frequency",
    "sound_pressure_level",
]

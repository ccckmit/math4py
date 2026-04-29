"""傅立葉轉換與頻譜分析。"""

from typing import Tuple
import numpy as np
import numpy.fft as fft


def fourier_transform(signal: np.ndarray, dt: float = 1.0) -> Tuple[np.ndarray, np.ndarray]:
    """傅立葉轉換（數值）。

    Args:
        signal: 時域信號
        dt: 取樣間隔

    Returns:
        (frequencies, spectrum)
    """
    n = len(signal)
    freqs = fft.fftfreq(n, d=dt)
    spectrum = fft.fft(signal) * dt
    return freqs, spectrum


def inverse_fourier_transform(spectrum: np.ndarray, dt: float = 1.0) -> Tuple[np.ndarray, np.ndarray]:
    """逆傅立葉轉換。

    Args:
        spectrum: 頻域信號
        dt: 取樣間隔

    Returns:
        (times, signal)
    """
    n = len(spectrum)
    t = np.arange(n) * dt
    signal = fft.ifft(spectrum) / dt
    return t, signal


def power_spectrum(signal: np.ndarray, dt: float = 1.0) -> Tuple[np.ndarray, np.ndarray]:
    """功率譜 |X(f)|²。

    Args:
        signal: 時域信號
        dt: 取樣間隔

    Returns:
        (frequencies, power)
    """
    freqs, spectrum = fourier_transform(signal, dt)
    power = np.abs(spectrum) ** 2
    return freqs, power


def fourier_series_coeff(f: callable, T: float, n_terms: int = 10) -> np.ndarray:
    """傅立葉級數系數 a_n, b_n。

    Args:
        f: 週期函數 f(t)
        T: 週期
        n_terms: 項數

    Returns:
        (a0, an_array, bn_array)
    """
    t = np.linspace(0, T, 1000, endpoint=False)
    y = f(t)
    if np.ndim(y) == 0:  # 标量輸出，轉為陣列
        y = np.full_like(t, y)
    dt = T / 1000
    a0 = 2.0 / T * np.sum(y) * dt

    an = np.zeros(n_terms)
    bn = np.zeros(n_terms)
    for n in range(1, n_terms + 1):
        an[n-1] = 2.0 / T * np.sum(y * np.cos(2 * np.pi * n * t / T)) * dt
        bn[n-1] = 2.0 / T * np.sum(y * np.sin(2 * np.pi * n * t / T)) * dt

    return a0, an, bn


def reconstruct_fourier_series(a0: float, an: np.ndarray, bn: np.ndarray, T: float, t: np.ndarray) -> np.ndarray:
    """用傅立葉系數重構信號。

    Args:
        a0: 直流分量
        an, bn: 系數數組
        T: 週期
        t: 時間點

    Returns:
        重構信號
    """
    signal = np.ones_like(t) * a0 / 2.0
    n_terms = len(an)
    for n in range(1, n_terms + 1):
        signal += an[n-1] * np.cos(2 * np.pi * n * t / T)
        signal += bn[n-1] * np.sin(2 * np.pi * n * t / T)
    return signal


def dft(x: np.ndarray) -> np.ndarray:
    """離散傅立葉轉換（直接計算，用於教學）。

    Args:
        x: 輸入信號

    Returns:
        DFT 結果
    """
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)


def idft(X: np.ndarray) -> np.ndarray:
    """逆離散傅立葉轉換。"""
    N = len(X)
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(2j * np.pi * k * n / N)
    return np.dot(M, X) / N


def convolution_fft(x: np.ndarray, h: np.ndarray) -> np.ndarray:
    """用 FFT 計算摺積 x * h。

    Args:
        x: 信號1
        h: 信號2

    Returns:
        摺積結果
    """
    n = len(x) + len(h) - 1
    X = fft.fft(x, n)
    H = fft.fft(h, n)
    return np.real(fft.ifft(X * H))


def windowed_ft(signal: np.ndarray, window: str = "hann", dt: float = 1.0) -> Tuple[np.ndarray, np.ndarray]:
    """加窗傅立葉轉換。

    Args:
        signal: 信號
        window: "hann", "hamming", "rectangular"
        dt: 取樣間隔

    Returns:
        (frequencies, spectrum)
    """
    n = len(signal)
    print(f"DEBUG: window parameter = {repr(window)}")
    if window == "hanning":
        w = np.hanning(n)
        print(f"DEBUG: Using hanning, w.mean = {w.mean()}")
    elif window == "hamming":
        w = np.hamming(n)
    else:
        w = np.ones(n)

    windowed_signal = signal * w
    print(f"DEBUG: windowed_signal sum = {np.sum(windowed_signal)}")
    return fourier_transform(windowed_signal, dt)


__all__ = [
    "fourier_transform",
    "inverse_fourier_transform",
    "power_spectrum",
    "fourier_series_coeff",
    "reconstruct_fourier_series",
    "dft",
    "idft",
    "convolution_fft",
    "windowed_ft",
]

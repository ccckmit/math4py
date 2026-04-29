"""小波轉換。"""

from typing import Tuple, List
import numpy as np


def haar_wavelet(t: np.ndarray) -> np.ndarray:
    """Haar 小波母函數 ψ(t)。

    ψ(t) = 1  if 0 ≤ t < 0.5
             -1 if 0.5 ≤ t < 1
             0  otherwise
    """
    psi = np.zeros_like(t)
    mask1 = (t >= 0.0) & (t < 0.5)
    mask2 = (t >= 0.5) & (t < 1.0)
    psi[mask1] = 1.0
    psi[mask2] = -1.0
    return psi


def daubechies4_coefficients() -> np.ndarray:
    """Daubechies-4 (db4) 小波濾波器系數。"""
    c = np.array([
        0.4829629131445341,
        0.8365163037378077,
        0.2241438680418574,
        -0.1294095225512603,
        -0.8373651210868268,
        0.4830025253896963,
        0.2241438680418574,
        -0.1294095225512603,
    ])
    return c[:4]  # 簡化取前4個


def dwt(signal: np.ndarray, wavelet: str = "haar") -> Tuple[np.ndarray, np.ndarray]:
    """離散小波轉換 (DWT) - 單層。

    Args:
        signal: 輸入信號
        wavelet: "haar" 或其他

    Returns:
        (approximation, detail)
    """
    n = len(signal)
    half = n // 2
    approx = np.zeros(half)
    detail = np.zeros(half)

    for i in range(half):
        approx[i] = (signal[2*i] + signal[2*i+1]) / np.sqrt(2)
        detail[i] = (signal[2*i] - signal[2*i+1]) / np.sqrt(2)

    return approx, detail


def idwt(approx: np.ndarray, detail: np.ndarray, wavelet: str = "haar") -> np.ndarray:
    """逆離散小波轉換。"""
    n = len(approx) * 2
    signal = np.zeros(n)
    for i in range(len(approx)):
        signal[2*i] = (approx[i] + detail[i]) / np.sqrt(2)
        signal[2*i+1] = (approx[i] - detail[i]) / np.sqrt(2)
    return signal


def multilevel_dwt(signal: np.ndarray, levels: int = 3, wavelet: str = "haar") -> List[np.ndarray]:
    """多層 DWT。

    Returns:
        列表 [cA_n, cD_n, cD_{n-1}, ..., cD_1]
    """
    coeffs = []
    current = signal.copy()
    for level in range(levels):
        if len(current) < 2:
            break
        approx, detail = dwt(current, wavelet)
        coeffs.append(detail)
        current = approx
    coeffs.append(current)
    coeffs.reverse()
    return coeffs


def wavelet_denoise(signal: np.ndarray, threshold: float, wavelet: str = "haar") -> np.ndarray:
    """小波閾值去雜訊。

    Args:
        signal: 含雜訊信號
        threshold: 閾值
        wavelet: 小波類型

    Returns:
        去雜訊後信號
    """
    coeffs = multilevel_dwt(signal, levels=3, wavelet=wavelet)
    denoised_coeffs = []
    for c in coeffs:
        denoised_c = c.copy()
        denoised_c[np.abs(c) < threshold] = 0.0
        denoised_coeffs.append(denoised_c)

    reconstructed = denoised_coeffs[0]
    for detail in denoised_coeffs[1:]:
        reconstructed = idwt(reconstructed, detail, wavelet)

    return reconstructed


def continuous_wavelet_transform(signal: np.ndarray, scales: np.ndarray, wavelet: callable) -> np.ndarray:
    """連續小波轉換 (CWT)。

    Args:
        signal: 輸入信號
        scales: 尺度陣列
        wavelet: 小波函數 ψ(t)

    Returns:
        CWT 系數矩陣 (n_scales x n_samples)
    """
    n_samples = len(signal)
    n_scales = len(scales)
    cwt_matrix = np.zeros((n_scales, n_samples))

    t = np.linspace(0, 1, n_samples)

    for i, scale in enumerate(scales):
        for j in range(n_samples):
            psi_scaled = wavelet((t - t[j]) / scale) / np.sqrt(scale)
            cwt_matrix[i, j] = np.trapezoid(signal * psi_scaled, t)

    return cwt_matrix


__all__ = [
    "haar_wavelet",
    "daubechies4_coefficients",
    "dwt",
    "idwt",
    "multilevel_dwt",
    "wavelet_denoise",
    "continuous_wavelet_transform",
]

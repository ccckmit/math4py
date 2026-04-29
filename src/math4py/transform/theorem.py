"""Transform 定理驗證。"""

import numpy as np
from math4py.transform.fourier import fourier_transform, dft, idft, fourier_series_coeff, reconstruct_fourier_series
from math4py.transform.wavelet import dwt, idwt, multilevel_dwt, wavelet_denoise, haar_wavelet
from math4py.transform.laplace import laplace_transform, laplace_transform_pairs, solve_ode_laplace


def fourier_inversion_theorem(signal: np.ndarray, dt: float = 0.01) -> float:
    """傅立葉逆轉換定理：F⁻¹(F(f)) = f。

    Returns:
        重建誤差
    """
    freqs, spectrum = fourier_transform(signal, dt)
    t_recon, signal_recon = idft(spectrum, dt)
    return np.max(np.abs(signal - signal_recon[:len(signal)]))


def dft_idft_theorem(x: np.ndarray) -> float:
    """DFT-IFFT 定理：IDFT(DFT(x)) = x。

    Returns:
        重建誤差
    """
    X = dft(x)
    x_recon = idft(X)
    return np.max(np.abs(x - x_recon))


def fourier_series_convergence(f: callable, T: float, n_terms: int = 20) -> float:
    """傅立葉級數收斂性：項數越多，誤差越小。

    Returns:
        使用 n_terms 項時的最大誤差
    """
    t = np.linspace(0, T, 200, endpoint=False)
    a0, an, bn = fourier_series_coeff(f, T, n_terms)
    f_recon = reconstruct_fourier_series(a0, an, bn, T, t)
    return np.max(np.abs(f(t) - f_recon))


def convolution_theorem_fourier(x: np.ndarray, h: np.ndarray, dt: float = 0.01) -> float:
    """摺積定理：F{f * g} = F{f} · F{g}。

    Returns:
        頻域乘積與摺積 FFT 的差異
    """
    from math4py.transform.fourier import convolution_fft
    conv_result = convolution_fft(x, h)
    
    freqs_x, X = fourier_transform(x, dt)
    freqs_h, H = fourier_transform(h, dt)
    product = X * H
    _, conv_fft = inverse_fourier_transform(product, dt)
    
    min_len = min(len(conv_result), len(conv_fft))
    return np.max(np.abs(conv_result[:min_len] - conv_fft[:min_len]))


def wavelet_reconstruction_theorem(signal: np.ndarray) -> float:
    """小波重建定理：IDWT(DWT(x)) = x。

    Returns:
        重建誤差
    """
    approx, detail = dwt(signal)
    signal_recon = idwt(approx, detail)
    return np.max(np.abs(signal[:len(signal_recon)] - signal_recon))


def multilevel_reconstruction(signal: np.ndarray, levels: int = 3) -> float:
    """多層小波重建。

    Returns:
        重建誤差
    """
    coeffs = multilevel_dwt(signal, levels)
    reconstructed = coeffs[0]
    for detail in coeffs[1:]:
        reconstructed = idwt(reconstructed, detail)
    return np.max(np.abs(signal[:len(reconstructed)] - reconstructed))


def wavelet_denoising_effect(signal: np.ndarray, noise_level: float = 0.3) -> float:
    """小波去雜訊應該減少雜訊。

    Returns:
        去雜訊後的雜訊標準差減少量
    """
    noise = np.random.normal(0, noise_level, len(signal))
    noisy_signal = signal + noise
    denoised = wavelet_denoise(noisy_signal, threshold=0.5)
    original_noise_std = np.std(noise)
    remaining_noise_std = np.std(noisy_signal - denoised)
    return original_noise_std - remaining_noise_std


def laplace_transform_pairs_verification(s: complex, t_max: float = 10.0) -> dict:
    """驗證拉普拉斯轉換對。

    Returns:
        字典 {名稱: 誤差}
    """
    pairs = laplace_transform_pairs()
    errors = {}
    for name, (f, F_expected) in pairs.items():
        F_actual = laplace_transform(f, s, t_max)
        errors[name] = abs(F_actual - F_expected(s))
    return errors


def laplace_derivative_theorem(f: callable, s: complex, f0: float, t_max: float = 10.0) -> complex:
    """導數定理：L{f'}(s) = sL{f}(s) - f(0)。

    Returns:
        定理殘差應接近 0
    """
    from math4py.transform.laplace import laplace_derivative_property
    return laplace_derivative_property(f, s, f0, t_max)


def laplace_ode_solution(a: float, b: float, y0: float, t_points: np.ndarray) -> float:
    """用拉普拉斯轉換解 ODE 的誤差。

    Returns:
        最大誤差
    """
    y_solution = solve_ode_laplace(a, b, y0)
    y_expected = y_solution(t_points)
    
    def ode_rhs(t):
        return -a * y_expected + b
    
    y_actual = np.zeros_like(t_points)
    y_actual[0] = y0
    dt = t_points[1] - t_points[0]
    for i in range(1, len(t_points)):
        y_actual[i] = y_actual[i-1] + dt * ode_rhs(t_points[i-1])
    
    return np.max(np.abs(y_expected - y_actual))


__all__ = [
    "fourier_inversion_theorem",
    "dft_idft_theorem",
    "fourier_series_convergence",
    "convolution_theorem_fourier",
    "wavelet_reconstruction_theorem",
    "multilevel_reconstruction",
    "wavelet_denoising_effect",
    "laplace_transform_pairs_verification",
    "laplace_derivative_theorem",
    "laplace_ode_solution",
]

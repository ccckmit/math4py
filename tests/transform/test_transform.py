"""Transform 函數測試。"""

import numpy as np
import pytest
from math4py.transform.fourier import (
    fourier_transform, inverse_fourier_transform, power_spectrum,
    fourier_series_coeff, reconstruct_fourier_series, dft, idft, convolution_fft, windowed_ft,
)
from math4py.transform.wavelet import (
    haar_wavelet, dwt, idwt, multilevel_dwt, wavelet_denoise,
)
from math4py.transform.laplace import (
    laplace_transform, inverse_laplace_bromwich, laplace_transform_pairs,
    solve_ode_laplace,
)


class TestFourierTransform:
    def test_sine_wave(self):
        """sin(2πt) 的頻譜應在 f=±1 處有峰值。"""
        t = np.linspace(0, 1, 1000, endpoint=False)
        signal = np.sin(2 * np.pi * t)
        freqs, spectrum = fourier_transform(signal, dt=1.0/1000)
        idx = np.argmax(np.abs(spectrum))
        assert abs(abs(freqs[idx]) - 1.0) < 0.1

    def test_inverse_transform(self):
        """F⁻¹(F(f)) ≈ f"""
        signal = np.random.randn(128)
        freqs, spectrum = fourier_transform(signal)
        _, recon = inverse_fourier_transform(spectrum)
        np.testing.assert_allclose(recon[:len(signal)].real, signal, atol=1e-4)

    def test_power_spectrum(self):
        """功率譜非負。"""
        signal = np.sin(2 * np.pi * np.linspace(0, 1, 1000))
        freqs, power = power_spectrum(signal)
        assert np.all(power >= 0)


class TestFourierSeries:
    def test_constant_function(self):
        """常數函數的傅立葉系數：a0=2c, an=bn=0"""
        f = lambda t: 3.0
        a0, an, bn = fourier_series_coeff(f, T=2.0, n_terms=5)
        assert abs(a0 - 6.0) < 0.1
        np.testing.assert_allclose(an, 0, atol=0.1)

    def test_sine_series(self):
        """sin(2πt/T) 應有 b1=1"""
        f = lambda t: np.sin(2 * np.pi * t)
        a0, an, bn = fourier_series_coeff(f, T=1.0, n_terms=5)
        assert abs(bn[0] - 1.0) < 0.1

    def test_reconstruction(self):
        """重構應接近原函數。"""
        f = lambda t: np.sin(2 * np.pi * t)
        a0, an, bn = fourier_series_coeff(f, T=1.0, n_terms=10)
        t = np.linspace(0, 1, 100, endpoint=False)
        recon = reconstruct_fourier_series(a0, an, bn, 1.0, t)
        np.testing.assert_allclose(recon, f(t), atol=0.2)


class TestDFT:
    def test_dft_idft(self):
        """IDFT(DFT(x)) = x"""
        x = np.array([1.0, 2.0, 3.0, 4.0])
        X = dft(x)
        x_recon = idft(X)
        np.testing.assert_allclose(x_recon.real, x, atol=1e-10)

    def test_dft_linearity(self):
        """DFT(ax + by) = a DFT(x) + b DFT(y)"""
        x1 = np.array([1.0, 0.0, 1.0, 0.0])
        x2 = np.array([0.0, 1.0, 0.0, 1.0])
        X1 = dft(x1)
        X2 = dft(x2)
        X_sum = dft(x1 + x2)
        np.testing.assert_allclose(X_sum, X1 + X2, atol=1e-10)


class TestConvolutionFFT:
    def test_convolution_vs_direct(self):
        """FFT 摺積應接近直接摺積。"""
        x = np.array([1.0, 2.0, 3.0])
        h = np.array([0.5, 0.5])
        result = convolution_fft(x, h)
        expected = np.convolve(x, h, mode='full')
        np.testing.assert_allclose(result, expected, atol=1e-10)

    def test_identity_convolution(self):
        """與單位脈衝摺積應為原信號。"""
        x = np.array([1.0, 2.0, 3.0, 4.0])
        delta = np.array([1.0, 0.0, 0.0, 0.0])
        result = convolution_fft(x, delta)
        np.testing.assert_allclose(result[:len(x)], x, atol=1e-10)


class TestWindowedFT:
    def test_hanning_window(self):
        """加窗後信號直流分量應減少。"""
        signal = np.ones(100)
        freqs1, spec1 = fourier_transform(signal)
        freqs2, spec2 = windowed_ft(signal, window="hanning")
        # 加窗後直流分量應該減少
        assert abs(spec2[0]) < abs(spec1[0])

    def test_rectangular_window(self):
        """矩形窗應等於未加窗。"""
        signal = np.random.randn(64)
        freqs1, spec1 = fourier_transform(signal)
        freqs2, spec2 = windowed_ft(signal, window="rectangular")
        np.testing.assert_allclose(spec1, spec2, atol=1e-10)


class TestHaarWavelet:
    def test_haar_orthogonality(self):
        """Haar 小波在 [0,1) 上正交。"""
        t = np.linspace(0, 1, 1000, endpoint=False)
        psi = haar_wavelet(t)
        inner = np.sum(psi) * (1.0 / 1000)
        assert abs(inner) < 0.1

    def test_haar_support(self):
        """Haar 小波支撐在 [0,1)"""
        t = np.linspace(-0.5, 1.5, 2000)
        psi = haar_wavelet(t)
        assert np.all(psi[np.logical_or(t < 0, t >= 1)] == 0)


class TestDWT:
    def test_dwt_reconstruction(self):
        """IDWT(DWT(x)) = x"""
        signal = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0])
        approx, detail = dwt(signal)
        recon = idwt(approx, detail)
        np.testing.assert_allclose(recon, signal, atol=1e-10)

    def test_dwt_energy_conservation(self):
        """能量守恆：||x||² = ||approx||² + ||detail||²"""
        signal = np.random.randn(16)
        approx, detail = dwt(signal)
        energy_original = np.sum(signal**2)
        energy_dwt = np.sum(approx**2) + np.sum(detail**2)
        assert abs(energy_original - energy_dwt) < 1e-10


class TestMultilevelDWT:
    def test_multilevel_coeffs(self):
        """多層 DWT 係數數量應正確。"""
        signal = np.random.randn(64)
        coeffs = multilevel_dwt(signal, levels=3)
        assert len(coeffs) == 4  # [cA3, cD3, cD2, cD1]

    def test_multilevel_reconstruction(self):
        """多層重建應接近原信號。"""
        signal = np.random.randn(32)
        coeffs = multilevel_dwt(signal, levels=3)
        recon = coeffs[0]
        for detail in coeffs[1:]:
            recon = idwt(recon, detail)
        np.testing.assert_allclose(recon[:len(signal)], signal, atol=0.1)


class TestWaveletDenoising:
    def test_denoise_reduces_noise(self):
        """去雜訊應減少雜訊功率。"""
        signal = np.sin(2 * np.pi * np.linspace(0, 1, 96))  # 長度為 2 的冪次
        noise = 0.5 * np.random.randn(96)
        noisy = signal + noise
        denoised = wavelet_denoise(noisy, threshold=0.3)
        assert np.std(denoised - signal) < np.std(noisy - signal)


class TestLaplaceTransform:
    def test_unit_step(self):
        """L{1}(s) = 1/s"""
        f = lambda t: 1.0 if t >= 0 else 0.0
        s = 2.0 + 0j
        result = laplace_transform(f, s, t_max=20.0)
        expected = 1.0 / s
        assert abs(result - expected) < 0.01

    def test_exponential(self):
        """L{e^{-at}}(s) = 1/(s+a)"""
        a = 2.0
        f = lambda t: np.exp(-a * t)
        s = 3.0 + 0j
        result = laplace_transform(f, s, t_max=10.0)
        expected = 1.0 / (s + a)
        assert abs(result - expected) < 0.01


class TestInverseLaplace:
    def test_inverse_unit_step(self):
        """L⁻¹{1/s}(t) = 1"""
        F = lambda s: 1.0 / s
        t = 1.0
        result = inverse_laplace_bromwich(F, t, sigma=0.5)
        assert abs(result - 1.0) < 0.1


class TestLaplaceODSolve:
    def test_solve_first_order(self):
        """解 y' + y = 0, y(0)=1 => y=e^{-t}"""
        y_sol = solve_ode_laplace(a=1.0, b=0.0, y0=1.0)
        t = np.linspace(0, 2, 100)
        y_expected = np.exp(-t)
        np.testing.assert_allclose(y_sol(t), y_expected, atol=0.05)

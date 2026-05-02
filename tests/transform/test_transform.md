# test_transform.py

## 概述 (Overview)

測試信號處理中的轉換函數，包含傅立葉變換、拉普拉斯變換、小波變換等。

## 測試內容 (Test Coverage)

### TestFourierTransform
- `test_sine_wave`: 正弦波的頻譜在 f=±1 處有峰值
- `test_inverse_transform`: F⁻¹(F(f)) ≈ f
- `test_power_spectrum`: 功率譜非負

### TestFourierSeries
- `test_constant_function`: 常數函數的傅立葉係數 a0=2c, an=bn=0
- `test_sine_series`: sin(2πt) 的 b1=1
- `test_reconstruction`: 傅立葉級數重構接近原函數

### TestDFT
- `test_dft_idft`: IDFT(DFT(x)) = x
- `test_dft_linearity`: DFT(ax + by) = a DFT(x) + b DFT(y)

### TestConvolutionFFT
- `test_convolution_vs_direct`: FFT 摺積等於直接摺積
- `test_identity_convolution`: 與單位脈衝摺積為原信號

### TestWindowedFT
- `test_hanning_window`: 加窗後直流分量減少
- `test_rectangular_window`: 矩形窗等於未加窗

### TestHaarWavelet
- `test_haar_orthogonality`: Haar 小波正交性
- `test_haar_support`: Haar 小波支撐在 [0,1)

### TestDWT
- `test_dwt_reconstruction`: IDWT(DWT(x)) = x
- `test_dwt_energy_conservation`: ||x||² = ||approx||² + ||detail||²

### TestMultilevelDWT
- `test_multilevel_coeffs`: 多層 DWT 係數數量正確
- `test_multilevel_reconstruction`: 多層重建接近原信號

### TestWaveletDenoising
- `test_denoise_reduces_noise`: 去雜訊後誤差功率降低

### TestLaplaceTransform
- `test_unit_step`: L{1}(s) = 1/s
- `test_exponential`: L{e^{-at}}(s) = 1/(s+a)

### TestInverseLaplace
- `test_inverse_unit_step`: L⁻¹{1/s}(t) = 1

### TestLaplaceODSolve
- `test_solve_first_order`: 解 y' + y = 0, y(0)=1 => y=e^{-t}

## 測試原理 (Testing Principles)

- **傅立葉變換**: 時域 ↔ 頻域的對偶關係
- **離散傅立葉變換**: 有限長度信號的頻譜分析
- **摺積定理**: 時域摺積等於頻域乘法
- **小波變換**: 多尺度時頻分析
- **拉普拉斯變換**: 解微分方程的強大工具
- **能量守恆**: Parseval 定理保證變換前後能量相等
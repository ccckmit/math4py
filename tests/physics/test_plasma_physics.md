# test_plasma_physics.py - 電漿物理學測試文檔

## 概述 (Overview)

本測試文件驗證 math4py 電漿物理學模組的核心參數計算，包括德拜長度、電漿頻率、迴旋頻率、阿爾文速度。

## 測試內容 (Test Coverage)

### 測試類別

| 類別 | 測試內容 | 驗證結果 |
|------|----------|----------|
| `TestDebyeLength` | 德拜長度計算 | $\lambda_D > 0$ |
| `TestPlasmaFrequency` | 電漿頻率計算 | $f_{pe} > 0$ |
| `TestCyclotronFrequency` | 迴旋頻率計算 | $f_{ce} > 0$ |
| `TestAlfvenSpeed` | 阿爾文速度計算 | $v_A > 0$ |

## 測試原理 (Testing Principles)

### 德拜長度
$$\lambda_D = \sqrt{\frac{\epsilon_0 k_B T_e}{n_e e^2}}$$

電漿屏蔽距離，定義電漿微觀尺度。
- $k_B$：波茲曼常數
- $T_e$：電子溫度
- $n_e$：電子密度
- $e$：電子電荷

### 電漿頻率
$$f_{pe} = \frac{1}{2\pi}\sqrt{\frac{n_e e^2}{\epsilon_0 m_e}}$$

電子集體振盪特徵頻率。

### 迴旋頻率（拉摩頻率）
$$\omega_{ce} = \frac{eB}{m_e}$$

帶電粒子在磁場中的螺旋運動頻率。

### 阿爾文速度
$$v_A = \frac{B}{\sqrt{\mu_0 \rho}}$$

磁流體波在電漿中的傳播速度。
- $B$：磁場強度
- $\mu_0$：真空導磁率
- $\rho$：質量密度
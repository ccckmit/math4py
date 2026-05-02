# test_quantum.py - 量子力學測試文檔

## 概述 (Overview)

本測試文件驗證 math4py 量子力學模組的基本常數與計算，包括普朗克常數、德布羅意波長、光子能量。

## 測試內容 (Test Coverage)

### 測試類別

| 類別 | 測試內容 | 驗證結果 |
|------|----------|----------|
| `TestPlanckConstant` | 普朗克常數 | $h = 6.62607015 \times 10^{-34}$ J·s |
| `TestDeBroglie` | 德布羅意波長 | $\lambda > 0$ |
| `TestEnergyPhoton` | 光子能量 | 可見光約 $10^{-19}$ - $10^{-18}$ J |

## 測試原理 (Testing Principles)

### 普朗克常數
$$h = 6.62607015 \times 10^{-34} \text{ J·s}$$

量子化能量：$E = h\nu = \hbar\omega$

其中 $\hbar = h / 2\pi$

### 德布羅意波長
$$\lambda = \frac{h}{p}$$

粒子的波粒二象性：
- 動量 $p$ 越大，波長越小
- 宏觀物體動量極大，波長可忽略

### 光子能量
$$E = h\nu = \frac{hc}{\lambda}$$

- 可見光頻率：$\nu \approx 4.3 \times 10^{14}$ - $7.5 \times 10^{14}$ Hz
- 可見光能量：$E \approx 1.8$ - $3.1$ eV
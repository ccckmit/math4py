# test_electromagnetism.py - 電磁學測試文檔

## 概述 (Overview)

本測試文件驗證 math4py 電磁學模組的基本計算功能，包括庫侖力與導線磁場計算。

## 測試內容 (Test Coverage)

### 測試類別

| 類別 | 測試內容 | 預期結果 |
|------|----------|----------|
| `TestCoulombLaw` | 庫侖力計算 | 電力向量不為零 |
| `TestMagneticField` | 直導線磁場計算 | 磁場強度為正 |

## 測試原理 (Testing Principles)

### 庫侖定律
$$\vec{F} = k_e \frac{q_1 q_2}{r^2} \hat{r}$$

- $k_e = \frac{1}{4\pi\epsilon_0} \approx 8.99 \times 10^9$ N·m²/C²
- $r$：兩電荷間距離
- $\hat{r}$：從源電荷指向目標電荷的單位向量

### 導線磁場（安培定律）
無限長直導線產生的磁場：
$$B = \frac{\mu_0 I}{2\pi r}$$

- $\mu_0 = 4\pi \times 10^{-7}$ T·m/A
- $I$：電流強度
- $r$：到導線的垂直距離
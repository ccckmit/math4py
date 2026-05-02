# test_nuclear_physics.py - 核物理學測試文檔

## 概述 (Overview)

本測試文件驗證 math4py 核物理學模組的功能，包括質量虧損、結合能、衰變常數與半衰期計算。

## 測試內容 (Test Coverage)

### 測試類別

| 類別 | 測試內容 | 驗證原理 |
|------|----------|----------|
| `TestMassDefect` | 質量虧損計算 | $\Delta m = Z m_p + N m_n - m_{nucleus} > 0$ |
| `TestBindingEnergy` | 結合能計算 | $E = \Delta m \cdot c^2 > 0$ |
| `TestHalfLife` | 半衰期與衰變常數互算 | $T_{1/2} = \frac{\ln 2}{\lambda}$ |

## 測試原理 (Testing Principles)

### 質量虧損
$$\Delta m = Z m_p + N m_n + Z m_e - m_{atom}$$

或核質量形式：
$$\Delta m = Z m_p + N m_n - m_{nucleus}$$

- $Z$：質子數
- $N$：中子數
- $m_p \approx 1.007276$ u
- $m_n \approx 1.008665$ u

### 結合能
$$E_b = \Delta m \cdot c^2$$

愛因斯坦質能關係，常用單位為 MeV：
$1$ u $= 931.494$ MeV/c²

### 衰變動力學
$$\lambda = \frac{\ln 2}{T_{1/2}}$$

$$N(t) = N_0 e^{-\lambda t}$$

- $\lambda$：衰變常數
- $T_{1/2}$：半衰期
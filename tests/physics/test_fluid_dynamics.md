# test_fluid_dynamics.py - 流體動力學測試文檔

## 概述 (Overview)

本測試文件驗證 math4py 流體動力學模組的核心方程，包括連續方程式、柏努利方程式、雷諾數計算。

## 測試內容 (Test Coverage)

### 測試類別

| 類別 | 測試內容 | 驗證原理 |
|------|----------|----------|
| `TestContinuityEquation` | 連續方程式 | 質量守恆：$\rho_1 A_1 v_1 = \rho_2 A_2 v_2$ |
| `TestBernoulliEquation` | 柏努利方程式 | 能量守恆：$P + \frac{1}{2}\rho v^2 + \rho gh = \text{const}$ |
| `TestReynoldsNumber` | 雷諾數計算 | 層流條件：$Re < 2000$ |

## 測試原理 (Testing Principles)

### 連續方程式（質量守恆）
$$\rho_1 A_1 v_1 = \rho_2 A_2 v_2$$

不可壓縮流體（$\rho_1 = \rho_2$）：
$$A_1 v_1 = A_2 v_2$$

### 柏努利方程式（能量守恆）
$$P_1 + \frac{1}{2}\rho v_1^2 + \rho g h_1 = P_2 + \frac{1}{2}\rho v_2^2 + \rho g h_2$$

靜止流體：$P + \rho gh = \text{const}$

### 雷諾數
$$Re = \frac{\rho v L}{\mu} = \frac{v L}{\nu}$$

- $Re < 2000$：層流
- $2000 < Re < 4000$：過渡流
- $Re > 4000$：亂流
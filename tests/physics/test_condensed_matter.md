# test_condensed_matter.py - 凝態物理學測試文檔

## 概述 (Overview)

本測試文件驗證 math4py 凝態物理學模組的計算功能，包括帶隙與波長轉換、費米能計算、三維態密度等固態物理核心概念。

## 測試內容 (Test Coverage)

### 測試類別

| 類別 | 測試內容 | 預期結果 |
|------|----------|----------|
| `TestBandGapToWavelength` | 帶隙能量轉換波長 | 正值；可見光帶隙對應 400-700 nm |
| `TestFermiEnergy` | 費米能計算 | 正值 |
| `TestDensityOfStates3D` | 三維態密度計算 | 正值 |

## 測試原理 (Testing Principles)

### 帶隙與波長轉換
$$E_g = \frac{hc}{\lambda}$$

- $E_g$：帶隙能量（以 J 或 eV 為單位）
- $h$：普朗克常數
- $c$：光速
- 矽（Si）帶隙：約 1.12 eV

### 費米能
三維電子氣費米能：
$$E_F = \frac{\hbar^2}{2m}(3\pi^2 n)^{2/3}$$

- $n$：電子濃度
- $m$：電子質量

### 三維態密度
$$g(E) = \frac{1}{2\pi^2}\left(\frac{2m}{\hbar^2}\right)^{3/2} \sqrt{E}$$

在能量 $E$ 附近的單位體積單位能量狀態數
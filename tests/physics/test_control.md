# test_control.py - 控制理論測試文檔

## 概述 (Overview)

本測試文件驗證 math4py 控制理論模組的功能，包括傳遞函數建立與 Routh-Hurwitz 穩定性判據。

## 測試內容 (Test Coverage)

### 測試類別

| 類別 | 測試內容 | 測試案例 |
|------|----------|----------|
| `TestTransferFunction` | 創建傳遞函數 | $G(s) = \frac{1}{s+1}$ |
| `TestRouthHurwitz` | 穩定性判斷 | 穩定：$s^2 + 2s + 1$；不穩定：$s^2 - 1$ |

## 測試原理 (Testing Principles)

### 傳遞函數
線性時不變系統：$G(s) = \frac{N(s)}{D(s)}$

分子係數：$[1.0]$，分母係數：$[1.0, 1.0]$ 代表 $G(s) = \frac{1}{s+1}$

### Routh-Hurwitz 判據
系統穩定條件：特徵多項式所有根均有負實部

特徵多項式係數：$a_0 s^n + a_1 s^{n-1} + \cdots + a_n$

構造 Routh 陣列，第一列元素均為正則系統穩定。

### 測試案例
- $s^2 + 2s + 1 = (s+1)^2$：穩定（負實部根）
- $s^2 - 1 = (s+1)(s-1)$：不穩定（有正實部根）
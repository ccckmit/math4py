# test_optics.py - 光學測試文檔

## 概述 (Overview)

本測試文件驗證 math4py 光學模組的核心概念，包括斯涅爾定律、臨界角與全反射、放大率計算。

## 測試內容 (Test Coverage)

### 測試類別

| 類別 | 測試內容 | 驗證結果 |
|------|----------|----------|
| `TestSnellsLaw` | 斯涅爾定律 | 法線入射 $\theta_2 = 0$；全反射時 $\theta_2 = \infty$ |
| `TestCriticalAngle` | 臨界角計算 | $n_1 > n_2$ 時有臨界角；否則 $\theta_c = \infty$ |
| `TestMagnification` | 放大率計算 | 實像為負值 |

## 測試原理 (Testing Principles)

### 斯涅爾定律（折射定律）
$$n_1 \sin\theta_1 = n_2 \sin\theta_2$$

- $n_1, n_2$：兩介質折射率
- $\theta_1$：入射角（法線測量）
- $\theta_2$：折射角

法線入射時 $\theta_1 = 0 \Rightarrow \theta_2 = 0$

### 全反射與臨界角
當光由密介质射向疏介质（$n_1 > n_2$）時：
$$\sin\theta_c = \frac{n_2}{n_1}$$

若 $\theta_1 > \theta_c$，則發生全反射，$\sin\theta_2 > 1$（無物理解）

### 放大率
$$m = -\frac{v}{u}$$

- $u$：物距
- $v$：像距
- 實像 $m < 0$，虛像 $m > 0$
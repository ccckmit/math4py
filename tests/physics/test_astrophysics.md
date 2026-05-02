# test_astrophysics.py - 天文物理學測試文檔

## 概述 (Overview)

本測試文件驗證 math4py 天文物理學模組的計算功能，包括史瓦西半徑、軌道速度、逃逸速度等天體物理核心公式。

## 測試內容 (Test Coverage)

### 測試類別

| 類別 | 測試內容 | 預期結果 |
|------|----------|----------|
| `TestSchwarzschildRadius` | 史瓦西半徑計算 | 地球約 9mm |
| `TestOrbitalVelocity` | 圓軌道速度 | 地球約 30 km/s |
| `TestEscapeVelocity` | 逃逸速度計算 | 地球約 11.2 km/s |

## 測試原理 (Testing Principles)

### 史瓦西半徑
$$R_s = \frac{2GM}{c^2}$$

- 質量與半徑成正比：$R_s \propto M$
- 地球質量：$M_\oplus = 5.97 \times 10^{24}$ kg
- 地球史瓦西半徑：約 8.87 mm

### 軌道速度
$$v = \sqrt{\frac{GM}{r}}$$

- 地球軌道半徑：$r = 1.496 \times 10^{11}$ m
- 太陽質量：$M_\odot = 1.989 \times 10^{30}$ kg

### 逃逸速度
$$v_{esc} = \sqrt{\frac{2GM}{r}}$$

- 地球表面逃逸速度：約 11.2 km/s
- 為軌道速度的 $\sqrt{2}$ 倍
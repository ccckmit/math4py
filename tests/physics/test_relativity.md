# test_relativity.py - 相對論測試文檔

## 概述 (Overview)

本測試文件驗證 math4py 相對論模組的計算功能，包括羅倫茲因子、時間膨脹、長度收縮、時空間隔。

## 測試內容 (Test Coverage)

### 測試類別

| 類別 | 測試內容 | 驗證結果 |
|------|----------|----------|
| `TestLorentzFactor` | 羅倫茲因子 | $\gamma = 1$（靜止）；$\gamma > 1$（運動） |
| `TestTimeDilation` | 時間膨脹 | $\Delta t' = \gamma \Delta t$ |
| `TestLengthContraction` | 長度收縮 | $L' = L / \gamma$ |
| `TestSpacetimeInterval` | 時空間隔 | 類時間隔 $s^2 < 0$ |

## 測試原理 (Testing Principles)

### 羅倫茲因子
$$\gamma = \frac{1}{\sqrt{1 - \frac{v^2}{c^2}}}$$

- $v = 0$ 時，$\gamma = 1$
- $v \to c$ 時，$\gamma \to \infty$

### 時間膨脹
$$\Delta t = \gamma \Delta \tau$$

運動參考系中時間較慢（$\Delta \tau$ 為固有時）。

### 長度收縮
$$L = \frac{L_0}{\gamma}$$

運動方向上的長度收縮，垂直方向不變。

### 時空間隔
$$s^2 = -c^2(t_2-t_1)^2 + (x_2-x_1)^2 + (y_2-y_1)^2 + (z_2-z_1)^2$$

- $s^2 < 0$：類時間隔（可因果聯繫）
- $s^2 > 0$：類空間隔（不可因果聯繫）
- $s^2 = 0$：類光間隔
# R-style Plotting Functions

## 概述

本模組提供仿 R 風格的繪圖函數，包裝 matplotlib 但使用類似 R 的 API 介面，包括 `plot()`、`hist()`、`boxplot()`、`qqnorm()` 等。

## 數學原理

本模組主要處理資料視覺化，不涉及深層數學原理，而是將統計圖形的製作流程封裝成 R 風格 API。

### 支援的圖形類型

| 函數 | 類型 | R 對應 |
|------|------|--------|
| `plot()` | 散點圖、折線圖 | plot() |
| `hist()` | 直方圖 | hist() |
| `boxplot()` | 盒鬚圖 | boxplot() |
| `qqnorm()` | Q-Q 圖 | qqnorm() |

## 實作細節

### 設備控制函數

| 函數 | 說明 |
|------|------|
| `pdf(filename, width, height)` | 開啟 PDF 設備（仿 R pdf()） |
| `png(filename, width, height, dpi)` | 開啟 PNG 設備（仿 R png()） |
| `dev_off()` | 關閉設備，儲存圖形（仿 R dev.off()） |

### plot() 參數

| 參數 | 說明 |
|------|------|
| `type` | "p"=散點, "l"=折線, "b"=兩者 |
| `main` | 標題 |
| `xlab`, `ylab` | 軸標籤 |
| `col` | 顏色 |
| `pch` | 點形狀 |
| `lty` | 線型（1=實線, 2=虛線） |
| `lwd` | 線寬 |
| `xlim`, `ylim` | 軸範圍 |

### 輸出機制

- `filename=None`: 螢幕顯示
- `filename="out/xxx.pdf"`: 輸出到 PDF

## 使用方式

```python
from math4py.plot import plot, hist, boxplot, qqnorm
from math4py.plot import pdf, png, dev_off

# 散點圖
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 3, 5]
plot(x, y, main="散點圖", xlab="X", ylab="Y", col="blue")

# 折線圖
plot(x, y, type="l", main="折線圖")

# 直方圖
data = [1, 2, 2, 3, 3, 3, 4, 4, 5]
hist(data, breaks=5, main="直方圖", freq=True)

# 盒鬚圖
boxplot([1, 2, 3, 4, 5], [2, 3, 4, 5, 6], names=["A", "B"])

# Q-Q 圖（常態性檢驗）
import numpy as np
data = np.random.normal(0, 1, 100)
qqnorm(data)

# 輸出到 PDF
pdf("out/scatter.pdf")
plot(x, y)
plot([1,2,3], [3,2,1])
dev_off()  # 儲存並關閉

# 輸出到 PNG
png("out/histogram.png", dpi=300)
hist(data)
dev_off()
```
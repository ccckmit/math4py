# test_rplot.py - R風格繪圖測試文檔

## 概述 (Overview)

本測試文件驗證 math4py 繪圖模組的 R 風格統計圖形功能，包括散點圖、線圖、直方圖、箱線圖、Q-Q 圖，以及資訊熵與 KL 散度可視化。

## 測試內容 (Test Coverage)

### 測試類別

| 類別 | 測試內容 | 輸出類型 |
|------|----------|----------|
| `TestPlot` | 散點圖/線圖/組合圖 | PDF |
| `TestHist` | 直方圖（頻率/密度） | PDF |
| `TestBoxplot` | 單/多組箱線圖 | PDF |
| `TestQQNorm` | 常態Q-Q圖 | PDF |
| `TestPlotEntropy` | 資訊熵視覺化 | PDF |
| `TestPlotKL` | KL散度繪圖 | PDF |

### TestPlot 細項
| 測試 | 類型參數 | 說明 |
|------|----------|------|
| `test_plot_scatter` | `type="p"` | 散點圖 |
| `test_plot_line` | `type="l"` | 線圖 |
| `test_plot_both` | `type="b"` | 同時顯示點和線 |
| `test_plot_series` | 無 x 參數 | 時間序列圖 |

### TestHist 細項
| 測試 | 頻率模式 |
|------|----------|
| `test_hist_basic` | 頻數（預設） |
| `test_hist_density` | 密度 |

### TestQQNorm 細項
| 測試 | 數據類型 | 預期圖形 |
|------|----------|----------|
| `test_qqnorm_normal` | 常態分布 | 近似直線 |
| `test_qqnorm_uniform` | 均勻分布 | 偏離直線 |

## 測試原理 (Testing Principles)

### 散點圖與線圖
`plot(x, y, type="p/l/b")` 模仿 R 語言語法：
- `type="p"`：points（散點）
- `type="l"`：lines（線段）
- `type="b"`：both（兼具兩者）

### 直方圖
$$f_{density} = \frac{n_i}{N \cdot \Delta x}$$

密度模式將頻數除以總數與組距，積分為 1。

### Q-Q 圖
比較樣本分位數與理論分位數：
- 常態數據：Q-Q 圖呈直線
- 偏離直線表示偏離常態

### 資訊熵
$$H(X) = -\sum_i p_i \log p_i$$

均勻分布具有最大熵，確切事件 $H = 0$。

### KL 散度
$$D_{KL}(P\|Q) = \sum_i p_i \log\frac{p_i}{q_i}$$

衡量分布 $P$ 與 $Q$ 的差異，恆正（除 $P=Q$ 外）。
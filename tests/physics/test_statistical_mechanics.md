# test_statistical_mechanics.py - 統計力學測試文檔

## 概述 (Overview)

本測試文件驗證 math4py 統計力學模組的核心計算，包括波茲曼分布、配分函數、馬克斯威爾-波茲曼速率分布。

## 測試內容 (Test Coverage)

### 測試類別

| 類別 | 測試內容 | 驗證結果 |
|------|----------|----------|
| `TestBoltzmannDistribution` | 波茲曼概率 | $0 \leq P \leq 1$；能量越高概率越低 |
| `TestPartitionFunction` | 配分函數計算 | $Z > 0$ |
| `TestMaxwellBoltzmannSpeed` | 速率分布 | $f(v) \geq 0$ |

## 測試原理 (Testing Principles)

### 波茲曼分布
$$P(E) = \frac{e^{-E/k_BT}}{Z}$$

單粒子能級佔有概率：
- 能量 $E$ 越低，概率越高
- 溫度 $T$ 越高，高能態概率相對增加

其中 $k_B$ 為波茲曼常數，$Z$ 為配分函數。

### 配分函數
$$Z = \sum_i e^{-E_i/k_BT}$$

歸一化因子，連續形式：
$$Z = \int_0^\infty g(E) e^{-E/k_BT} dE$$

### 馬克斯威爾-波茲曼速率分布
$$f(v) = 4\pi \left(\frac{m}{2\pi k_B T}\right)^{3/2} v^2 e^{-mv^2/2k_BT}$$

最可能速率：
$$v_{mp} = \sqrt{\frac{2k_BT}{m}}$$

平均速率：
$$\bar{v} = \sqrt{\frac{8k_BT}{\pi m}}$$
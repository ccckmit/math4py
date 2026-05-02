# test_thermodynamics.py - 熱力學測試文檔

## 概述 (Overview)

本測試文件驗證 math4py 熱力學模組的核心計算，包括理想氣體定律與卡諾效率。

## 測試內容 (Test Coverage)

### 測試類別

| 類別 | 測試內容 | 驗證結果 |
|------|----------|----------|
| `TestIdealGasLaw` | 理想氣體定律 | $PV = nRT$ 各變數互算 |
| `TestCarnotEfficiency` | 卡諾循環效率 | $T_1 = T_2$ 時 $\eta = 0$；$\eta > 0$ 當 $T_h > T_c$ |

## 測試原理 (Testing Principles)

### 理想氣體定律
$$PV = nRT = Nk_BT$$

- $P$：壓力（Pa）
- $V$：體積（m³）
- $n$：莫爾數
- $R = 8.314462618$ J/(mol·K)：通用氣體常數
- $T$：絕對溫度（K）

常用形式：
$$PV = Nk_BT$$
其中 $N = n \cdot N_A$ 為分子數。

### 卡諾效率
$$\eta = 1 - \frac{T_c}{T_h} = \frac{T_h - T_c}{T_h}$$

可逆熱機最大效率：
- 當 $T_h = T_c$ 時，$\eta = 0$（無功輸出）
- 當 $T_h \gg T_c$ 時，$\eta \to 1$

注意：需使用絕對溫度（K）。
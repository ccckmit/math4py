# test_acoustics.py - 聲學測試文檔

## 概述 (Overview)

本測試文件驗證 math4py 聲學模組的基本計算功能，包括音速、都卜勒效應、分貝計算等核心概念。

## 測試內容 (Test Coverage)

### 測試類別

| 類別 | 測試內容 | 預期結果 |
|------|----------|----------|
| `TestSoundSpeed` | 空氣中音速計算 | 約 343 m/s (20°C) |
| `TestDopplerShift` | 都卜勒頻率偏移 | 接近時頻率增加 |
| `TestDecibelLevel` | 分貝等級計算 | 參考強度為 0 dB |

## 測試原理 (Testing Principles)

### 音速計算
理想氣體音速：$c = \sqrt{\gamma \cdot \frac{R}{M} \cdot T}$

其中：
- $\gamma$：比熱比（空氣約 1.4）
- $R$：氣體常數
- $M$：莫爾質量
- $T$：絕對溫度

### 都卜勒效應
$$f' = f \cdot \frac{v}{v - v_{source}}$$

當聲源接近觀測者（$v_{source} > 0$）時，觀測頻率 $f' > f$

### 分貝計算
$$dB = 10 \log_{10}\left(\frac{I}{I_0}\right)$$

參考強度 $I_0 = 10^{-12}$ W/m²
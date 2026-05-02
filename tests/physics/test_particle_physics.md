# test_particle_physics.py - 粒子物理學測試文檔

## 概述 (Overview)

本測試文件驗證 math4py 粒子物理學模組的功能，包括羅倫茲不變質量、衰變寬度與壽命關係、分支比計算。

## 測試內容 (Test Coverage)

### 測試類別

| 類別 | 測試內容 | 驗證結果 |
|------|----------|----------|
| `TestLorentzInvariantMass` | 羅倫茲不變質量計算 | $m > 0$ |
| `TestDecayWidthToLifetime` | 衰變寬度轉換壽命 | $\tau = \hbar / \Gamma > 0$ |
| `TestBranchingRatio` | 分支比計算 | $0 \leq BR \leq 1$ |

## 測試原理 (Testing Principles)

### 羅倫茲不變質量
$$m^2 c^4 = E^2 - |\vec{p}|^2 c^2$$

對於多粒子系統：
$$m^2 = \left(\sum E_i\right)^2 - \left|\sum \vec{p}_i\right|^2$$

這是相對論性不變量，適用於任意慣性參考系。

### 衰變寬度與壽命
$$\tau = \frac{\hbar}{\Gamma}$$

- $\Gamma$：總衰變寬度（energy width）
- $\tau$：平均壽命
- 測不準原理：$\Delta E \cdot \Delta t \sim \hbar/2$

### 分支比
$$BR_i = \frac{\Gamma_i}{\Gamma_{total}}$$

指定衰變模式的寬度佔總寬度的比例，所有分支比之和為 1：
$$\sum_i BR_i = 1$$
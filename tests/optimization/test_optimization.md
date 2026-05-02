# test_optimization.py - 最優化測試文檔

## 概述 (Overview)

本測試文件驗證 math4py 最優化模組的功能，包括：
- 梯度下降、牛頓法、共軛梯度法
- 爬山演算法、模擬退火
- 線性規劃（單形法、LP求解）
- 凸性分析與最優性條件

## 測試內容 (Test Coverage)

### 優化演算法測試
| 類別 | 測試內容 |
|------|----------|
| `TestGradientDescent` | 梯度下降收斂到二次函數極值 |
| `TestNewtonMethod` | 牛頓法快速收斂驗證 |
| `TestConjugateGradient` | 共軛梯度法求解線性系統 Ax=b |
| `TestBacktrackingLineSearch` | 回溯線搜索返回正步長 |
| `TestHillClimbing` | 爬山演算法求極值 |
| `TestHillClimbingSimple` | 簡化版爬山演算法 |
| `TestRandomRestartHillClimbing` | 隨機重啟爬山 |
| `TestSimulatedAnnealing` | 模擬退火演算法 |

### 凸性分析測試
| 類別 | 測試內容 |
|------|----------|
| `TestIsConvexFunction` | 凸函數/凹函數判斷 |
| `TestConvexFirstOrderCondition` | 凸函數一階條件 |
| `TestConvexSecondOrderCondition` | 凸函數二階條件（Hessian正定） |

### 線性規劃測試
| 類別 | 測試內容 |
|------|----------|
| `TestSimplexMethod` | 單形法求解LP |
| `TestSolveLP` | LP問題求解 |
| `TestIsFeasiblePoint` | 可行點判斷 |
| `TestDualityGap` | 對偶間隙計算 |

### 定理驗證測試
| 類別 | 測試內容 |
|------|----------|
| `TestGradientVanishing` | 極值點梯度為零 |
| `TestConvexOptimality` | 凸函數最優性條件 |

## 測試原理 (Testing Principles)

### 梯度下降法
沿負梯度方向迭代：$x_{k+1} = x_k - \alpha \nabla f(x_k)$

### 牛頓法
利用Hessian加速收斂：$x_{k+1} = x_k - H^{-1}\nabla f$

### 凸性條件
- 一階條件：$f(y) \geq f(x) + \nabla f(x)^T(y-x)$
- 二階條件：Hessian $H \succeq 0$

### 線性規劃
標準形式：$\min c^T x \quad \text{s.t.} \quad Ax \leq b$
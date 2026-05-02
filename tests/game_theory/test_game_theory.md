# test_game_theory.py

## 概述 (Overview)

測試遊戲理論（Game Theory）模組的定理和函數功能，包括納什均衡、極大極小定理、優勢策略、零和遊戲等核心概念。

## 測試內容 (Test Coverage)

### 定理測試 (Theorem Tests)

| 類別 | 測試內容 |
|------|----------|
| `TestNashEquilibrium` | 納什均衡定理驗證（囚犯困境、協調遊戲） |
| `TestMinimax` | 極大極小定理（匹配硬幣遊戲） |
| `TestDominantStrategy` | 優勢策略存在性檢驗 |
| `TestZeroSum` | 零和遊戲價值定理 |
| `TestPrisonersDilemma` | 囚犯困境均衡點驗證 |
| `TestBattleSex` | 鬥雞博弈多重均衡 |
| `TestMixedStrategy` | 混合策略機率總和為1 |
| `TestIteratedDominance` | 重複優勢消除定理 |

### 函數 API 測試 (Function API Tests)

| 函數 | 測試內容 |
|------|----------|
| `payoff_matrix` | 支付矩陣構建 |
| `best_response` | 最佳回應策略計算 |
| `nash_equilibrium` | 納什均衡求解 |
| `expected_payoff` | 期望支付計算 |
| `prisoner_dilemma` | 囚犯困境標準支付矩陣 |
| `matching_pennies` | 匹配硬幣遊戲標準支付矩陣 |
| `battle_sex` | 鬥雞博弈標準支付矩陣 |

## 測試原理 (Testing Principles)

- **納什均衡**：在他人策略固定下，沒有人能單方面改變策略而獲得更好結果
- **極大極小**：玩家最大化自身最小支付（保守策略）
- **優勢策略**：無論對手如何選擇，該策略都優於其他策略
- **零和遊戲**：一方的收益正好是另一方的損失
- **混合策略**：將多個純策略以機率混合，確保行動不可預測
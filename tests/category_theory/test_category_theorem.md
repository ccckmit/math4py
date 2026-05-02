# test_category_theorem.py

## 概述 (Overview)

測試 `math4py.category_theory.theorem` 模組，驗證範疇論的核心定理與性質，包括範疇公理、函子定律、米田嵌入、伴隨函子定理等。

## 測試內容 (Test Coverage)

| 類別 | 測試項目 |
|------|----------|
| `TestCategoryAxioms` | 範疇公理驗證（有效性、恆等法則） |
| `TestFunctorLaws` | 函子定律（保持結構） |
| `TestYonedaEmbedding` | 米田嵌入定理（完全且忠實） |
| `TestAdjointFunctorTheorem` | 伴隨函子定理（三角形恆等式） |
| `TestLimitUniqueness` | 極限唯一性（同構意義下） |
| `TestInitialObjectUniqueness` | 始物件唯一性 |
| `TestTerminalObjectUniqueness` | 終物件唯一性 |

## 測試原理 (Testing Principles)

- **範疇公理**：
  - 結合律：(f∘g)∘h = f∘(g∘h)
  - 恆等律：id∘f = f = f∘id
- **函子定律**：
  - F(idₐ) = id_{F(A)}
  - F(g∘f) = F(g)∘F(f)
- **米田嵌入**：將範疇 C 嵌入到 [C, Set]，為完全忠實函子
- **伴隨函子**：單位 η: 1 → GF，余單位 ε: FG → 1
- **極限唯一性**：泛態射的唯一性
- **物件唯一性**：始/終物件在同構意義下唯一
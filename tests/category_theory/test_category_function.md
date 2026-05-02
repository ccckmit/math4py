# test_category_function.py

## 概述 (Overview)

測試 `math4py.category_theory.function` 模組，實作範疇論的基礎結構，包括物件（Object）、態射（Morphism）、範疇（Category）、函子（Functor）、自然變換（Natural Transformation）等。

## 測試內容 (Test Coverage)

| 類別 | 測試項目 |
|------|----------|
| `TestObject` | 範疇物件創建與屬性 |
| `TestMorphism` | 態射創建（f: A → B） |
| `TestCategory` | 範疇創建、添加物件/態射、恆等態射、範疇有效性 |
| `TestFunctor` | 函子創建與性質 |
| `TestNaturalTransformation` | 自然變換 |
| `TestLimitProduct` | 乘積極限 |
| `TestColimitCoproduct` | 餘乘積餘極限 |
| `TestAdjointFunctors` | 伴隨函子 |
| `TestYonedaLemma` | 米田引理 |
| `TestInitialObject` | 始物件 |
| `TestTerminalObject` | 終物件 |

## 測試原理 (Testing Principles)

- **範疇公理**：態射可複合、複合滿足結合律、有恆等態射
- **函子**：保持物件與態射結構，保存恆等態射與複合
- **自然變換**：函子間的自然映射
- **極限/餘極限**：泛性質（Universal Property）
- **米田引理**：Hom(A,-) 與 F(A) 的自然同構
- **伴隨函子**：單位與餘單位滿足三角形恆等式
- **始/終物件**：唯一（至多差一個同構）
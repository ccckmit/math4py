# test_structures.py

## 概述 (Overview)

測試 `math4py.algebra.function` 模組，此模組實作代數結構的抽象類別：群（Group）、環（Ring）、域（Field）、向量空間（VectorSpace）。

## 測試內容 (Test Coverage)

| 類別 | 測試項目 |
|------|----------|
| `TestGroup` | Z/3Z 加法群（交換群）、S₃ 置換群 |
| `TestRing` | Z/4Z 環 |
| `TestField` | F₅ 有限域 |
| `TestVectorSpace` | F₂ 上的二維向量空間 |

## 測試原理 (Testing Principles)

- **群公理**：封閉性、結合性、恆等元素、逆元素
- **交換群**：額外滿足交換律
- **環公理**：加法群 + 乘法封閉 + 分配律
- **域公理**：環 + 非零元素乘法逆元
- **向量空間**：域上的加法群 + 純量乘法
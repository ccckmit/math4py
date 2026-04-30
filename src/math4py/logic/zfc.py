"""ZFC 公理系統（Zermelo-Fraenkel + Choice）。"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Set, Tuple


@dataclass
class Set:
    """集合的簡化表示。

    為了簡化，我們用 Python 集合模擬集合論中的集合。
    注意：這是一個簡化版本，無法完整表達集合論的所有概念。
    """

    elements: Set[Any] = field(default_factory=set)
    name: Optional[str] = None

    def __hash__(self):
        # 簡化：使用名稱或 id
        if self.name:
            return hash(self.name)
        return id(self)

    def __eq__(self, other):
        if isinstance(other, Set):
            return self.elements == other.elements
        return False

    def __repr__(self):
        if self.name:
            return f"Set({self.name})"
        return f"Set({self.elements})"


# 預定義的基本集合
EMPTY_SET = Set(elements=set(), name="∅")


def extensionality_axiom(A: Set, B: Set) -> bool:
    """外延公理（Axiom of Extensionality）。

    兩個集合相等當且僅當它們有完全相同的元素。
    ∀A ∀B (∀x (x ∈ A ↔ x ∈ B) → A = B)

    Returns:
        如果 A 和 B 有相同元素，返回 True
    """
    return A.elements == B.elements


def pair_set_axiom(a: Any, b: Any) -> Set:
    """無序對公理（Axiom of Pairing）。

    給定任意兩個集合 a 和 b，存在一個集合 {a, b} 包含它們。
    ∀a ∀b ∃c ∀x (x ∈ c ↔ (x = a ∨ x = b))
    """
    return Set(elements={a, b})


def union_axiom(sets: List[Set]) -> Set:
    """併集公理（Axiom of Union）。

    給定一個集合的集合，存在一個集合包含這些集合的所有元素。
    ∀F ∃A ∀x (x ∈ A ↔ ∃S (S ∈ F ∧ x ∈ S))
    """
    union_elements = set()
    for s in sets:
        union_elements.update(s.elements)
    return Set(elements=union_elements)


def power_set_axiom(s: Set) -> Set:
    """冪集公理（Axiom of Power Set）。

    給定集合 s，存在一個集合 P(s) 包含 s 的所有子集。
    ∀s ∃P ∀x (x ∈ P ↔ x ⊆ s)
    """
    # 簡化：這裡不實現真正的冪集，只返回一個標記
    return Set(elements=set(), name=f"P({s.name or s})")


def infinity_axiom() -> Set:
    """無窮公理（Axiom of Infinity）。

    存在一個歸納集合：包含 ∅ 且對每個元素 x，x ∪ {x} 也在集合中。
    這保證了自然數集合的存在。
    """
    # 構造一個簡化的無窮集合的表示
    # 實際實現需要更複雜的結構
    return Set(elements=set(), name="ℕ (infinite)")


def replacement_schema(F: Any, A: Set) -> Set:
    """替換公理模式（Axiom Schema of Replacement）。

    如果 F 是一個函數（類），那麼對於集合 A，存在集合 B = {F(x) : x ∈ A}。
    ∀A ∀F ∃B ∀y (y ∈ B ↔ ∃x ∈ A (y = F(x)))

    Args:
        F: 函數（Python 函數或映射）
        A: 原集合

    Returns:
        替換後的集合
    """
    new_elements = set()
    for x in A.elements:
        try:
            y = F(x)
            new_elements.add(y)
        except Exception:
            pass  # 忽略無法映射的元素
    return Set(elements=new_elements)


def foundation_axiom(s: Set) -> bool:
    """正則公理（Axiom of Foundation / Regularity）。

    每個非空集合都包含一個與自身不相交的元素。
    ∀x (x ≠ ∅ → ∃y ∈ x (y ∩ x = ∅))

    這防止了集合包含自身的情況（x ∈ x）。
    """
    if not s.elements:
        return True  # 空集滿足

    for y in s.elements:
        if isinstance(y, Set):
            # 檢查 y ∩ s = ∅
            if y.elements.isdisjoint(s.elements):
                return True
        else:
            # 基本元素（不是集合）自動滿足
            return True

    return False


def choice_axiom(sets: List[Set]) -> Tuple[bool, Optional[Dict[int, Any]]]:
    """選擇公理（Axiom of Choice）。

    給定一族非空集合，存在一個函數（選擇函數）從每個集合中選擇一個元素。
    ∀F (∀x ∈ F (x ≠ ∅) → ∃f: F → ⋃F ∀x ∈ F (f(x) ∈ x))

    Returns:
        (是否成功, 選擇字典)
    """
    choice_dict = {}
    for i, s in enumerate(sets):
        if not s.elements:
            return False, None  # 空集，選擇公理不適用
        # 選擇第一個元素（簡化）
        element = next(iter(s.elements))
        choice_dict[i] = element
    return True, choice_dict


def is_set_element(x: Any, s: Set) -> bool:
    """檢查 x 是否為集合 s 的元素。"""
    return x in s.elements


def is_subset(A: Set, B: Set) -> bool:
    """檢查 A ⊆ B。"""
    return A.elements.issubset(B.elements)


def construct_natural_numbers() -> List[Set]:
    """構造自然數（馮·諾伊曼表示法）。

    0 = ∅
    1 = {∅}
    2 = {∅, {∅}}
    3 = {∅, {∅}, {∅, {∅}}}
    ...
    """
    numbers = []
    current = EMPTY_SET

    for n in range(10):  # 構造前 10 個自然數
        num_set = Set(elements=current.elements.copy(), name=str(n))
        numbers.append(num_set)
        # 下一個數：current ∪ {current}
        next_elements = current.elements.copy()
        next_elements.add(current)
        current = Set(elements=next_elements)

    return numbers


def separation_schema(P: Any, A: Set) -> Set:
    """分離公理模式（Axiom Schema of Separation / Subset）。

    給定集合 A 和性質 P，存在集合 B = {x ∈ A : P(x)}。
    ∀A ∀P ∃B ∀x (x ∈ B ↔ (x ∈ A ∧ P(x)))
    """
    new_elements = set()
    for x in A.elements:
        try:
            if P(x):
                new_elements.add(x)
        except Exception:
            pass
    return Set(elements=new_elements)


def ordered_pair(a: Any, b: Any) -> Set:
    """構造有序對 (a, b) = {{a}, {a, b}}。"""
    return Set(elements={Set(elements={a}), Set(elements={a, b})})


def is_ordered_pair_equal(p1: Set, p2: Set) -> bool:
    """檢查兩個有序對是否相等。

    (a, b) = (c, d) 當且僅當 a = c 且 b = d。
    """
    if len(p1.elements) != len(p2.elements):
        return False
    # 簡化檢查（完整的檢查需要更細緻的比較）
    return p1.elements == p2.elements


# ZFC 公理系統的完整檢查
def verify_zfc_axioms() -> Dict[str, bool]:
    """驗證 ZFC 各公理的基本性質。"""
    results = {}

    # 外延公理
    A = Set(elements={1, 2, 3})
    B = Set(elements={3, 2, 1})
    results["extensionality"] = extensionality_axiom(A, B)

    # 無序對公理
    pair = pair_set_axiom(1, 2)
    results["pair_set"] = len(pair.elements) == 2

    # 併集公理
    s1 = Set(elements={1, 2})
    s2 = Set(elements={3, 4})
    union = union_axiom([s1, s2])
    results["union"] = len(union.elements) == 4

    # 正則公理
    s = Set(elements={1, 2, 3})
    results["foundation"] = foundation_axiom(s)

    # 選擇公理
    sets = [Set(elements={1, 2}), Set(elements={3, 4}), Set(elements={5})]
    success, _ = choice_axiom(sets)
    results["choice"] = success

    return results


__all__ = [
    "Set",
    "EMPTY_SET",
    "extensionality_axiom",
    "pair_set_axiom",
    "union_axiom",
    "power_set_axiom",
    "infinity_axiom",
    "replacement_schema",
    "foundation_axiom",
    "choice_axiom",
    "is_set_element",
    "is_subset",
    "construct_natural_numbers",
    "separation_schema",
    "ordered_pair",
    "verify_zfc_axioms",
]

"""ZFC 公理系統測試。"""

import pytest
from math4py.logic.zfc import (
    Set,
    EMPTY_SET,
    extensionality_axiom,
    pair_set_axiom,
    union_axiom,
    power_set_axiom,
    infinity_axiom,
    foundation_axiom,
    choice_axiom,
    is_set_element,
    is_subset,
    construct_natural_numbers,
    separation_schema,
    ordered_pair,
    verify_zfc_axioms,
)


class TestSet:
    def test_creation(self):
        """創建集合。"""
        s = Set(elements={1, 2, 3})
        assert len(s.elements) == 3

    def test_empty_set(self):
        """空集不應包含任何元素。"""
        assert len(EMPTY_SET.elements) == 0

    def test_equality(self):
        """兩個有相同元素的集合應相等。"""
        s1 = Set(elements={1, 2})
        s2 = Set(elements={2, 1})
        assert s1 == s2


class TestExtensionalityAxiom:
    def test_equal_sets(self):
        """外延公理：相同元素的集合相等。"""
        A = Set(elements={1, 2, 3})
        B = Set(elements={3, 2, 1})
        assert extensionality_axiom(A, B)

    def test_different_sets(self):
        """不同元素的集合不相等。"""
        A = Set(elements={1, 2})
        B = Set(elements={1, 3})
        assert not extensionality_axiom(A, B)


class TestPairSetAxiom:
    def test_pair_creation(self):
        """無序對 {a, b}。"""
        pair = pair_set_axiom(1, 2)
        assert is_set_element(1, pair)
        assert is_set_element(2, pair)
        assert len(pair.elements) == 2

    def test_pair_with_same_element(self):
        """{a, a} = {a}。"""
        pair = pair_set_axiom(1, 1)
        assert len(pair.elements) == 1


class TestUnionAxiom:
    def test_union_of_sets(self):
        """併集：{1,2} ∪ {3,4} = {1,2,3,4}。"""
        s1 = Set(elements={1, 2})
        s2 = Set(elements={3, 4})
        union = union_axiom([s1, s2])
        assert len(union.elements) == 4
        assert is_set_element(1, union)
        assert is_set_element(3, union)

    def test_union_with_empty(self):
        """與空集的併集。"""
        s = Set(elements={1, 2})
        union = union_axiom([s, EMPTY_SET])
        assert is_subset(s, union)


class TestFoundationAxiom:
    def test_regular_set(self):
        """正則集合應滿足正則公理。"""
        s = Set(elements={1, 2, 3})
        assert foundation_axiom(s)

    def test_empty_set(self):
        """空集滿足正則公理。"""
        assert foundation_axiom(EMPTY_SET)


class TestChoiceAxiom:
    def test_choice_exists(self):
        """非空集合族存在選擇函數。"""
        sets = [Set(elements={1, 2}), Set(elements={3, 4})]
        success, choice = choice_axiom(sets)
        assert success
        assert choice is not None
        assert len(choice) == 2

    def test_with_empty_set(self):
        """包含空集的集合族不滿足選擇公理條件。"""
        sets = [Set(elements={1}), EMPTY_SET]
        success, _ = choice_axiom(sets)
        assert not success


class TestSubset:
    def test_is_subset(self):
        """子集關係。"""
        A = Set(elements={1, 2})
        B = Set(elements={1, 2, 3})
        assert is_subset(A, B)

    def test_not_subset(self):
        """非子集。"""
        A = Set(elements={1, 4})
        B = Set(elements={1, 2, 3})
        assert not is_subset(A, B)


class TestConstructNaturalNumbers:
    def test_first_few(self):
        """構造自然數。"""
        numbers = construct_natural_numbers()
        assert len(numbers) > 0
        # 0 = ∅
        assert len(numbers[0].elements) == 0

    def test_names(self):
        """自然數應有正確的名稱。"""
        numbers = construct_natural_numbers()
        for n in numbers[:5]:
            assert n.name is not None


class TestSeparationSchema:
    def test_filter_even(self):
        """分離公理：抽取偶數。"""
        A = Set(elements={1, 2, 3, 4, 5, 6})
        even_pred = lambda x: x % 2 == 0
        evens = separation_schema(even_pred, A)
        assert is_set_element(2, evens)
        assert is_set_element(4, evens)
        assert not is_set_element(1, evens)

    def test_empty_result(self):
        """分離結果可能為空。"""
        A = Set(elements={1, 2, 3})
        pred = lambda x: x > 10
        result = separation_schema(pred, A)
        assert len(result.elements) == 0


class TestOrderedPair:
    def test_pair_creation(self):
        """有序對 (a, b)。"""
        pair = ordered_pair(1, 2)
        assert len(pair.elements) == 2

    def test_pair_representation(self):
        """檢查有序對的內部表示。"""
        pair = ordered_pair(1, 2)
        # 應該是 {{1}, {1, 2}}
        assert len(pair.elements) == 2


class TestVerifyZFC:
    def test_all_axioms(self):
        """驗證所有 ZFC 公理的基本性質。"""
        results = verify_zfc_axioms()
        assert "extensionality" in results
        assert "pair_set" in results
        assert "union" in results
        assert "choice" in results
        # 大部分公理應該返回 True
        assert sum(1 for v in results.values() if v) >= 4

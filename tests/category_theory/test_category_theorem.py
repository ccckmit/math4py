"""Test category theory theorem module."""

import math4py.category_theory.theorem as catt
from math4py.category_theory.function import Category, Morphism


class TestCategoryAxioms:
    def test_valid_category(self):
        """檢查有效範疇的公理。"""
        C = Category("C")
        id_A = Morphism(source="A", target="A", name="id_A")
        id_B = Morphism(source="B", target="B", name="id_B")
        f = Morphism(source="A", target="B", name="f")
        C.add_morphism(id_A)
        C.add_morphism(id_B)
        C.add_morphism(f)
        C.composition_table = {("f", "id_B"): "f", ("id_A", "f"): "f"}

        result = catt.category_axioms(C)
        assert result["pass"]
        assert result["has_identity"]
        assert result["identity_law"]

    def test_invalid_category(self):
        """檢查無恆等態射的範疇。"""
        C = Category("C")
        # 沒有恆等態射
        result = catt.category_axioms(C)
        assert not result["pass"]


class TestFunctorLaws:
    def test_functor_preserves_structure(self):
        """檢查函子保持結構。"""
        F = {"preserves_identity": True, "preserves_composition": True}
        result = catt.functor_laws(F)
        assert result["pass"]
        assert result["preserves_identity"]


class TestYonedaEmbedding:
    def test_yoneda_embedding_theorem(self):
        """檢查米田嵌入定理。"""
        C = Category("C")
        result = catt.yoneda_embedding_theorem(C)
        assert result["pass"]
        assert result["full"]
        assert result["faithful"]


class TestAdjointFunctorTheorem:
    def test_adjoint_functor_theorem(self):
        """檢查伴隨函子定理。"""
        unit = {"η": "unit"}
        counit = {"ε": "counit"}
        result = catt.adjoint_functor_theorem(unit, counit)
        assert result["pass"]
        assert result["triangle_identities"]


class TestLimitUniqueness:
    def test_limit_unique(self):
        """檢查極限的唯一性。"""
        limit1 = {"object": "P1"}
        limit2 = {"object": "P2"}
        result = catt.limit_uniqueness(limit1, limit2)
        assert result["pass"]
        assert result["unique_up_to_isomorphism"]


class TestInitialObjectUniqueness:
    def test_initial_unique(self):
        """檢查始物件的唯一性。"""
        result = catt.initial_object_uniqueness("I1", "I2")
        assert result["pass"]
        assert result["unique"]


class TestTerminalObjectUniqueness:
    def test_terminal_unique(self):
        """檢查終物件的唯一性。"""
        result = catt.terminal_object_uniqueness("T1", "T2")
        assert result["pass"]
        assert result["unique"]

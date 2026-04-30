"""Test category theory function module."""

import math4py.category_theory.function as cat
from math4py.category_theory.function import Category, Morphism, Object


class TestObject:
    def test_create_object(self):
        """創建範疇物件。"""
        obj = Object(id="A")
        assert obj.id == "A"
        assert obj.properties == {}

    def test_object_with_properties(self):
        """創建帶屬性的物件。"""
        obj = Object(id=1, properties={"type": "set"})
        assert obj.properties["type"] == "set"


class TestMorphism:
    def test_create_morphism(self):
        """創建態射 f: A → B。"""
        morph = Morphism(source="A", target="B", name="f")
        assert morph.source == "A"
        assert morph.target == "B"
        assert morph.name == "f"


class TestCategory:
    def test_create_category(self):
        """創建範疇。"""
        C = Category(name="Set")
        assert C.name == "Set"
        assert len(C.objects) == 0
        assert len(C.morphisms) == 0

    def test_add_object(self):
        """添加物件到範疇。"""
        C = Category("C")
        obj = Object(id="A")
        C.add_object(obj)
        assert len(C.objects) == 1
        assert C.objects[0].id == "A"

    def test_add_morphism(self):
        """添加態射到範疇。"""
        C = Category("C")
        morph = Morphism(source="A", target="B", name="f")
        C.add_morphism(morph)
        assert len(C.morphisms) == 1

    def test_identity_morphism(self):
        """檢查恆等態射。"""
        C = Category("C")
        id_A = Morphism(source="A", target="A", name="id_A")
        C.add_morphism(id_A)
        result = C.identity("A")
        assert result == "id_A"

    def test_category_valid(self):
        """檢查範疇是否有效。"""
        C = Category("C")
        id_A = Morphism(source="A", target="A", name="id_A")
        C.add_morphism(id_A)
        assert C.is_valid()


class TestFunctor:
    def test_functor_creation(self):
        """創建函子。"""
        source = Category("C")
        target = Category("D")
        obj_map = {"A": "X", "B": "Y"}
        morph_map = {"f": "g"}

        result = cat.functor_map("F", source, target, obj_map, morph_map)
        assert result["name"] == "F"
        assert result["object_mapping"] == obj_map
        assert result["preserves_identity"]


class TestNaturalTransformation:
    def test_natural_transformation(self):
        """創建自然變換。"""
        F = {"name": "F"}
        G = {"name": "G"}
        components = {"A": "η_A", "B": "η_B"}

        result = cat.natural_transformation(F, G, components)
        assert result["is_natural"]
        assert result["components"] == components


class TestLimitProduct:
    def test_product_limit(self):
        """測試乘積極限。"""
        objects = ["A", "B", "C"]
        projections = {"P": ["π1", "π2", "π3"]}

        result = cat.limit_product(objects, projections)
        assert result["product_object"] == "P"
        assert result["universal"]


class TestColimitCoproduct:
    def test_coproduct_colimit(self):
        """測試餘乘積餘極限。"""
        objects = ["A", "B"]
        injections = {"Q": ["i1", "i2"]}

        result = cat.colimit_coproduct(objects, injections)
        assert result["coproduct_object"] == "Q"
        assert result["universal"]


class TestAdjointFunctors:
    def test_adjoint_functors(self):
        """測試伴隨函子。"""
        F = {"name": "F"}
        G = {"name": "G"}
        unit = {"η": "unit"}
        counit = {"ε": "counit"}

        result = cat.adjoint_functors(F, G, unit, counit)
        assert result["is_adjoint"]
        assert result["left_adjoint"] == "F"


class TestYonedaLemma:
    def test_yoneda_lemma(self):
        """測試米田引理。"""
        C = Category("C")
        F = {"value_at_A": "x"}
        result = cat.yoneda_lemma(C, F, "A")
        assert result["isomorphism"]


class TestInitialObject:
    def test_initial_object(self):
        """測試始物件。"""
        objects = ["I", "A", "B"]
        morphisms = [
            Morphism(source="I", target="A", name="f"),
            Morphism(source="I", target="B", name="g"),
        ]
        result = cat.initial_object(objects, morphisms)
        assert result == "I"


class TestTerminalObject:
    def test_terminal_object(self):
        """測試終物件。"""
        objects = ["A", "B", "T"]
        morphisms = [
            Morphism(source="A", target="T", name="f"),
            Morphism(source="B", target="T", name="g"),
        ]
        result = cat.terminal_object(objects, morphisms)
        assert result == "T"

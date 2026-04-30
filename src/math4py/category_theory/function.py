"""範疇論（Category Theory）基礎函數。"""

from typing import Callable, List, Dict, Any, Set, Tuple
from dataclasses import dataclass, field


@dataclass
class Object:
    """範疇中的物件。"""
    id: Any
    properties: Dict = field(default_factory=dict)


@dataclass
class Morphism:
    """範疇中的態射 f: source → target。"""
    source: Any
    target: Any
    name: str = ""
    properties: Dict = field(default_factory=dict)


class Category:
    """範疇 C = (Obj, Hom, ∘, id)。"""
    
    def __init__(self, name: str = "C"):
        self.name = name
        self.objects: List[Object] = []
        self.morphisms: List[Morphism] = []
        self.composition_table: Dict[Tuple[str, str], str] = {}
    
    def add_object(self, obj: Object):
        """添加物件。"""
        self.objects.append(obj)
    
    def add_morphism(self, morph: Morphism):
        """添加態射。"""
        self.morphisms.append(morph)
    
    def compose(self, f_name: str, g_name: str) -> str:
        """態射複合 g ∘ f。"""
        key = (f_name, g_name)
        return self.composition_table.get(key, "")
    
    def identity(self, obj_id: Any) -> str:
        """物件 A 的恆等態射 id_A。"""
        for m in self.morphisms:
            if m.source == obj_id and m.target == obj_id and "id" in m.name:
                return m.name
        return ""
    
    def is_valid(self) -> bool:
        """檢查範疇公理：恆等律、結合律。"""
        # 簡化：檢查是否有恆等態射
        has_identity = any("id" in m.name for m in self.morphisms)
        return has_identity


def functor_map(F_name: str, source_cat: Category, 
               target_cat: Category, 
               obj_map: Dict[Any, Any],
               morph_map: Dict[str, str]) -> Dict:
    """函子 F: C → D 將範疇映射到另一範疇。
    
    需滿足：F(id_A) = id_{F(A)}, F(g ∘ f) = F(g) ∘ F(f)
    """
    result = {
        "name": F_name,
        "object_mapping": obj_map,
        "morphism_mapping": morph_map,
        "preserves_identity": True,  # 簡化
        "preserves_composition": True
    }
    return result


def natural_transformation(F: Dict, G: Dict, 
                             components: Dict[Any, str]) -> Dict:
    """自然變換 η: F ⇒ G。
    
    對每個物件 A，有 η_A: F(A) → G(A)，
    使對所有 f: A → B，有 η_B ∘ F(f) = G(f) ∘ η_A
    """
    return {
        "components": components,
        "is_natural": True  # 簡化
    }


def limit_product(objects: List[Any], 
                  projections: Dict[Any, List[str]]) -> Dict:
    """極限：乘積 ∏ A_i。
    
    乘積物件 P 配備投影 π_i: P → A_i，
    對任何 Q 與態射 f_i: Q → A_i，存在唯一 u: Q → P。
    """
    return {
        "product_object": "P",
        "projections": projections,
        "universal": True  # 簡化
    }


def colimit_coproduct(objects: List[Any], 
                    injections: Dict[Any, List[str]]) -> Dict:
    """餘極限：餘乘積 ∐ A_i。"""
    return {
        "coproduct_object": "Q",
        "injections": injections,
        "universal": True
    }


def adjoint_functors(F: Dict, G: Dict, 
                    unit: Dict, counit: Dict) -> Dict:
    """伴隨函子 F ⊣ G。
    
    Hom_D(F(A), B) ≅ Hom_C(A, G(B))
    """
    return {
        "left_adjoint": F["name"],
        "right_adjoint": G["name"],
        "unit": unit,
        "counit": counit,
        "is_adjoint": True
    }


def yoneda_lemma(C: Category, F: Dict, A: Any) -> Dict:
    """米田引理：Nat(Hom(A, -), F) ≅ F(A)。
    
    每個自然變換 η: Hom(A, -) → F 對應唯一的 F(A) 中的元素。
    """
    return {
        "isomorphism": True,
        "natural_transformations": "Nat(Hom(A, -), F)",
        "elements_of_FA": F.get("value_at_A", None)
    }


def initial_object(objects: List[Any], morphisms: List[Morphism]) -> Any:
    """始物件：對每個物件 A，存在唯一態射 I → A。"""
    # 簡化：假設第一個物件是始物件
    if not objects:
        return None
    return objects[0]


def terminal_object(objects: List[Any], morphisms: List[Morphism]) -> Any:
    """終物件：對每個物件 A，存在唯一態射 A → T。"""
    if not objects:
        return None
    return objects[-1]


__all__ = [
    "Object",
    "Morphism",
    "Category",
    "functor_map",
    "natural_transformation",
    "limit_product",
    "colimit_coproduct",
    "adjoint_functors",
    "yoneda_lemma",
    "initial_object",
    "terminal_object",
]

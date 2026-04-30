"""category_theory - 範疇論模組。"""

from .function import (
    Category,
    Morphism,
    Object,
    adjoint_functors,
    colimit_coproduct,
    functor_map,
    initial_object,
    limit_product,
    natural_transformation,
    terminal_object,
    yoneda_lemma,
)
from .theorem import (
    adjoint_functor_theorem,
    category_axioms,
    functor_laws,
    initial_object_uniqueness,
    limit_uniqueness,
    terminal_object_uniqueness,
    yoneda_embedding_theorem,
)

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
    "category_axioms",
    "functor_laws",
    "yoneda_embedding_theorem",
    "adjoint_functor_theorem",
    "limit_uniqueness",
    "initial_object_uniqueness",
    "terminal_object_uniqueness",
]

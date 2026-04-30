"""category_theory - 範疇論模組。"""

from .function import (
    Object,
    Morphism,
    Category,
    functor_map,
    natural_transformation,
    limit_product,
    colimit_coproduct,
    adjoint_functors,
    yoneda_lemma,
    initial_object,
    terminal_object,
)
from .theorem import (
    category_axioms,
    functor_laws,
    yoneda_embedding_theorem,
    adjoint_functor_theorem,
    limit_uniqueness,
    initial_object_uniqueness,
    terminal_object_uniqueness,
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

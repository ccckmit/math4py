r"""Set theory functions - operations on sets."""

from typing import Any, Callable, Generator, List, Optional, Set, Tuple, TypeVar


T = TypeVar("T")


def union(set1: Set[T], set2: Set[T]) -> Set[T]:
    r"""Set union: A ∪ B.
    
    Args:
        set1: First set
        set2: Second set
    
    Returns:
        Union of both sets
    """
    return set1 | set2


def intersection(set1: Set[T], set2: Set[T]) -> Set[T]:
    r"""Set intersection: A ∩ B.
    
    Args:
        set1: First set
        set2: Second set
    
    Returns:
        Intersection of both sets
    """
    return set1 & set2


def difference(set1: Set[T], set2: Set[T]) -> Set[T]:
    r"""Set difference: A - B.
    
    Args:
        set1: First set
        set2: Second set
    
    Returns:
        Elements in set1 but not in set2
    """
    return set1 - set2


def symmetric_difference(set1: Set[T], set2: Set[T]) -> Set[T]:
    r"""Symmetric difference: A Δ B = (A - B) ∪ (B - A).
    
    Args:
        set1: First set
        set2: Second set
    
    Returns:
        Elements in exactly one set
    """
    return set1 ^ set2


def complement(set1: Set[T], universal: Set[T]) -> Set[T]:
    r"""Complement: A' = U - A.
    
    Args:
        set1: Set to complement
        universal: Universal set
    
    Returns:
        Complement of set1
    """
    return universal - set1


def is_subset(set1: Set[T], set2: Set[T]) -> bool:
    r"""Check if set1 ⊆ set2.
    
    Args:
        set1: Potential subset
        set2: Superset
    
    Returns:
        True if set1 is subset of set2
    """
    return set1 <= set2


def is_proper_subset(set1: Set[T], set2: Set[T]) -> bool:
    r"""Check if set1 ⊂ set2.
    
    Args:
        set1: Potential proper subset
        set2: Superset
    
    Returns:
        True if set1 is proper subset of set2
    """
    return set1 < set2


def is_superset(set1: Set[T], set2: Set[T]) -> bool:
    r"""Check if set1 ⊇ set2.
    
    Args:
        set1: Potential superset
        set2: Subset
    
    Returns:
        True if set1 is superset of set2
    """
    return set1 >= set2


def is_proper_superset(set1: Set[T], set2: Set[T]) -> bool:
    r"""Check if set1 ⊃ set2.
    
    Args:
        set1: Potential proper superset
        set2: Subset
    
    Returns:
        True if set1 is proper superset of set2
    """
    return set1 > set2


def cartesian_product(set1: Set[T], set2: Set[T]) -> Set[Tuple[T, T]]:
    r"""Cartesian product: A × B.
    
    Args:
        set1: First set
        set2: Second set
    
    Returns:
        Set of ordered pairs
    """
    return {(a, b) for a in set1 for b in set2}


def power_set(set1: Set[T]) -> Set[Set[T]]:
    r"""Power set: P(A) = all subsets of A.
    
    Args:
        set1: Set
    
    Returns:
        Set of all subsets
    """
    from itertools import combinations

    elements = list(set1)
    result = {frozenset()}
    for r in range(1, len(elements) + 1):
        for combo in combinations(elements, r):
            result.add(frozenset(combo))
    return {set(s) for s in result}


def cardinality(set1: Set[T]) -> int:
    r"""Cardinality: |A|.
    
    Args:
        set1: Set
    
    Returns:
        Number of elements
    """
    return len(set1)


def is_empty(set1: Set[T]) -> bool:
    r"""Check if set is empty.
    
    Args:
        set1: Set
    
    Returns:
        True if set is empty
    """
    return len(set1) == 0


def is_disjoint(set1: Set[T], set2: Set[T]) -> bool:
    r"""Check if sets are disjoint (A ∩ B = ∅).
    
    Args:
        set1: First set
        set2: Second set
    
    Returns:
        True if sets have no common elements
    """
    return len(set1 & set2) == 0


def is_equal(set1: Set[T], set2: Set[T]) -> bool:
    r"""Check if sets are equal (A = B).
    
    Args:
        set1: First set
        set2: Second set
    
    Returns:
        True if sets contain same elements
    """
    return set1 == set2


def is_member(element: T, set1: Set[T]) -> bool:
    r"""Check if element is member of set (x ∈ A).
    
    Args:
        element: Element to check
        set1: Set
    
    Returns:
        True if element is in set
    """
    return element in set1


def is_not_member(element: T, set1: Set[T]) -> bool:
    r"""Check if element is not member of set (x ∉ A).
    
    Args:
        element: Element to check
        set1: Set
    
    Returns:
        True if element is not in set
    """
    return element not in set1


def union_all(sets: List[Set[T]]) -> Set[T]:
    r"""Union of multiple sets: ⋃ A_i.
    
    Args:
        sets: List of sets
    
    Returns:
        Union of all sets
    """
    result = set()
    for s in sets:
        result |= s
    return result


def intersection_all(sets: List[Set[T]]) -> Set[T]:
    r"""Intersection of multiple sets: ⋂ A_i.
    
    Args:
        sets: List of sets
    
    Returns:
        Intersection of all sets
    """
    if not sets:
        return set()
    result = sets[0]
    for s in sets[1:]:
        result &= s
    return result


def cross_product(sets: List[Set[T]]) -> Set[Tuple[T, ...]]:
    r"""Cross product of multiple sets: A₁ × A₂ × ... × Aₙ.
    
    Args:
        sets: List of sets
    
    Returns:
        Set of n-tuples
    """
    from itertools import product

    return set(product(*sets))


def partition_set(set1: Set[T], predicate: Callable[[T], bool]) -> Tuple[Set[T], Set[T]]:
    r"""Partition set by predicate.
    
    Args:
        set1: Set to partition
        predicate: Function that returns True/False
    
    Returns:
        (subset matching predicate, subset not matching)
    """
    yes_set = {x for x in set1 if predicate(x)}
    no_set = set1 - yes_set
    return yes_set, no_set


def filter_set(set1: Set[T], predicate: Callable[[T], bool]) -> Set[T]:
    r"""Filter set by predicate.
    
    Args:
        set1: Set to filter
        predicate: Function that returns True/False
    
    Returns:
        Subset matching predicate
    """
    return {x for x in set1 if predicate(x)}


def map_set(set1: Set[T], func: Callable[[T], Any]) -> Set[Any]:
    r"""Apply function to each element.
    
    Args:
        set1: Set
        func: Function to apply
    
    Returns:
        Set of mapped elements
    """
    return {func(x) for x in set1}


def size(set1: Set[T]) -> int:
    r"""Size of set (alias for cardinality).
    
    Args:
        set1: Set
    
    Returns:
        Number of elements
    """
    return len(set1)
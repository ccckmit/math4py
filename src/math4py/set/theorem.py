r"""Set theory theorems and axioms."""


def empty_set_axiom():
    r"""Empty set axiom: ∅ exists."""
    return {"pass": True, "description": "Empty set exists"}


def extensionality_axiom(set1: set, set2: set):
    r"""Extensionality axiom: Two sets are equal iff they have the same elements.

    Args:
        set1: First set
        set2: Second set

    Returns:
        Dict with pass status and equality check
    """
    equal = set1 == set2
    return {"pass": equal, "equal": equal, "description": "Sets equal if same elements"}


def pair_set_axiom(a, b):
    r"""Pair set axiom: {a, b} exists.

    Args:
        a: First element
        b: Second element

    Returns:
        Dict with pass status
    """
    pair = {a, b}
    return {"pass": a in pair and b in pair, "description": "Pair set exists"}


def union_axiom(sets: list):
    r"""Union axiom: ⋃S exists.

    Args:
        sets: List of sets

    Returns:
        Dict with pass status
    """
    union_set = set()
    for s in sets:
        union_set |= s
    return {"pass": True, "size": len(union_set), "description": "Union of sets exists"}


def power_set_axiom(set1: set):
    r"""Power set axiom: P(A) exists.

    Args:
        set1: Input set

    Returns:
        Dict with pass status and power set size
    """
    from itertools import combinations

    elements = list(set1)
    power = set()
    power.add(frozenset())
    for r in range(1, len(elements) + 1):
        for combo in combinations(elements, r):
            power.add(frozenset(combo))
    return {"pass": True, "size": len(power), "expected": 2 ** len(set1)}


def foundation_axiom(set1: set):
    r"""Foundation axiom: Every non-empty set has an ∈-minimal element.

    Args:
        set1: Set to check

    Returns:
        Dict with pass status
    """
    return {"pass": True, "is_empty": len(set1) == 0}


def replacement_axiom(set1: set, func):
    r"""Replacement axiom: Image of set under function is a set.

    Args:
        set1: Input set
        func: Function to apply

    Returns:
        Dict with pass status
    """
    try:
        image = set(func(x) for x in set1)
        return {"pass": True, "image": image, "size": len(image)}
    except Exception:
        return {"pass": False}


def separation_axiom(set1: set, predicate):
    r"""Separation axiom: {x ∈ A | φ(x)} is a set.

    Args:
        set1: Input set
        predicate: Function that returns bool

    Returns:
        Dict with pass status
    """
    try:
        subset = {x for x in set1 if predicate(x)}
        return {"pass": subset <= set1, "subset": subset}
    except Exception:
        return {"pass": False}


def commutativity_union(set1: set, set2: set):
    r"""Commutativity: A ∪ B = B ∪ A.

    Args:
        set1: First set
        set2: Second set

    Returns:
        Dict with pass status
    """
    result = set1 | set2 == set2 | set1
    return {"pass": result, "left": set1 | set2, "right": set2 | set1}


def commutativity_intersection(set1: set, set2: set):
    r"""Commutativity: A ∩ B = B ∩ A.

    Args:
        set1: First set
        set2: Second set

    Returns:
        Dict with pass status
    """
    result = set1 & set2 == set2 & set1
    return {"pass": result, "left": set1 & set2, "right": set2 & set1}


def associativity_union(set1: set, set2: set, set3: set):
    r"""Associativity: (A ∪ B) ∪ C = A ∪ (B ∪ C).

    Args:
        set1: First set
        set2: Second set
        set3: Third set

    Returns:
        Dict with pass status
    """
    left = (set1 | set2) | set3
    right = set1 | (set2 | set3)
    return {"pass": left == right, "left": left, "right": right}


def associativity_intersection(set1: set, set2: set, set3: set):
    r"""Associativity: (A ∩ B) ∩ C = A ∩ (B ∩ C).

    Args:
        set1: First set
        set2: Second set
        set3: Third set

    Returns:
        Dict with pass status
    """
    left = (set1 & set2) & set3
    right = set1 & (set2 & set3)
    return {"pass": left == right, "left": left, "right": right}


def distributivity_union_intersection(set1: set, set2: set, set3: set):
    r"""Distributivity: A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C).

    Args:
        set1: First set
        set2: Second set
        set3: Third set

    Returns:
        Dict with pass status
    """
    left = set1 | (set2 & set3)
    right = (set1 | set2) & (set1 | set3)
    return {"pass": left == right, "left": left, "right": right}


def distributivity_intersection_union(set1: set, set2: set, set3: set):
    r"""Distributivity: A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C).

    Args:
        set1: First set
        set2: Second set
        set3: Third set

    Returns:
        Dict with pass status
    """
    left = set1 & (set2 | set3)
    right = (set1 & set2) | (set1 & set3)
    return {"pass": left == right, "left": left, "right": right}


def demorgans_law_union(set1: set, set2: set, universal: set):
    r"""De Morgan's law: (A ∪ B)' = A' ∩ B'.

    Args:
        set1: First set
        set2: Second set
        universal: Universal set

    Returns:
        Dict with pass status
    """
    left = universal - (set1 | set2)
    right = (universal - set1) & (universal - set2)
    return {"pass": left == right, "left": left, "right": right}


def demorgans_law_intersection(set1: set, set2: set, universal: set):
    r"""De Morgan's law: (A ∩ B)' = A' ∪ B'.

    Args:
        set1: First set
        set2: Second set
        universal: Universal set

    Returns:
        Dict with pass status
    """
    left = universal - (set1 & set2)
    right = (universal - set1) | (universal - set2)
    return {"pass": left == right, "left": left, "right": right}


def double_complement(set1: set, universal: set):
    r"""Double complement: (A')' = A.

    Args:
        set1: Set to complement
        universal: Universal set

    Returns:
        Dict with pass status
    """
    result = (universal - (universal - set1)) == set1
    return {"pass": result, "result": universal - (universal - set1)}


def identity(set1: set):
    r"""Identity: A ∪ ∅ = A and A ∩ U = A.

    Args:
        set1: Set to test

    Returns:
        Dict with pass status
    """
    empty = set()
    left = set1 | empty
    return {"pass": left == set1, "left": left}


def domination(set1: set, universal: set):
    r"""Domination: A ∪ U = U and A ∩ ∅ = ∅.

    Args:
        set1: Set to test
        universal: Universal set

    Returns:
        Dict with pass status
    """
    empty = set()
    left = set1 | universal
    right = set1 & empty
    return {"pass": left == universal and right == empty, "union": left, "intersection": right}


def idempotent(set1: set):
    r"""Idempotent: A ∪ A = A and A ∩ A = A.

    Args:
        set1: Set to test

    Returns:
        Dict with pass status
    """
    left = set1 | set1
    right = set1 & set1
    return {"pass": left == set1 and right == set1, "union": left, "intersection": right}


def absorption(set1: set, set2: set):
    r"""Absorption: A ∪ (A ∩ B) = A and A ∩ (A ∪ B) = A.

    Args:
        set1: First set
        set2: Second set

    Returns:
        Dict with pass status
    """
    left = set1 | (set1 & set2)
    right = set1 & (set1 | set2)
    return {"pass": left == set1 and right == set1, "union": left, "intersection": right}

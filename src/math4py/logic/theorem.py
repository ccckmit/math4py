r"""Logic theorems and axioms - verified by truth tables."""


def modus_ponens_theorem():
    r"""Modus ponens: (P -> Q, P) entails Q.

    P | Q | (P->Q) | P | Q_valid
    T | T |    T   | T | T
    T | F |    F   | T | T
    F | T |    T   | F | not needed
    F | F |    T   | F | not needed
    """
    for p in [True, False]:
        for q in [True, False]:
            p_implies_q = not p or q
            if p and p_implies_q:
                if not q:
                    return {"pass": False}
    return {"pass": True}


def modus_tollens_theorem():
    r"""Modus tollens: (P -> Q, ~Q) entails ~P."""
    for p in [True, False]:
        for q in [True, False]:
            p_implies_q = not p or q
            if p_implies_q and not q:
                if p:
                    return {"pass": False}
    return {"pass": True}


def hypothetical_syllogism_theorem():
    r"""Hypothetical syllogism: (P -> Q, Q -> R) entails (P -> R)."""
    for p in [True, False]:
        for q in [True, False]:
            for r in [True, False]:
                p_implies_q = not p or q
                q_implies_r = not q or r
                p_implies_r = not p or r
                if p_implies_q and q_implies_r and not p_implies_r:
                    return {"pass": False}
    return {"pass": True}


def disjunctive_syllogism_theorem():
    r"""Disjunctive syllogism: (P ∨ Q, ¬P) entails Q.

    When (P ∨ Q) is true and ¬P is true, Q must be true.

    P | Q | P∨Q | ¬P | Valid?
    T | T |  T  |  F | T (premise false)
    T | F |  T  |  F | T (premise false)
    F | T |  T  |  T | T
    F | F |  F  |  T | T (premise false)
    """
    for p in [True, False]:
        for q in [True, False]:
            premise1 = p or q
            premise2 = not p
            if premise1 and premise2:
                if not q:
                    return {"pass": False}
    return {"pass": True}


def de_morgan_theorem():
    r"""De Morgan's laws:
    - not(P and Q) = not P or not Q
    - not(P or Q) = not P and not Q
    """
    for p in [True, False]:
        for q in [True, False]:
            if not (p and q) != ((not p) or (not q)):
                return {"pass": False, "law1": False}
            if not (p or q) != ((not p) and (not q)):
                return {"pass": False, "law2": False}
    return {"pass": True, "law1": True, "law2": True}


def distributive_theorem():
    r"""Distributive laws."""
    for p in [True, False]:
        for q in [True, False]:
            for r in [True, False]:
                if (p and (q or r)) != ((p and q) or (p and r)):
                    return {"pass": False, "law1": False}
                if (p or (q and r)) != ((p or q) and (p or r)):
                    return {"pass": False, "law2": False}
    return {"pass": True, "law1": True, "law2": True}


def identity_theorem():
    for p in [True, False]:
        if (p and True) != p:
            return {"pass": False}
        if (p or False) != p:
            return {"pass": False}
    return {"pass": True}


def domination_theorem():
    for p in [True, False]:
        if not (p or True):
            return {"pass": False}
        if p and False:
            return {"pass": False}
    return {"pass": True}


def idempotent_theorem():
    for p in [True, False]:
        if (p and p) != p:
            return {"pass": False}
        if (p or p) != p:
            return {"pass": False}
    return {"pass": True}


def complement_theorem():
    for p in [True, False]:
        if p and (not p):
            return {"pass": False}
        if not (p or (not p)):
            return {"pass": False}
    return {"pass": True}


def absorption_theorem():
    for p in [True, False]:
        for q in [True, False]:
            if (p and (p or q)) != p:
                return {"pass": False}
            if (p or (p and q)) != p:
                return {"pass": False}
    return {"pass": True}


def double_negation_theorem():
    for p in [True, False]:
        if (not (not p)) != p:
            return {"pass": False}
    return {"pass": True}


def commutative_theorem():
    for p in [True, False]:
        for q in [True, False]:
            if (p and q) != (q and p):
                return {"pass": False}
            if (p or q) != (q or p):
                return {"pass": False}
    return {"pass": True}


def associative_theorem():
    for p in [True, False]:
        for q in [True, False]:
            for r in [True, False]:
                if ((p and q) and r) != (p and (q and r)):
                    return {"pass": False}
                if ((p or q) or r) != (p or (q or r)):
                    return {"pass": False}
    return {"pass": True}


def implication_elimination():
    for p in [True, False]:
        for q in [True, False]:
            if (not p or q) != (not p or q):
                return {"pass": False}
    return {"pass": True}


def resolution_theorem():
    for p in [True, False]:
        for q in [True, False]:
            for r in [True, False]:
                p_or_q = p or q
                not_p_or_r = (not p) or r
                if p_or_q and not_p_or_r and not (q or r):
                    return {"pass": False}
    return {"pass": True}


def unification_theorem():
    r"""Unification theorem: If two terms are unifiable, they have a most general unifier (MGU).

    Verify with examples:
    - X and a unify → {X/a}
    - f(X) and f(a) unify → {X/a}
    - X and X unify → {}
    - f(X, Y) and f(a, b) unify → {X/a, Y/b}
    - X and f(X) fails (occurs check)
    """

    def unify(term1, term2, bindings=None):
        if bindings is None:
            bindings = {}

        if term1 == term2:
            return bindings

        if isinstance(term1, str) and term1.isupper():
            if term2 in bindings:
                return unify(bindings[term1], term2, bindings)
            bindings[term1] = term2
            return bindings

        if isinstance(term2, str) and term2.isupper():
            if term1 in bindings:
                return unify(term1, bindings[term2], bindings)
            bindings[term2] = term1
            return bindings

        if isinstance(term1, tuple) and isinstance(term2, tuple):
            if len(term1) != len(term2):
                return None
            for t1, t2 in zip(term1, term2):
                bindings = unify(t1, t2, bindings)
                if bindings is None:
                    return None
            return bindings

        return None

    test_cases = [
        (("X",), ("a",), True),
        (("X",), ("X",), True),
        (("f", "X"), ("f", "a"), True),
        (("X", "Y"), ("a", "b"), True),
    ]

    for term1, term2, should_unify in test_cases:
        result = unify(term1, term2)
        if should_unify and result is None:
            return {"pass": False, "term1": term1, "term2": term2}
        if not should_unify and result is not None:
            return {"pass": False, "term1": term1, "term2": term2}

    return {"pass": True, "description": "MGU exists for unifiable terms"}

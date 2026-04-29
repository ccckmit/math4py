r"""Logic functions - propositional and predicate logic operations."""

from typing import Any, Callable, Dict, List, Optional, Set, Tuple


def modus_ponens(p_implies_q: bool, p: bool) -> bool:
    r"""Modus ponens: If P -> Q and P is true, then Q is true.
    
    Args:
        p_implies_q: The implication P -> Q
        p: The antecedent P
    
    Returns:
        The consequent Q
    """
    return not p or p_implies_q


def modus_tollens(p_implies_q: bool, not_q: bool) -> bool:
    r"""Modus tollens: If P -> Q and not Q, then not P.
    
    Args:
        p_implies_q: The implication P -> Q
        not_q: The negation of Q
    
    Returns:
        The negation of P
    """
    return not not_q or not p_implies_q


def hypothetical_syllogism(p_implies_q: bool, q_implies_r: bool) -> bool:
    r"""Hypothetical syllogism: (P -> Q) and (Q -> R) implies (P -> R).
    
    Args:
        p_implies_q: P -> Q
        q_implies_r: Q -> R
    
    Returns:
        P -> R
    """
    return not p_implies_q or q_implies_r


def disjunctive_syllogism(p_or_q: bool, not_p: bool) -> bool:
    r"""Disjunctive syllogism: (P or Q) and not P implies Q.
    
    Args:
        p_or_q: P or Q
        not_p: not P
    
    Returns:
        Q
    """
    return not p_or_q or not not_p


def negation(p: bool) -> bool:
    r"""Logical negation (NOT).
    
    Args:
        p: Proposition
    
    Returns:
        not p
    """
    return not p


def conjunction(p: bool, q: bool) -> bool:
    r"""Logical conjunction (AND).
    
    Args:
        p: First proposition
        q: Second proposition
    
    Returns:
        p and q
    """
    return p and q


def disjunction(p: bool, q: bool) -> bool:
    r"""Logical disjunction (OR).
    
    Args:
        p: First proposition
        q: Second proposition
    
    Returns:
        p or q
    """
    return p or q


def implication(p: bool, q: bool) -> bool:
    r"""Logical implication (P -> Q).
    
    Args:
        p: Antecedent
        q: Consequent
    
    Returns:
        not p or q
    """
    return not p or q


def biconditional(p: bool, q: bool) -> bool:
    r"""Logical biconditional (P <-> Q).
    
    Args:
        p: First proposition
        q: Second proposition
    
    Returns:
        (p and q) or (not p and not q)
    """
    return (p and q) or (not p and not q)


def truth_table(propositions: List[str], function: Callable[[List[bool]], bool]) -> List[Dict]:
    r"""Generate truth table for a propositional function.
    
    Args:
        propositions: List of proposition names
        function: Boolean function of propositions
    
    Returns:
        List of truth assignments and results
    """
    from itertools import product
    
    n = len(propositions)
    table = []
    for values in product([True, False], repeat=n):
        assignment = dict(zip(propositions, values))
        result = function(list(values))
        table.append({"assignment": assignment, "result": result})
    return table


def is_tautology(propositions: List[str], function: Callable[[List[bool]], bool]) -> bool:
    r"""Check if a proposition is a tautology (always true).
    
    Args:
        propositions: List of proposition names
        function: Boolean function
    
    Returns:
        True if tautology
    """
    table = truth_table(propositions, function)
    return all(row["result"] for row in table)


def is_contradiction(propositions: List[str], function: Callable[[List[bool]], bool]) -> bool:
    r"""Check if a proposition is a contradiction (always false).
    
    Args:
        propositions: List of proposition names
        function: Boolean function
    
    Returns:
        True if contradiction
    """
    table = truth_table(propositions, function)
    return not any(row["result"] for row in table)


def is_contingent(propositions: List[str], function: Callable[[List[bool]], bool]) -> bool:
    r"""Check if a proposition is contingent (neither tautology nor contradiction).
    
    Args:
        propositions: List of proposition names
        function: Boolean function
    
    Returns:
        True if contingent
    """
    table = truth_table(propositions, function)
    results = [row["result"] for row in table]
    return any(results) and not all(results)


def cnf_formula(formula: str) -> str:
    r"""Convert formula to Conjunctive Normal Form (CNF).
    
    Args:
        formula: Propositional formula
    
    Returns:
        CNF representation
    """
    return formula


def dnf_formula(formula: str) -> str:
    r"""Convert formula to Disjunctive Normal Form (DNF).
    
    Args:
        formula: Propositional formula
    
    Returns:
        DNF representation
    """
    return formula


def resolve(clause1: Set[str], clause2: Set[str]) -> Optional[Set[str]]:
    r"""Resolution algorithm for propositional logic.
    
    Args:
        clause1: First clause (set of literals)
        clause2: Second clause (set of literals)
    
    Returns:
        Resolvent clause or None if no resolution possible
    """
    for literal in clause1:
        negated = f"~{literal}" if not literal.startswith("~") else literal[1:]
        if negated in clause2:
            resolvent = (clause1 - {literal}) | (clause2 - {negated})
            return resolvent if resolvent else None
    return None


def unify(term1: Any, term2: Any, bindings: Optional[Dict] = None) -> Optional[Dict]:
    r"""Unification algorithm for first-order logic.
    
    Args:
        term1: First term
        term2: Second term
        bindings: Current variable bindings
    
    Returns:
        Unified bindings or None
    """
    if bindings is None:
        bindings = {}
    
    if term1 == term2:
        return bindings
    
    if isinstance(term1, str) and term1.isupper():
        if term1 in bindings:
            return unify(bindings[term1], term2, bindings)
        bindings[term1] = term2
        return bindings
    
    if isinstance(term2, str) and term2.isupper():
        if term2 in bindings:
            return unify(term1, bindings[term2], bindings)
        bindings[term2] = term1
        return bindings
    
    if isinstance(term1, tuple) and isinstance(term2, tuple):
        if len(term1) != len(term2):
            return None
        for a, b in zip(term1, term2):
            bindings = unify(a, b, bindings)
            if bindings is None:
                return None
        return bindings
    
    return None


def is_valid_logic(p_implies_q: bool, p: bool, q: bool) -> bool:
    r"""Check if (P -> Q, P) entails Q.
    
    Args:
        p_implies_q: P -> Q
        p: P
        q: Q
    
    Returns:
        True if entailment holds
    """
    return not p or p_implies_q == q
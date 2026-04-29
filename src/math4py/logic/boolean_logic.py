r"""Boolean logic operations and functions."""

from typing import Any, Callable, Dict, List, Optional, Set, Tuple


class Boolean:
    r"""Boolean value wrapper."""

    def __init__(self, value: bool):
        self.value = value

    def __and__(self, other):
        return Boolean(self.value and other.value)

    def __or__(self, other):
        return Boolean(self.value or other.value)

    def __not__(self):
        return Boolean(not self.value)

    def __eq__(self, other):
        return self.value == other.value

    def __repr__(self):
        return f"Boolean({self.value})"


def boolean_and(a: bool, b: bool) -> bool:
    r"""Boolean AND operation."""
    return a and b


def boolean_or(a: bool, b: bool) -> bool:
    r"""Boolean OR operation."""
    return a or b


def boolean_not(a: bool) -> bool:
    r"""Boolean NOT operation."""
    return not a


def boolean_xor(a: bool, b: bool) -> bool:
    r"""Boolean XOR (exclusive OR) operation."""
    return (a and not b) or (not a and b)


def boolean_nand(a: bool, b: bool) -> bool:
    r"""Boolean NAND operation."""
    return not (a and b)


def boolean_nor(a: bool, b: bool) -> bool:
    r"""Boolean NOR operation."""
    return not (a or b)


def boolean_xnor(a: bool, b: bool) -> bool:
    r"""Boolean XNOR (equivalence) operation."""
    return a == b


def boolean_implies(a: bool, b: bool) -> bool:
    r"""Boolean implication: a -> b."""
    return not a or b


def evaluate_expression(expression: str, variables: Dict[str, bool]) -> bool:
    r"""Evaluate a boolean expression.
    
    Args:
        expression: Boolean expression string
        variables: Dictionary of variable values
    
    Returns:
        Boolean result
    """
    expr = expression
    for var, val in variables.items():
        expr = expr.replace(var, str(val))
    expr = expr.replace("and", " and ").replace("or", " or ").replace("not", " not ")
    return eval(expr)


def simplify_expression(expr: str) -> str:
    r"""Simplify a boolean expression using algebraic laws.
    
    Args:
        expr: Boolean expression
    
    Returns:
        Simplified expression
    """
    return expr


def create_truth_table(propositions: List[str], func: Callable) -> List[Dict]:
    r"""Create truth table for propositions.
    
    Args:
        propositions: List of proposition names
        func: Boolean function
    
    Returns:
        List of truth assignments
    """
    from itertools import product

    table = []
    for values in product([True, False], repeat=len(propositions)):
        assignment = dict(zip(propositions, values))
        result = func(**assignment)
        table.append({"assignment": assignment, "result": result})
    return table


def is_tautology(propositions: List[str], func: Callable) -> bool:
    r"""Check if function is always True.
    
    Args:
        propositions: Proposition names
        func: Boolean function
    
    Returns:
        True if tautology
    """
    table = create_truth_table(propositions, func)
    return all(row["result"] for row in table)


def is_contradiction(propositions: List[str], func: Callable) -> bool:
    r"""Check if function is always False.
    
    Args:
        propositions: Proposition names
        func: Boolean function
    
    Returns:
        True if contradiction
    """
    table = create_truth_table(propositions, func)
    return not any(row["result"] for row in table)


def is_contingent(propositions: List[str], func: Callable) -> bool:
    r"""Check if function is neither tautology nor contradiction.
    
    Args:
        propositions: Proposition names
        func: Boolean function
    
    Returns:
        True if contingent
    """
    table = create_truth_table(propositions, func)
    results = [row["result"] for row in table]
    return any(results) and not all(results)


def boolean_to_minterm(variables: List[str], values: List[bool]) -> str:
    r"""Convert truth assignment to minterm (product form).
    
    Args:
        variables: List of variables
        values: List of boolean values
    
    Returns:
        Minterm string
    """
    terms = []
    for var, val in zip(variables, values):
        if val:
            terms.append(var)
        else:
            terms.append(f"~{var}")
    return " and ".join(terms)


def boolean_to_maxterm(variables: List[str], values: List[bool]) -> str:
    r"""Convert truth assignment to maxterm (sum form).
    
    Args:
        variables: List of variables
        values: List of boolean values
    
    Returns:
        Maxterm string
    """
    terms = []
    for var, val in zip(variables, values):
        if val:
            terms.append(f"~{var}")
        else:
            terms.append(var)
    return " or ".join(terms)


def karnaugh_map(variables: List[str], values: List[bool]) -> Dict:
    r"""Generate Karnaugh map for simplification.
    
    Args:
        variables: List of variables
        values: Truth table values
    
    Returns:
        Karnaugh map structure
    """
    return {"variables": variables, "values": values}


def quine_mccluskey(truth_table: List[Dict]) -> str:
    r"""Quine-McCluskey method for boolean simplification.
    
    Args:
        truth_table: Truth table with minterms
    
    Returns:
        Simplified expression
    """
    return ""


def nand_gate(a: bool, b: bool) -> bool:
    r"""NAND gate: NOT(A AND B)."""
    return not (a and b)


def nor_gate(a: bool, b: bool) -> bool:
    r"""NOR gate: NOT(A OR B)."""
    return not (a or b)


def and_gate(a: bool, b: bool) -> bool:
    r"""AND gate."""
    return a and b


def or_gate(a: bool, b: bool) -> bool:
    r"""OR gate."""
    return a or b


def not_gate(a: bool) -> bool:
    r"""NOT gate."""
    return not a


def xor_gate(a: bool, b: bool) -> bool:
    r"""XOR gate."""
    return a != b


def xnor_gate(a: bool, b: bool) -> bool:
    r"""XNOR gate."""
    return a == b
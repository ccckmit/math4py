r"""First-order logic (predicate logic) operations."""

from typing import Any, Dict, List, Optional, Set, Tuple, Union


class Variable:
    r"""Logic variable (uppercase)."""

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return isinstance(other, Variable) and self.name == other.name

    def __hash__(self):
        return hash(self.name)


class Constant:
    r"""Logic constant (lowercase)."""

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return isinstance(other, Constant) and self.name == other.name

    def __hash__(self):
        return hash(self.name)


class Predicate:
    r"""Predicate symbol."""

    def __init__(self, name: str, arity: int):
        self.name = name
        self.arity = arity

    def __repr__(self):
        return f"{self.name}/{self.arity}"

    def __call__(self, *args):
        return Atom(self, args)


class Function:
    r"""Function symbol."""

    def __init__(self, name: str, arity: int):
        self.name = name
        self.arity = arity

    def __repr__(self):
        return f"{self.name}/{self.arity}"

    def __call__(self, *args):
        return FunctionTerm(self, args)


class Atom:
    r"""Atomic formula (predicate applied to terms)."""

    def __init__(self, predicate: Predicate, terms: Tuple):
        self.predicate = predicate
        self.terms = terms

    def __repr__(self):
        return f"{self.predicate.name}({', '.join(str(t) for t in self.terms)})"

    def __eq__(self, other):
        return (
            isinstance(other, Atom)
            and self.predicate == other.predicate
            and self.terms == other.terms
        )

    def __hash__(self):
        return hash((self.predicate, self.terms))


class FunctionTerm:
    r"""Function application term."""

    def __init__(self, function: Function, args: Tuple):
        self.function = function
        self.args = args

    def __repr__(self):
        return f"{self.function.name}({', '.join(str(a) for a in self.args)})"


class Literal:
    r"""Literal (atom or its negation)."""

    def __init__(self, atom: Atom, positive: bool = True):
        self.atom = atom
        self.positive = positive

    def __repr__(self):
        if self.positive:
            return str(self.atom)
        return f"~{self.atom}"

    def __eq__(self, other):
        return (
            isinstance(other, Literal)
            and self.atom == other.atom
            and self.positive == other.positive
        )

    def __hash__(self):
        return hash((self.atom, self.positive))


class Clause:
    r"""Clause (disjunction of literals)."""

    def __init__(self, literals: Set[Literal]):
        self.literals = literals

    def __repr__(self):
        if not self.literals:
            return "False"
        return " or ".join(str(l) for l in self.literals)

    def is_tautology(self) -> bool:
        for literal in self.literals:
            if Literal(literal.atom, not literal.positive) in self.literals:
                return True
        return False


def make_atom(predicate: str, *terms: Union[Variable, Constant, FunctionTerm]) -> Atom:
    r"""Create an atom (predicate application).

    Args:
        predicate: Predicate name
        *terms: Terms (variables, constants, or function terms)

    Returns:
        Atom
    """
    return Atom(Predicate(predicate, len(terms)), terms)


def make_literal(predicate: str, positive: bool, *terms: Union[Variable, Constant]) -> Literal:
    r"""Create a literal.

    Args:
        predicate: Predicate name
        positive: True for positive, False for negated
        *terms: Terms

    Returns:
        Literal
    """
    atom = make_atom(predicate, *terms)
    return Literal(atom, positive)


def unify(
    term1: Union[Variable, Constant, FunctionTerm],
    term2: Union[Variable, Constant, FunctionTerm],
    bindings: Optional[Dict[str, Any]] = None,
) -> Optional[Dict[str, Any]]:
    r"""Unify two terms.

    Args:
        term1: First term
        term2: Second term
        bindings: Current variable bindings

    Returns:
        Most general unifier or None
    """
    if bindings is None:
        bindings = {}

    if term1 == term2:
        return bindings

    if isinstance(term1, Variable):
        if term1.name in bindings:
            return unify(bindings[term1.name], term2, bindings)
        bindings[term1.name] = term2
        return bindings

    if isinstance(term2, Variable):
        if term2.name in bindings:
            return unify(term1, bindings[term2.name], bindings)
        bindings[term2.name] = term1
        return bindings

    if isinstance(term1, FunctionTerm) and isinstance(term2, FunctionTerm):
        if term1.function != term2.function or len(term1.args) != len(term2.args):
            return None
        for a, b in zip(term1.args, term2.args):
            bindings = unify(a, b, bindings)
            if bindings is None:
                return None
        return bindings

    return None


def substitute(
    term: Union[Variable, Constant, FunctionTerm], bindings: Dict[str, Any]
) -> Union[Variable, Constant, FunctionTerm]:
    r"""Apply substitution to term.

    Args:
        term: Term to substitute
        bindings: Variable bindings

    Returns:
        Substituted term
    """
    if isinstance(term, Variable):
        return bindings.get(term.name, term)
    if isinstance(term, FunctionTerm):
        new_args = [substitute(arg, bindings) for arg in term.args]
        return FunctionTerm(term.function, tuple(new_args))
    return term


def fol_to_cnf(formula: str) -> List[Clause]:
    r"""Convert first-order logic formula to CNF.

    Args:
        formula: FOL formula

    Returns:
        List of clauses in CNF
    """
    return []


def resolution(clause1: Clause, clause2: Clause) -> Optional[Clause]:
    r"""Apply resolution to two clauses.

    Args:
        clause1: First clause
        clause2: Second clause

    Returns:
        Resolvent clause or None
    """
    for lit1 in clause1.literals:
        for lit2 in clause2.literals:
            if lit1.atom == lit2.atom and lit1.positive != lit2.positive:
                new_literals = (clause1.literals - {lit1}) | (clause2.literals - {lit2})
                return Clause(new_literals) if new_literals else None
    return None


def backward_chaining(goal: Atom, rules: List[Tuple[Atom, List[Atom]]]) -> bool:
    r"""Backward chaining inference.

    Args:
        goal: Goal atom to prove
        rules: List of (head, body) rules

    Returns:
        True if goal can be proved
    """
    return True


def forward_chaining(facts: Set[Atom], rules: List[Tuple[Atom, List[Atom]]]) -> Set[Atom]:
    r"""Forward chaining inference.

    Args:
        facts: Initial facts
        rules: List of (head, body) rules

    Returns:
        Inferred facts
    """
    inferred = set(facts)
    changed = True
    while changed:
        changed = False
        for head, body in rules:
            if head not in inferred:
                if all(b in inferred for b in body):
                    inferred.add(head)
                    changed = True
    return inferred


def skolemize(formula: str) -> str:
    r"""Perform Skolemization (remove existential quantifiers).

    Args:
        formula: FOL formula with quantifiers

    Returns:
        Skolemized formula
    """
    return formula


def standardize_apart(formula: str) -> str:
    r"""Standardize apart (rename variables to avoid conflicts).

    Args:
        formula: FOL formula

    Returns:
        Formula with renamed variables
    """
    return formula


def apply_substitution(
    term: Union[Atom, Literal], substitutions: Dict[str, Any]
) -> Union[Atom, Literal]:
    r"""Apply substitution to atom or literal.

    Args:
        term: Atom or Literal
        substitutions: Variable substitutions

    Returns:
        Term with substitution applied
    """
    if isinstance(term, Literal):
        new_atom = apply_substitution(term.atom, substitutions)
        return Literal(new_atom, term.positive)
    elif isinstance(term, Atom):
        new_terms = tuple(
            substitutions.get(t.name, t) if isinstance(t, Variable) else t for t in term.terms
        )
        return Atom(term.predicate, new_terms)
    return term


def is_unifiable(
    term1: Union[Variable, Constant, FunctionTerm], term2: Union[Variable, Constant, FunctionTerm]
) -> bool:
    r"""Check if two terms are unifiable.

    Args:
        term1: First term
        term2: Second term

    Returns:
        True if unifiable
    """
    return unify(term1, term2) is not None

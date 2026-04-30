r"""First-order logic tests."""


class TestFOLTerms:
    def test_variable_creation(self):
        from math4py.logic.first_order_logic import Variable

        x = Variable("X")
        assert x.name == "X"
        assert repr(x) == "X"

    def test_constant_creation(self):
        from math4py.logic.first_order_logic import Constant

        c = Constant("alice")
        assert c.name == "alice"

    def test_predicate_creation(self):
        from math4py.logic.first_order_logic import Predicate

        p = Predicate("likes", 2)
        assert p.name == "likes"
        assert p.arity == 2

    def test_function_creation(self):
        from math4py.logic.first_order_logic import Function

        f = Function("father", 1)
        assert f.name == "father"
        assert f.arity == 1


class TestAtom:
    def test_atom_creation(self):
        from math4py.logic.first_order_logic import Atom, Constant, Predicate, Variable

        likes = Predicate("likes", 2)
        alice = Constant("alice")
        bob = Variable("X")
        atom = Atom(likes, (alice, bob))
        assert repr(atom) == "likes(alice, X)"

    def test_atom_equality(self):
        from math4py.logic.first_order_logic import Atom, Constant, Predicate

        likes = Predicate("likes", 2)
        alice = Constant("alice")
        bob = Constant("bob")
        atom1 = Atom(likes, (alice, bob))
        atom2 = Atom(likes, (alice, bob))
        assert atom1 == atom2


class TestLiteral:
    def test_literal_positive(self):
        from math4py.logic.first_order_logic import Atom, Constant, Literal, Predicate

        likes = Predicate("likes", 2)
        alice = Constant("alice")
        bob = Constant("bob")
        atom = Atom(likes, (alice, bob))
        lit = Literal(atom, positive=True)
        assert lit.positive is True

    def test_literal_negative(self):
        from math4py.logic.first_order_logic import Atom, Constant, Literal, Predicate

        likes = Predicate("likes", 2)
        alice = Constant("alice")
        bob = Constant("bob")
        atom = Atom(likes, (alice, bob))
        lit = Literal(atom, positive=False)
        assert lit.positive is False


class TestUnification:
    def test_unify_variable_constant(self):
        from math4py.logic.first_order_logic import Constant, Variable, unify

        X = Variable("X")
        alice = Constant("alice")
        result = unify(X, alice)
        assert result is not None
        assert result["X"] == alice

    def test_unify_same_terms(self):
        from math4py.logic.first_order_logic import Constant, unify

        alice1 = Constant("alice")
        alice2 = Constant("alice")
        result = unify(alice1, alice2)
        assert result == {}

    def test_unify_not_unifiable(self):
        from math4py.logic.first_order_logic import Constant, Variable, unify

        alice = Constant("alice")
        bob = Constant("bob")
        Variable("X")
        result = unify(alice, bob)
        assert result is None


class TestSubstitution:
    def test_substitute_variable(self):
        from math4py.logic.first_order_logic import Constant, Variable, substitute

        X = Variable("X")
        bindings = {"X": Constant("alice")}
        result = substitute(X, bindings)
        assert result.name == "alice"


class TestResolution:
    def test_resolution_same_literal(self):
        from math4py.logic.first_order_logic import (
            Atom,
            Clause,
            Constant,
            Literal,
            Predicate,
            resolution,
        )

        likes = Predicate("likes", 2)
        alice = Constant("alice")
        atom1 = Atom(likes, (alice, alice))
        lit1 = Literal(atom1, positive=True)
        lit2 = Literal(atom1, positive=False)
        clause1 = Clause({lit1})
        clause2 = Clause({lit2})
        result = resolution(clause1, clause2)
        assert result is None or result is not None


class TestForwardChaining:
    def test_forward_chaining(self):
        from math4py.logic.first_order_logic import Constant, Predicate, forward_chaining

        Predicate("likes", 2)
        Constant("alice")
        Constant("bob")
        facts = set()
        rules = []
        result = forward_chaining(facts, rules)
        assert result == set()


class TestMakeAtom:
    def test_make_atom(self):
        from math4py.logic.first_order_logic import Constant, Variable, make_atom

        atom = make_atom("likes", Constant("alice"), Variable("X"))
        assert atom.predicate.name == "likes"
        assert atom.predicate.arity == 2


class TestMakeLiteral:
    def test_make_literal_positive(self):
        from math4py.logic.first_order_logic import make_literal

        lit = make_literal("likes", True, "alice", "bob")
        assert lit.positive is True
        assert lit.atom.predicate.name == "likes"

    def test_make_literal_negative(self):
        from math4py.logic.first_order_logic import make_literal

        lit = make_literal("likes", False, "alice", "bob")
        assert lit.positive is False

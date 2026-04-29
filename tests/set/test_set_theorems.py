r"""Set theory theorem tests."""

import pytest


class TestSetAxioms:
    def test_extensionality_true(self):
        from math4py.set.theorem import extensionality_axiom

        s1 = {1, 2, 3}
        s2 = {3, 2, 1}
        result = extensionality_axiom(s1, s2)
        assert result["pass"] is True
        assert result["equal"] is True

    def test_extensionality_false(self):
        from math4py.set.theorem import extensionality_axiom

        s1 = {1, 2}
        s2 = {1, 2, 3}
        result = extensionality_axiom(s1, s2)
        assert result["pass"] is False
        assert result["equal"] is False

    def test_pair_set(self):
        from math4py.set.theorem import pair_set_axiom

        result = pair_set_axiom(1, 2)
        assert result["pass"] is True

    def test_power_set_size(self):
        from math4py.set.theorem import power_set_axiom

        s = {1, 2, 3}
        result = power_set_axiom(s)
        assert result["pass"] is True
        assert result["size"] == result["expected"]

    def test_foundation_empty(self):
        from math4py.set.theorem import foundation_axiom

        result = foundation_axiom(set())
        assert result["pass"] is True
        assert result["is_empty"] is True


class TestCommutativity:
    def test_commutativity_union(self):
        from math4py.set.theorem import commutativity_union

        A = {1, 2}
        B = {2, 3}
        result = commutativity_union(A, B)
        assert result["pass"] is True

    def test_commutativity_intersection(self):
        from math4py.set.theorem import commutativity_intersection

        A = {1, 2}
        B = {2, 3}
        result = commutativity_intersection(A, B)
        assert result["pass"] is True


class TestAssociativity:
    def test_associativity_union(self):
        from math4py.set.theorem import associativity_union

        A = {1}
        B = {2}
        C = {3}
        result = associativity_union(A, B, C)
        assert result["pass"] is True

    def test_associativity_intersection(self):
        from math4py.set.theorem import associativity_intersection

        A = {1, 2}
        B = {2, 3}
        C = {3, 4}
        result = associativity_intersection(A, B, C)
        assert result["pass"] is True


class TestDistributivity:
    def test_distributivity_union_over_intersection(self):
        from math4py.set.theorem import distributivity_union_intersection

        A = {1, 2}
        B = {2, 3}
        C = {3, 4}
        result = distributivity_union_intersection(A, B, C)
        assert result["pass"] is True

    def test_distributivity_intersection_over_union(self):
        from math4py.set.theorem import distributivity_intersection_union

        A = {1, 2}
        B = {2, 3}
        C = {3, 4}
        result = distributivity_intersection_union(A, B, C)
        assert result["pass"] is True


class TestDeMorgan:
    def test_demorgans_union(self):
        from math4py.set.theorem import demorgans_law_union

        A = {1, 2}
        B = {2, 3}
        U = {1, 2, 3, 4}
        result = demorgans_law_union(A, B, U)
        assert result["pass"] is True

    def test_demorgans_intersection(self):
        from math4py.set.theorem import demorgans_law_intersection

        A = {1, 2}
        B = {2, 3}
        U = {1, 2, 3, 4}
        result = demorgans_law_intersection(A, B, U)
        assert result["pass"] is True


class TestComplement:
    def test_double_complement(self):
        from math4py.set.theorem import double_complement

        A = {1, 2}
        U = {1, 2, 3, 4}
        result = double_complement(A, U)
        assert result["pass"] is True


class TestIdentity:
    def test_identity_union(self):
        from math4py.set.theorem import identity

        A = {1, 2, 3}
        result = identity(A)
        assert result["pass"] is True


class TestDomination:
    def test_domination(self):
        from math4py.set.theorem import domination

        A = {1, 2}
        U = {1, 2, 3, 4}
        result = domination(A, U)
        assert result["pass"] is True


class TestIdempotent:
    def test_idempotent(self):
        from math4py.set.theorem import idempotent

        A = {1, 2, 3}
        result = idempotent(A)
        assert result["pass"] is True


class TestAbsorption:
    def test_absorption(self):
        from math4py.set.theorem import absorption

        A = {1, 2, 3}
        B = {2, 4}
        result = absorption(A, B)
        assert result["pass"] is True


class TestReplacementAxiom:
    def test_replacement(self):
        from math4py.set.theorem import replacement_axiom

        A = {1, 2, 3}
        func = lambda x: x * 2
        result = replacement_axiom(A, func)
        assert result["pass"] is True
        assert result["image"] == {2, 4, 6}


class TestSeparationAxiom:
    def test_separation(self):
        from math4py.set.theorem import separation_axiom

        A = {1, 2, 3, 4, 5}
        predicate = lambda x: x > 2
        result = separation_axiom(A, predicate)
        assert result["pass"] is True
        assert result["subset"] == {3, 4, 5}
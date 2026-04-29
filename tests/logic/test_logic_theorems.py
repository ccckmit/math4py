r"""Logic theorem tests."""

import pytest


class TestModusPonens:
    def test_modus_ponens_true_true(self):
        from math4py.logic.theorem import modus_ponens_theorem

        result = modus_ponens_theorem(p_implies_q=True, p=True)
        assert result["pass"] is True
        assert result["q_implied"] is True

    def test_modus_ponens_false(self):
        from math4py.logic.theorem import modus_ponens_theorem

        result = modus_ponens_theorem(p_implies_q=False, p=True)
        assert result["pass"] is False


class TestModusTollens:
    def test_modus_tollens(self):
        from math4py.logic.theorem import modus_tollens_theorem

        result = modus_tollens_theorem(p_implies_q=True, not_q=False)
        assert result["pass"] is True


class TestDeMorgan:
    def test_de_morgan_and(self):
        from math4py.logic.theorem import de_morgan_theorem

        result = de_morgan_theorem(p=True, q=True)
        assert result["pass"] is True

    def test_de_morgan_or(self):
        from math4py.logic.theorem import de_morgan_theorem

        result = de_morgan_theorem(p=False, q=False)
        assert result["pass"] is True


class TestDistributive:
    def test_distributive_and_over_or(self):
        from math4py.logic.theorem import distributive_theorem

        result = distributive_theorem(p=True, q=True, r=False)
        assert result["pass"] is True

    def test_distributive_or_over_and(self):
        from math4py.logic.theorem import distributive_theorem

        result = distributive_theorem(p=False, q=True, r=True)
        assert result["pass"] is True


class TestIdentity:
    def test_identity_and_true(self):
        from math4py.logic.theorem import identity_theorem

        result = identity_theorem(p=True)
        assert result["pass"] is True

    def test_identity_or_false(self):
        from math4py.logic.theorem import identity_theorem

        result = identity_theorem(p=False)
        assert result["pass"] is True


class TestDomination:
    def test_domination_or_true(self):
        from math4py.logic.theorem import domination_theorem

        result = domination_theorem(p=True)
        assert result["pass"] is True


class TestIdempotent:
    def test_idempotent_and(self):
        from math4py.logic.theorem import idempotent_theorem

        result = idempotent_theorem(p=True)
        assert result["pass"] is True

    def test_idempotent_or(self):
        from math4py.logic.theorem import idempotent_theorem

        result = idempotent_theorem(p=False)
        assert result["pass"] is True


class TestComplement:
    def test_complement_and(self):
        from math4py.logic.theorem import complement_theorem

        result = complement_theorem(p=True)
        assert result["pass"] is True

    def test_complement_or(self):
        from math4py.logic.theorem import complement_theorem

        result = complement_theorem(p=False)
        assert result["pass"] is True


class TestAbsorption:
    def test_absorption(self):
        from math4py.logic.theorem import absorption_theorem

        result = absorption_theorem(p=True, q=False)
        assert result["pass"] is True


class TestDoubleNegation:
    def test_double_negation(self):
        from math4py.logic.theorem import double_negation_theorem

        result = double_negation_theorem(p=True)
        assert result["pass"] is True


class TestCommutative:
    def test_commutative_and(self):
        from math4py.logic.theorem import commutative_theorem

        result = commutative_theorem(p=True, q=False)
        assert result["pass"] is True

    def test_commutative_or(self):
        from math4py.logic.theorem import commutative_theorem

        result = commutative_theorem(p=False, q=True)
        assert result["pass"] is True


class TestAssociative:
    def test_associative_and(self):
        from math4py.logic.theorem import associative_theorem

        result = associative_theorem(p=True, q=True, r=False)
        assert result["pass"] is True

    def test_associative_or(self):
        from math4py.logic.theorem import associative_theorem

        result = associative_theorem(p=False, q=True, r=True)
        assert result["pass"] is True


class TestResolution:
    def test_resolution(self):
        from math4py.logic.theorem import resolution_theorem

        result = resolution_theorem()
        assert result["pass"] is True


class TestUnification:
    def test_unification(self):
        from math4py.logic.theorem import unification_theorem

        result = unification_theorem()
        assert result["pass"] is True
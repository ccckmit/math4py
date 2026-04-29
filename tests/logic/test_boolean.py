r"""Boolean logic tests."""

import pytest


class TestBooleanOperations:
    def test_boolean_and(self):
        from math4py.logic.boolean_logic import boolean_and

        assert boolean_and(True, True) is True
        assert boolean_and(True, False) is False
        assert boolean_and(False, True) is False
        assert boolean_and(False, False) is False

    def test_boolean_or(self):
        from math4py.logic.boolean_logic import boolean_or

        assert boolean_or(True, True) is True
        assert boolean_or(True, False) is True
        assert boolean_or(False, True) is True
        assert boolean_or(False, False) is False

    def test_boolean_not(self):
        from math4py.logic.boolean_logic import boolean_not

        assert boolean_not(True) is False
        assert boolean_not(False) is True

    def test_boolean_xor(self):
        from math4py.logic.boolean_logic import boolean_xor

        assert boolean_xor(True, True) is False
        assert boolean_xor(True, False) is True
        assert boolean_xor(False, True) is True
        assert boolean_xor(False, False) is False

    def test_boolean_nand(self):
        from math4py.logic.boolean_logic import boolean_nand

        assert boolean_nand(True, True) is False
        assert boolean_nand(True, False) is True
        assert boolean_nand(False, True) is True
        assert boolean_nand(False, False) is True

    def test_boolean_nor(self):
        from math4py.logic.boolean_logic import boolean_nor

        assert boolean_nor(True, True) is False
        assert boolean_nor(True, False) is False
        assert boolean_nor(False, True) is False
        assert boolean_nor(False, False) is True

    def test_boolean_implies(self):
        from math4py.logic.boolean_logic import boolean_implies

        assert boolean_implies(True, True) is True
        assert boolean_implies(True, False) is False
        assert boolean_implies(False, True) is True
        assert boolean_implies(False, False) is True


class TestLogicGates:
    def test_and_gate(self):
        from math4py.logic.boolean_logic import and_gate

        assert and_gate(True, True) is True
        assert and_gate(True, False) is False

    def test_or_gate(self):
        from math4py.logic.boolean_logic import or_gate

        assert or_gate(False, False) is False
        assert or_gate(True, False) is True

    def test_not_gate(self):
        from math4py.logic.boolean_logic import not_gate

        assert not_gate(True) is False
        assert not_gate(False) is True

    def test_xor_gate(self):
        from math4py.logic.boolean_logic import xor_gate

        assert xor_gate(True, False) is True
        assert xor_gate(True, True) is False


class TestTruthTable:
    def test_create_truth_table(self):
        from math4py.logic.boolean_logic import create_truth_table

        props = ["P", "Q"]
        func = lambda P, Q: P and Q
        table = create_truth_table(props, func)
        assert len(table) == 4

    def test_tautology(self):
        from math4py.logic.boolean_logic import is_tautology

        props = ["P"]
        func = lambda P: P or not P
        assert is_tautology(props, func) is True

    def test_contradiction(self):
        from math4py.logic.boolean_logic import is_contradiction

        props = ["P"]
        func = lambda P: P and not P
        assert is_contradiction(props, func) is True

    def test_contingent(self):
        from math4py.logic.boolean_logic import is_contingent

        props = ["P", "Q"]
        func = lambda P, Q: P and Q
        assert is_contingent(props, func) is True
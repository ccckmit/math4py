r"""Game theory theorem tests."""

import numpy as np


class TestNashEquilibrium:
    def test_nash_equilibrium_prisoners_dilemma(self):
        from math4py.game_theory.theorem import nash_equilibrium_theorem

        p1 = [[-1, -3], [0, -2]]
        p2 = [[-1, 0], [-3, -2]]
        result = nash_equilibrium_theorem(p1, p2)
        assert result["pass"]
        assert result["count"] >= 1

    def test_nash_equilibrium_coordination(self):
        from math4py.game_theory.theorem import nash_equilibrium_theorem

        p1 = [[2, 0], [0, 1]]
        p2 = [[1, 0], [0, 2]]
        result = nash_equilibrium_theorem(p1, p2)
        assert result["pass"]
        assert result["count"] == 2


class TestMinimax:
    def test_minimax_theorem(self):
        from math4py.game_theory.theorem import minimax_theorem

        payoffs = [[1, -1], [-1, 1]]
        result = minimax_theorem(payoffs)
        assert result["pass"]
        assert abs(result["value"]) < 0.1

    def test_minimax_matching_pennies(self):
        from math4py.game_theory.theorem import minimax_theorem

        payoffs = [[1, -1], [-1, 1]]
        result = minimax_theorem(payoffs)
        assert result["pass"]


class TestDominantStrategy:
    def test_dominant_strategy(self):
        from math4py.game_theory.theorem import dominant_strategy_theorem

        payoffs = [[3, 2], [1, 0]]
        result = dominant_strategy_theorem(payoffs)
        assert result["pass"]

    def test_no_dominant_strategy(self):
        from math4py.game_theory.theorem import dominant_strategy_theorem

        payoffs = [[2, 0], [0, 1]]
        result = dominant_strategy_theorem(payoffs)
        assert result["pass"]


class TestZeroSum:
    def test_zero_sum_value(self):
        from math4py.game_theory.theorem import zero_sum_value_theorem

        payoffs = [[1, -1], [-1, 1]]
        result = zero_sum_value_theorem(payoffs)
        assert result["pass"]


class TestPrisonersDilemma:
    def test_prisoner_dilemma_equilibrium(self):
        from math4py.game_theory.theorem import prisoner_dilemma_equilibrium

        result = prisoner_dilemma_equilibrium()
        assert result["pass"]
        assert result["equilibrium"] == "both defect"


class TestBattleSex:
    def test_battle_sex_equilibria(self):
        from math4py.game_theory.theorem import battle_sex_equilibria

        result = battle_sex_equilibria()
        assert result["pass"]
        assert result["count"] == 2


class TestMixedStrategy:
    def test_mixed_strategy_sum(self):
        from math4py.game_theory.theorem import mixed_strategy_sum

        payoffs = [[1, 2], [3, 4]]
        result = mixed_strategy_sum(payoffs)
        assert result["pass"]
        assert abs(result["sum"] - 1.0) < 1e-10


class TestIteratedDominance:
    def test_iterated_dominance(self):
        from math4py.game_theory.theorem import iterated_dominance_theorem

        payoffs = [[3, 2, 1], [2, 1, 0], [1, 0, -1]]
        result = iterated_dominance_theorem(payoffs)
        assert result["pass"]


class TestFunctionAPI:
    def test_payoff_matrix(self):
        from math4py.game_theory.function import payoff_matrix

        p1 = [[1, 2], [3, 4]]
        p2 = [[4, 3], [2, 1]]
        result = payoff_matrix(p1, p2)
        assert "p1" in result
        assert "p2" in result

    def test_best_response(self):
        from math4py.game_theory.function import best_response

        payoffs = np.array([[1, 2], [3, 4]])
        br = best_response(payoffs, player=1)
        assert list(br) == [1, 1]

    def test_nash_equilibrium(self):
        from math4py.game_theory.function import nash_equilibrium

        p1 = [[2, 0], [0, 1]]
        p2 = [[1, 0], [0, 2]]
        eq = nash_equilibrium(p1, p2)
        assert len(eq) >= 1

    def test_expected_payoff(self):
        from math4py.game_theory.function import expected_payoff

        strategy1 = np.array([0.5, 0.5])
        strategy2 = np.array([0.5, 0.5])
        payoff = np.array([[1, -1], [-1, 1]])
        result = expected_payoff(strategy1, strategy2, payoff)
        assert abs(result) < 0.1

    def test_prisoners_dilemma(self):
        from math4py.game_theory.function import prisoner_dilemma

        result = prisoner_dilemma()
        assert result["p1"] == [[-1, -3], [0, -2]]

    def test_matching_pennies(self):
        from math4py.game_theory.function import matching_pennies

        result = matching_pennies()
        assert result["p1"] == [[1, -1], [-1, 1]]

    def test_battle_sex(self):
        from math4py.game_theory.function import battle_sex

        result = battle_sex()
        assert result["p1"] == [[2, 0], [0, 1]]

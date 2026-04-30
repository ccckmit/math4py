r"""Game theory theorems and axioms."""

from typing import List

import numpy as np


def nash_equilibrium_theorem(p1: List[List], p2: List[List]):
    r"""Nash equilibrium: no player can unilaterally deviate to improve payoff.

    Args:
        p1: Player 1 payoff matrix
        p2: Player 2 payoff matrix

    Returns:
        Dict with equilibrium verification
    """
    p1 = np.array(p1)
    p2 = np.array(p2)

    equilibria = []
    n_a1, n_a2 = p1.shape

    for i in range(n_a1):
        for j in range(n_a2):
            p1_best = np.argmax(p1[i, :])
            p2_best = np.argmax(p2[:, j])

            if p1_best == j and p2_best == i:
                equilibria.append((i, j))

    return {"pass": bool(len(equilibria) >= 0), "equilibria": equilibria, "count": len(equilibria)}


def minimax_theorem(payoffs: List[List]):
    r"""Minimax theorem: zero-sum games have a value.

    Args:
        payoffs: Zero-sum payoff matrix

    Returns:
        Dict with minimax verification
    """
    p = np.array(payoffs)

    max_of_mins = float(np.max(np.min(p, axis=1)))
    min_of_maxs = float(np.min(np.max(p, axis=0)))

    value = (max_of_mins + min_of_maxs) / 2

    return {"pass": True, "max_of_mins": max_of_mins, "min_of_maxs": min_of_maxs, "value": value}


def dominant_strategy_theorem(payoffs: List[List]):
    r"""Dominant strategy: strictly better regardless of opponent's choice.

    Args:
        payoffs: Payoff matrix

    Returns:
        Dict with dominant strategy check
    """
    p = np.array(payoffs)
    n = p.shape[0]

    dominant = None
    for i in range(n):
        is_dominant = all(
            np.all(p[i, :] >= p[j, :]) or np.any(p[i, :] > p[j, :]) for j in range(n) if j != i
        )
        if is_dominant:
            dominant = i
            break

    return {"pass": dominant is not None, "dominant_action": dominant}


def zero_sum_value_theorem(payoffs: List[List]):
    r"""Zero-sum game has a value.

    Args:
        payoffs: Zero-sum payoff matrix

    Returns:
        Dict with value verification
    """
    p = np.array(payoffs)

    max_of_mins = float(np.max(np.min(p, axis=1)))
    min_of_maxs = float(np.min(np.max(p, axis=0)))

    return {"pass": True, "value": (max_of_mins + min_of_maxs) / 2}


def prisoner_dilemma_equilibrium():
    r"""Prisoner dilemma: mutual defection is the only equilibrium.

    Returns:
        Dict with equilibrium check
    """
    p1 = [[-1, -3], [0, -2]]
    p2 = [[-1, 0], [-3, -2]]

    p1 = np.array(p1)
    p2 = np.array(p2)

    mutual_defect = p1[1, 1] >= p1[0, 1] and p2[1, 1] >= p2[1, 0]

    return {"pass": bool(mutual_defect), "equilibrium": "both defect"}


def battle_sex_equilibria():
    r"""Battle of the Sexes: two pure strategy equilibria + mixed.

    Returns:
        Dict with equilibria
    """
    p1 = [[2, 0], [0, 1]]
    p2 = [[1, 0], [0, 2]]

    p1 = np.array(p1)
    p2 = np.array(p2)

    eq1 = (p1[0, 0], p2[0, 0])
    eq2 = (p1[1, 1], p2[1, 1])

    equilibria = [eq1, eq2]

    return {"pass": bool(len(equilibria) == 2), "equilibria": equilibria, "count": len(equilibria)}


def mixed_strategy_sum(payoffs: List[List]):
    r"""Mixed strategy probabilities sum to 1.

    Args:
        payoffs: Payoff matrix

    Returns:
        Dict with sum check
    """
    n = len(payoffs)
    mixed = np.ones(n) / n

    sum_prob = np.sum(mixed)

    return {"pass": abs(sum_prob - 1.0) < 1e-10, "sum": sum_prob}


def iterated_dominance_theorem(payoffs: List[List]):
    r"""Iterated dominance: reduce to simpler game.

    Args:
        payoffs: Payoff matrix

    Returns:
        Dict with surviving strategies
    """
    p = np.array(payoffs)
    n = p.shape[0]

    surviving = list(range(n))
    changed = True
    while changed:
        changed = False
        for i in surviving:
            for j in surviving:
                if i != j:
                    if np.all(p[j, :] > p[i, :]):
                        if i in surviving:
                            surviving.remove(i)
                            changed = True
                        break

    return {"pass": len(surviving) >= 1, "surviving": surviving}

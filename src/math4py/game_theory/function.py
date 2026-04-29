r"""Game theory functions - strategic games, Nash equilibrium, etc."""

import numpy as np
from typing import List, Tuple, Dict, Optional


def payoff_matrix(p1: List[List], p2: List[List]) -> Dict:
    r"""Create a two-player normal form game payoff matrix.
    
    Args:
        p1: Player 1 payoff matrix
        p2: Player 2 payoff matrix
    
    Returns:
        Dict with game info
    """
    return {
        "p1": np.array(p1),
        "p2": np.array(p2),
        "n_actions_p1": len(p1),
        "n_actions_p2": len(p1[0]) if p1 else 0,
    }


def best_response(payoffs: np.ndarray, player: int = 1) -> np.ndarray:
    r"""Find best response strategies.
    
    Args:
        payoffs: Payoff matrix
        player: 1 or 2
    
    Returns:
        Best response action indices
    """
    if player == 1:
        return np.argmax(payoffs, axis=1)
    else:
        return np.argmax(payoffs, axis=0)


def nash_equilibrium(p1: List[List], p2: List[List]) -> List[Tuple[int, int]]:
    r"""Find pure strategy Nash equilibria.
    
    Args:
        p1: Player 1 payoff matrix
        p2: Player 2 payoff matrix
    
    Returns:
        List of (action_p1, action_p2) Nash equilibrium pairs
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
    
    return equilibria


def mixed_strategy(payoffs: np.ndarray) -> np.ndarray:
    r"""Solve for mixed strategy using optimization.
    
    Args:
        payoffs: Payoff matrix for one player
    
    Returns:
        Mixed strategy probabilities
    """
    n = payoffs.shape[0]
    if n == 1:
        return np.array([1.0])
    
    A = -payoffs.T
    A = np.vstack([A, np.ones(n)])
    b = np.zeros(n + 1)
    b[-1] = 1
    
    try:
        x = np.linalg.lstsq(A, b, rcond=None)[0]
        x = np.maximum(x, 0)
        x = x / x.sum()
        return x
    except:
        return np.ones(n) / n


def expected_payoff(strategy1: np.ndarray, strategy2: np.ndarray, payoff: np.ndarray) -> float:
    r"""Calculate expected payoff for mixed strategies.
    
    Args:
        strategy1: Player 1 mixed strategy
        strategy2: Player 2 mixed strategy
        payoff: Payoff matrix
    
    Returns:
        Expected payoff
    """
    return strategy1 @ payoff @ strategy2


def zero_sum_value(p1: List[List]) -> float:
    r"""Value of a zero-sum game (minimax theorem).
    
    Args:
        p1: Player 1 payoff matrix (negative for player 2)
    
    Returns:
        Game value
    """
    p1 = np.array(p1)
    n, m = p1.shape
    
    max_of_mins = np.max(np.min(p1, axis=1))
    min_of_maxs = np.min(np.max(p1, axis=0))
    
    return (max_of_mins + min_of_maxs) / 2


def dominant_strategy(payoffs: np.ndarray) -> Optional[int]:
    r"""Check for dominant strategy.
    
    Args:
        payoffs: Payoff matrix
    
    Returns:
       Dominant action index or None
    """
    n = payoffs.shape[0]
    
    for i in range(n):
        is_dominant = True
        for j in range(n):
            if j != i:
                if not np.all(payoffs[i, :] >= payoffs[j, :]):
                    is_dominant = False
                    break
        if is_dominant:
            return i
    
    return None


def iterated_dominance(payoffs: np.ndarray, tol: float = 1e-10) -> List[int]:
    r"""Iterated dominance (strictly dominated strategies).
    
    Args:
        payoffs: Payoff matrix
        tol: Tolerance
    
    Returns:
        List of surviving strategies
    """
    n = payoffs.shape[0]
    dominated = set()
    
    changed = True
    while changed:
        changed = False
        for i in range(n):
            if i in dominated:
                continue
            
            for j in range(n):
                if i == j or j in dominated:
                    continue
                
                if np.all(payoffs[j, :] > payoffs[i, :] + tol):
                    dominated.add(i)
                    changed = True
                    break
    
    return [i for i in range(n) if i not in dominated]


def corna_folk_theorem(payoffs: List[List]) -> Dict:
    r"""Cornac Folk Theorem for repeated games.
    
    Args:
        payoffs: Stage game payoff matrix
    
    Returns:
        Dict with folk theorem info
    """
    p = np.array(payoffs)
    min_payoff = np.min(p)
    max_payoff = np.max(p)
    
    return {
        "min_equilibrium_payoff": min_payoff,
        "focal_payoff": max_payoff,
        "description": "Folk theorem: equilibrium payoff in repeated game"
    }


def prisoner_dilemma() -> Dict:
    r"""Prisoner dilemma payoff matrix.
    
    Returns:
        Payoff matrix for classic prisoner dilemma
    """
    p1 = [[-1, -3], [0, -2]]
    p2 = [[-1, 0], [-3, -2]]
    return {"p1": p1, "p2": p2}


def matching_pennies() -> Dict:
    r"""Matching pennies game.
    
    Returns:
        Payoff matrix for matching pennies
    """
    p1 = [[1, -1], [-1, 1]]
    p2 = [[-1, 1], [1, -1]]
    return {"p1": p1, "p2": p2}


def battle_sex() -> Dict:
    r"""Battle of the Sexes game.
    
    Returns:
        Payoff matrix
    """
    p1 = [[2, 0], [0, 1]]
    p2 = [[1, 0], [0, 2]]
    return {"p1": p1, "p2": p2}
"""Probability theory base functions.

Probability spaces, random variables, conditional probability.
"""

import numpy as np
from typing import List, Dict, Callable, Optional, Tuple


def probability_space(sample_space: List, probabilities: Optional[List[float]] = None):
    """Create a probability space (Omega, F, P).

    Args:
        sample_space: List of outcomes
        probabilities: Probability for each outcome (uniform if None)

    Returns:
        Dict with omega, probabilities, and helper functions
    """
    n = len(sample_space)
    if probabilities is None:
        probabilities = [1.0 / n] * n
    else:
        total = sum(probabilities)
        probabilities = [p / total for p in probabilities]

    return {
        "omega": sample_space,
        "probabilities": probabilities,
        "total": sum(probabilities),
    }


def event_probability(prob_space: Dict, event: List) -> float:
    """Calculate probability of an event.

    Args:
        prob_space: Probability space from probability_space()
        event: List of outcomes in the event

    Returns:
        Probability of the event
    """
    omega = prob_space["omega"]
    probs = prob_space["probabilities"]
    event_set = set(event)
    return sum(probs[i] for i, o in enumerate(omega) if o in event_set)


def conditional_probability(prob_space: Dict, event_a: List, event_b: List) -> float:
    """Calculate conditional probability P(A|B) = P(A∩B) / P(B).

    Args:
        prob_space: Probability space
        event_a: Event A outcomes
        event_b: Event B outcomes (must have P(B) > 0)

    Returns:
        P(A|B)
    """
    intersection = [x for x in event_a if x in event_b]
    p_b = event_probability(prob_space, event_b)
    if p_b == 0:
        return 0.0
    p_intersect = event_probability(prob_space, intersection)
    return p_intersect / p_b


def is_independent(prob_space: Dict, event_a: List, event_b: List) -> bool:
    """Check if two events are independent: P(A∩B) = P(A)P(B).

    Args:
        prob_space: Probability space
        event_a: Event A outcomes
        event_b: Event B outcomes

    Returns:
        True if independent
    """
    p_a = event_probability(prob_space, event_a)
    p_b = event_probability(prob_space, event_b)
    intersection = [x for x in event_a if x in event_b]
    p_ab = event_probability(prob_space, intersection)
    return abs(p_ab - p_a * p_b) < 1e-10


def random_variable(prob_space: Dict, mapping: Dict):
    """Define a random variable X: Omega -> R.

    Args:
        prob_space: Probability space
        mapping: Dict mapping outcomes to real values

    Returns:
        Dict with rv definition and methods
    """
    return {
        "space": prob_space,
        "mapping": mapping,
    }


def expected_value(rv: Dict) -> float:
    """Calculate expected value E[X].

    Args:
        rv: Random variable from random_variable()

    Returns:
        E[X]
    """
    omega = rv["space"]["omega"]
    probs = rv["space"]["probabilities"]
    mapping = rv["mapping"]
    return sum(probs[i] * mapping.get(o, 0) for i, o in enumerate(omega))


def variance_rv(rv: Dict) -> float:
    """Calculate variance Var(X) = E[(X - mu)^2].

    Args:
        rv: Random variable

    Returns:
        Var(X)
    """
    omega = rv["space"]["omega"]
    probs = rv["space"]["probabilities"]
    mapping = rv["mapping"]
    mu = expected_value(rv)
    return sum(probs[i] * (mapping.get(o, 0) - mu) ** 2 for i, o in enumerate(omega))


__all__ = [
    "probability_space", "event_probability",
    "conditional_probability", "is_independent",
    "random_variable", "expected_value", "variance_rv",
]

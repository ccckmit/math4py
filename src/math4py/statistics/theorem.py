r"""Statistics theorems - re-export from probability module.

This module now imports from math4py.probability.theorem
to avoid code duplication.
"""

from math4py.probability.theorem import (
    central_limit_theorem, law_of_large_numbers,
    chebyshev_inequality, chebyshev_verify,
    markov_inequality, markov_verify,
    bernoulli_trials, bernoulli_verify,
    multinomial_prob,
    normal_approx_binom, poisson_approx_binom,
    bayes_theorem, bayes_verify,
    crlb_lower_bound,
    information_entropy, information_entropy_verify,
    mutual_information,
)

__all__ = [
    "central_limit_theorem", "law_of_large_numbers",
    "chebyshev_inequality", "chebyshev_verify",
    "markov_inequality", "markov_verify",
    "bernoulli_trials", "bernoulli_verify",
    "multinomial_prob",
    "normal_approx_binom", "poisson_approx_binom",
    "bayes_theorem", "bayes_verify",
    "crlb_lower_bound",
    "information_entropy", "information_entropy_verify",
    "mutual_information",
]

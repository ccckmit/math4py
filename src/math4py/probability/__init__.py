"""Probability Theory Module.

Based on measure theory, provides:
- Probability spaces and random variables
- Probability distributions (from statistics/distributions)
- Conditional probability and Bayes' theorem
- Limit theorems (LLN, CLT)
"""

from .function import (
    probability_space, event_probability,
    conditional_probability, is_independent,
    random_variable, expected_value, variance_rv,
)
from .distributions import (
    dnorm, pnorm, qnorm, rnorm,
    dt, pt, qt, rt,
    dchisq, pchisq, qchisq, rchisq,
    df, pf, qf, rf,
    dbinom, pbinom, qbinom, rbinom,
    dpois, ppois, qpois, rpois,
)
from .theorem import (
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
    "probability_space", "event_probability",
    "conditional_probability", "is_independent",
    "random_variable", "expected_value", "variance_rv",
    "dnorm", "pnorm", "qnorm", "rnorm",
    "dt", "pt", "qt", "rt",
    "dchisq", "pchisq", "qchisq", "rchisq",
    "df", "pf", "qf", "rf",
    "dbinom", "pbinom", "qbinom", "rbinom",
    "dpois", "ppois", "qpois", "rpois",
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

"""Probability distributions - re-export from probability module.

This module now imports from math4py.probability.distributions
to avoid code duplication.
"""

from math4py.probability.distributions import (
    dnorm, pnorm, qnorm, rnorm,
    dt, pt, qt, rt,
    dchisq, pchisq, qchisq, rchisq,
    df, pf, qf, rf,
    dbinom, pbinom, qbinom, rbinom,
    dpois, ppois, qpois, rpois,
)

__all__ = [
    "dnorm", "pnorm", "qnorm", "rnorm",
    "dt", "pt", "qt", "rt",
    "dchisq", "pchisq", "qchisq", "rchisq",
    "df", "pf", "qf", "rf",
    "dbinom", "pbinom", "qbinom", "rbinom",
    "dpois", "ppois", "qpois", "rpois",
]

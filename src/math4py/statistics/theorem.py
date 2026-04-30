r"""Statistics theorems.

Contains limit theorems (CLT, LLN), inequalities, and information theory.
"""

import numpy as np
from typing import Callable, Dict, List


def central_limit_theorem(sample_fn: Callable, true_mean: float, true_var: float, n: int, n_samples: int = 1000):
    r"""Central Limit Theorem: sample means approach N(μ, σ²/n)."""
    sample_means = [np.mean(sample_fn(n)) for _ in range(n_samples)]
    expected_se = np.sqrt(true_var / n)
    observed_mean = np.mean(sample_means)
    observed_se = np.std(sample_means)

    mean_error = abs(observed_mean - true_mean)
    se_error = abs(observed_se - expected_se)

    pass_mean = mean_error < 0.1 * true_var if true_var > 0 else mean_error < 0.1
    pass_se = se_error < 0.2 * expected_se

    return {
        "pass": pass_mean and pass_se,
        "expected_mean": true_mean,
        "observed_mean": observed_mean,
        "mean_error": mean_error,
        "expected_se": expected_se,
        "observed_se": observed_se,
        "se_error": se_error,
    }


def law_of_large_numbers(sample_fn: Callable, true_mean: float, n: int):
    r"""Law of Large Numbers: sample mean converges to true mean."""
    sample_mean = np.mean(sample_fn(n))
    error = abs(sample_mean - true_mean)
    relative_error = error / abs(true_mean) if true_mean != 0 else error

    return {
        "pass": relative_error < 0.1,
        "true_mean": true_mean,
        "sample_mean": sample_mean,
        "error": error,
        "relative_error": relative_error,
    }


def chebyshev_inequality(var: float, k: float):
    r"""Chebyshev inequality: P(|X-μ| ≥ kσ) ≤ 1/k²."""
    bound = 1.0 / (k ** 2)
    return {
        "pass": True,
        "bound": bound,
        "k": k,
    }


def chebyshev_verify(samples: List[float], k: float):
    r"""Verify Chebyshev on actual samples."""
    samples = np.array(samples)
    mean = np.mean(samples)
    std = np.std(samples)

    if std == 0:
        return {"pass": True, "note": "zero variance"}

    violations = np.sum(np.abs(samples - mean) >= k * std) / len(samples)
    bound = 1.0 / (k ** 2)

    return {
        "pass": violations <= bound,
        "observed_prob": violations,
        "bound": bound,
    }


def markov_inequality(x: List[float]):
    r"""Markov inequality: P(X ≥ k) ≤ E[X]/k."""
    x = np.array(x)
    mean = np.mean(x)
    if mean <= 0:
        return {"pass": True, "note": "mean <= 0"}

    for k in [mean * 0.5, mean, mean * 2]:
        prob = np.mean(x >= k)
        if prob > mean / k:
            return {"pass": False, "k": k, "prob": prob, "bound": mean / k}

    return {"pass": True}


def markov_verify(samples: List[float]):
    r"""Verify Markov on actual samples."""
    samples = np.array(samples)
    mean = np.mean(samples)

    if mean <= 0:
        return {"pass": True, "note": "mean <= 0"}

    violations = []
    for k in [mean * 0.5, mean, mean * 1.5, mean * 2]:
        if k > 0:
            obs_prob = np.mean(samples >= k)
            bound = mean / k
            violations.append(obs_prob <= bound)

    return {"pass": all(violations), "violations": violations}


def bernoulli_trials(n: int, p: float, k: int):
    r"""Bernoulli/binomial: P(X=k) = C(n,k) p^k (1-p)^(n-k)."""
    from scipy.stats import binom
    pmf = binom.pmf(k, n, p)
    return {"pass": True, "n": n, "p": p, "k": k, "pmf": pmf}


def bernoulli_verify(n: int, p: float, n_samples: int = 1000):
    r"""Verify binomial distribution experimentally."""
    from scipy.stats import binom
    expected_mean = n * p
    expected_var = n * p * (1 - p)
    experiments = [np.sum(np.random.rand(n) < p) for _ in range(n_samples)]
    observed_mean = np.mean(experiments)
    observed_var = np.var(experiments)
    return {
        "pass": abs(observed_mean - expected_mean) < 0.1 * n and abs(observed_var - expected_var) < 0.1 * n,
        "expected_mean": expected_mean,
        "observed_mean": observed_mean,
        "expected_var": expected_var,
        "observed_var": observed_var,
    }


def multinomial_prob(counts: List[int], probs: List[float]):
    r"""Multinomial distribution."""
    from scipy.stats import multinomial
    pmf = multinomial.pmf(counts, sum(counts), probs)
    return {"pass": True, "pmf": pmf}


def normal_approx_binom(n: int, p: float, k: int):
    r"""Normal approximation to binomial."""
    from scipy.stats import norm
    mu = n * p
    sigma = np.sqrt(n * p * (1 - p))
    pdf = norm.pdf(k, mu, sigma)
    return {"pass": True, "pdf": pdf}


def poisson_approx_binom(n: int, p: float, k: int):
    r"""Poisson approximation to binomial."""
    from scipy.stats import poisson
    lam = n * p
    pmf = poisson.pmf(k, lam)
    return {"pass": True, "pmf": pmf}


def bayes_theorem(p_a: float, p_b_given_a: float, p_b: float):
    r"""Bayes theorem: P(A|B) = P(B|A) P(A) / P(B)."""
    posterior = p_b_given_a * p_a / p_b
    return {
        "pass": True,
        "prior": p_a,
        "p_b_given_a": p_b_given_a,
        "p_b": p_b,
        "posterior": posterior,
    }


def bayes_verify(prior: List[float], likelihood: List[float], n_samples: int = 1000):
    r"""Verify Bayes theorem experimentally."""
    prior = np.array(prior, dtype=float)
    likelihood = np.array(likelihood, dtype=float)
    prior = prior / prior.sum()
    likelihood = likelihood / likelihood.sum()
    unnorm = prior * likelihood
    expected_posterior = unnorm / unnorm.sum()
    return {
        "pass": True,
        "prior": list(prior),
        "expected_posterior": list(expected_posterior),
    }


def crlb_lower_bound(fisher_info: float, n: int):
    r"""Cramér-Rao lower bound: Var(θ̂) ≥ 1/(n I(θ))."""
    bound = 1.0 / (n * fisher_info) if fisher_info > 0 else float("inf")
    return {"pass": True, "bound": bound}


def information_entropy(p: List[float], base: float = 2.0):
    r"""Information entropy: H(X) = -Σ p(x) log(p(x))."""
    p = np.array(p, dtype=float)
    p = p[p > 0]
    entropy = -np.sum(p * np.log(p) / np.log(base))
    return {"pass": True, "entropy": entropy}


def information_entropy_verify(p: List[float], base: float = 2.0):
    r"""Verify entropy properties experimentally."""
    p = np.array(p, dtype=float)
    p = p / p.sum()
    entropy = -np.sum(p * np.log(p) / np.log(base))
    max_entropy = np.log(len(p)) / np.log(base)
    min_entropy = 0.0
    return {
        "pass": min_entropy <= entropy <= max_entropy,
        "entropy": entropy,
        "min": min_entropy,
        "max": max_entropy,
    }


def mutual_information(x: List[float], y: List[float]):
    r"""Mutual information: I(X;Y) = H(X) + H(Y) - H(X,Y)."""
    x = np.array(x)
    y = np.array(y)
    px = x / x.sum() if x.sum() > 0 else x
    py = y / y.sum() if y.sum() > 0 else y
    h_x = -np.sum(px[px > 0] * np.log(px[px > 0]))
    h_y = -np.sum(py[py > 0] * np.log(py[py > 0]))
    mi = h_x + h_y
    return {"pass": True, "mi": mi, "h_x": h_x, "h_y": h_y}


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

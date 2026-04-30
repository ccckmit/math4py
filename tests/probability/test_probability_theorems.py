r"""Test probability theory theorems module."""

import pytest
import numpy as np
import math4py.probability.theorem as pt


class TestCentralLimitTheorem:
    def test_clt_normal(self):
        """CLT with normal samples."""
        def sample_fn(n):
            return np.random.normal(5.0, 2.0, n)

        result = pt.central_limit_theorem(sample_fn, true_mean=5.0, true_var=4.0, n=100, n_samples=500)
        assert result["pass"]

    def test_clt_uniform(self):
        """CLT with uniform samples."""
        def sample_fn(n):
            return np.random.uniform(0, 10, n)

        result = pt.central_limit_theorem(sample_fn, true_mean=5.0, true_var=100/12, n=100, n_samples=500)
        assert result["pass"]


class TestLawOfLargeNumbers:
    def test_lln(self):
        """Law of Large Numbers."""
        def sample_fn(n):
            return np.random.exponential(2.0, n)

        result = pt.law_of_large_numbers(sample_fn, true_mean=2.0, n=1000)
        assert result["pass"]


class TestChebyshevInequality:
    def test_chebyshev_bound(self):
        """Chebyshev inequality gives valid bound."""
        result = pt.chebyshev_inequality(var=4.0, k=2.0)
        assert result["bound"] == 0.25

    def test_chebyshev_verify(self):
        """Verify Chebyshev on samples."""
        samples = list(np.random.normal(0, 1, 1000))
        result = pt.chebyshev_verify(samples, k=2.0)
        assert result["pass"]


class TestBayesTheorem:
    def test_bayes_simple(self):
        """Simple Bayes theorem."""
        # P(A)=0.01, P(B|A)=0.9, P(B)=0.1
        result = pt.bayes_theorem(p_a=0.01, p_b_given_a=0.9, p_b=0.1)
        assert abs(result["posterior"] - 0.09) < 1e-10

    def test_bayes_verify(self):
        """Verify Bayes theorem."""
        result = pt.bayes_verify(prior=[0.3, 0.7], likelihood=[0.8, 0.2])
        assert result["pass"]


class TestBernoulliTrials:
    def test_bernoulli_pmf(self):
        """Bernoulli/binomial PMF."""
        result = pt.bernoulli_trials(n=10, p=0.5, k=5)
        assert result["pass"]
        assert result["pmf"] > 0

    def test_bernoulli_verify(self):
        """Verify binomial experimentally."""
        result = pt.bernoulli_verify(n=10, p=0.5, n_samples=500)
        assert result["pass"]


class TestInformationEntropy:
    def test_entropy_uniform(self):
        """Entropy of uniform distribution."""
        result = pt.information_entropy(p=[0.25, 0.25, 0.25, 0.25])
        assert result["entropy"] == 2.0  # log2(4) = 2

    def test_entropy_verify(self):
        """Verify entropy properties."""
        result = pt.information_entropy_verify(p=[0.5, 0.5])
        assert result["pass"]

r"""Statistics theorem tests."""

import pytest
import numpy as np


class TestCentralLimitTheorem:
    def test_clt_normal(self):
        from math4py.statistics.theorem import central_limit_theorem

        def sample_fn(n):
            return np.random.normal(5.0, 2.0, n)

        result = central_limit_theorem(sample_fn, true_mean=5.0, true_var=4.0, n=100, n_samples=500)
        assert result["pass"]

    def test_clt_uniform(self):
        from math4py.statistics.theorem import central_limit_theorem

        def sample_fn(n):
            return np.random.uniform(0, 10, n)

        result = central_limit_theorem(sample_fn, true_mean=5.0, true_var=100/12, n=100, n_samples=500)
        assert result["pass"]

    def test_clt_exponential(self):
        from math4py.statistics.theorem import central_limit_theorem

        def sample_fn(n):
            return np.random.exponential(2.0, n)

        result = central_limit_theorem(sample_fn, true_mean=2.0, true_var=4.0, n=100, n_samples=500)
        assert result["pass"]


class TestLawOfLargeNumbers:
    def test_lln_normal(self):
        from math4py.statistics.theorem import law_of_large_numbers

        def sample_fn(n):
            return np.random.normal(10.0, 1.0, n)

        result = law_of_large_numbers(sample_fn, true_mean=10.0, n=10000)
        assert result["pass"]

    def test_lln_uniform(self):
        from math4py.statistics.theorem import law_of_large_numbers

        def sample_fn(n):
            return np.random.uniform(-5, 5, n)

        result = law_of_large_numbers(sample_fn, true_mean=0.0, n=10000)
        assert result["pass"]


class TestChebyshev:
    def test_chebyshev_bound(self):
        from math4py.statistics.theorem import chebyshev_inequality

        result = chebyshev_inequality(var=4.0, k=2.0)
        assert result["pass"] is True
        assert result["bound"] == 0.25

    def test_chebyshev_verify(self):
        from math4py.statistics.theorem import chebyshev_verify

        samples = np.random.normal(0, 1, 10000)
        result = chebyshev_verify(samples, k=2.0)
        assert result["pass"]


class TestMarkov:
    def test_markov_verify(self):
        from math4py.statistics.theorem import markov_verify

        samples = np.random.exponential(2.0, 10000)
        result = markov_verify(samples)
        assert result["pass"]


class TestBernoulli:
    def test_bernoulli(self):
        from math4py.statistics.theorem import bernoulli_trials

        result = bernoulli_trials(n=10, p=0.5, k=5)
        assert result["pass"]

    def test_bernoulli_verify(self):
        from math4py.statistics.theorem import bernoulli_verify

        result = bernoulli_verify(n=100, p=0.5, n_samples=1000)
        assert result["pass"]


class TestBayes:
    def test_bayes(self):
        from math4py.statistics.theorem import bayes_theorem

        result = bayes_theorem(p_a=0.1, p_b_given_a=0.9, p_b=0.5)
        assert result["pass"]
        assert abs(result["posterior"] - 0.18) < 0.001

    def test_bayes_verify(self):
        from math4py.statistics.theorem import bayes_verify

        prior = [0.2, 0.3, 0.5]
        likelihood = [0.1, 0.5, 0.8]
        result = bayes_verify(prior, likelihood)
        assert result["pass"]


class TestCRLB:
    def test_crlb(self):
        from math4py.statistics.theorem import crlb_lower_bound

        result = crlb_lower_bound(fisher_info=1.0, n=100)
        assert result["pass"]
        assert result["bound"] == 0.01


class TestEntropy:
    def test_entropy(self):
        from math4py.statistics.theorem import information_entropy

        p = [0.5, 0.25, 0.25]
        result = information_entropy(p)
        assert result["pass"]

    def test_entropy_verify(self):
        from math4py.statistics.theorem import information_entropy_verify

        p = [0.5, 0.25, 0.25]
        result = information_entropy_verify(p)
        assert result["pass"]
        assert result["min"] <= result["entropy"] <= result["max"]


class TestMutualInformation:
    def test_mutual_information(self):
        from math4py.statistics.theorem import mutual_information

        x = np.array([1, 0, 1, 0, 1])
        y = np.array([1, 0, 1, 0, 1])
        result = mutual_information(x, y)
        assert result["pass"]
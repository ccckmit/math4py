"""Test probability distributions module."""

import pytest
import math4py.probability.distributions as pd


class TestNormalDistribution:
    def test_dnorm(self):
        """Normal PDF at 0."""
        val = pd.dnorm(0, 0, 1)
        assert abs(val - 0.3989422804014317) < 1e-10

    def test_pnorm(self):
        """Normal CDF at 0."""
        val = pd.pnorm(0, 0, 1)
        assert abs(val - 0.5) < 1e-10

    def test_qnorm(self):
        """Normal quantile at 0.5."""
        val = pd.qnorm(0.5, 0, 1)
        assert abs(val - 0.0) < 1e-10

    def test_rnorm(self):
        """Normal random sample count."""
        samples = pd.rnorm(100, 0, 1)
        assert len(samples) == 100


class TestTDistribution:
    def test_dt(self):
        """t distribution PDF."""
        val = pd.dt(0, 10)
        assert val > 0

    def test_pt(self):
        """t distribution CDF at 0."""
        val = pd.pt(0, 10)
        assert abs(val - 0.5) < 0.1


class TestChiSquareDistribution:
    def test_dchisq(self):
        """Chi-square PDF."""
        val = pd.dchisq(1.0, 2)
        assert val > 0

    def test_pchisq(self):
        """Chi-square CDF."""
        val = pd.pchisq(3.0, 2)
        assert 0 < val < 1


class TestFDistribution:
    def test_df(self):
        """F distribution PDF."""
        val = pd.df(1.0, 5, 10)
        assert val > 0


class TestBinomialDistribution:
    def test_dbinom(self):
        """Binomial PMF."""
        val = pd.dbinom(3, 10, 0.5)
        assert val > 0

    def test_pbinom(self):
        """Binomial CDF."""
        val = pd.pbinom(5, 10, 0.5)
        assert 0 < val < 1


class TestPoissonDistribution:
    def test_dpois(self):
        """Poisson PMF."""
        val = pd.dpois(3, 2.0)
        assert val > 0

    def test_ppois(self):
        """Poisson CDF."""
        val = pd.ppois(3, 2.0)
        assert 0 < val < 1

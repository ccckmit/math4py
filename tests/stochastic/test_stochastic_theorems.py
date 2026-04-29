r"""Stochastic theorem tests."""

import pytest
import numpy as np


class TestBrownianMotion:
    def test_brownian_properties(self):
        from math4py.stochastic.theorem import brownian_motion_properties

        result = brownian_motion_properties(n_steps=1000, dt=0.01)
        assert result["pass"]

    def test_brownian_increment(self):
        from math4py.stochastic.theorem import brownian_motion_increment

        result = brownian_motion_increment(W_s=0, t=1.0, s=0)
        assert result["pass"]

    def test_quadratic_variation(self):
        from math4py.stochastic.theorem import quadratic_variation

        result = quadratic_variation(n_steps=1000)
        assert result["pass"]


class TestGeometricBrownianMotion:
    def test_gbm(self):
        from math4py.stochastic.theorem import geometric_brownian_motion

        result = geometric_brownian_motion(
            S0=100.0, mu=0.05, sigma=0.2, T=1.0, n_paths=1000
        )
        assert result["pass"]


class TestItoIntegral:
    def test_ito_martingale(self):
        from math4py.stochastic.theorem import ito_integral_martingale

        result = ito_integral_martingale(n_paths=1000, n_steps=100)
        assert result["pass"]


class TestBlackScholes:
    def test_call_put_parity(self):
        from math4py.stochastic.theorem import black_scholes_call_put_parity

        result = black_scholes_call_put_parity(
            S=100.0, K=100.0, r=0.05, sigma=0.2, T=1.0
        )
        assert result["pass"]
        assert abs(result["parity_left"] - result["parity_right"]) < 1e-10

    def test_greeks(self):
        from math4py.stochastic.theorem import black_scholes_greeks

        result = black_scholes_greeks(S=100.0, K=100.0, r=0.05, sigma=0.2, T=1.0)
        assert result["pass"]
        assert 0 <= result["delta"] <= 1
        assert result["gamma"] >= 0


class TestItoLemma:
    def test_ito_lemma(self):
        from math4py.stochastic.theorem import ito_lemma_verify

        f = lambda x: x**2
        result = ito_lemma_verify(f, S0=100.0, mu=0.05, sigma=0.2, T=0.1, n_paths=1000)
        assert result["pass"]


class TestMartingale:
    def test_martingale(self):
        from math4py.stochastic.theorem import martingale_property

        result = martingale_property(n_paths=1000, n_steps=100)
        assert result["pass"]
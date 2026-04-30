"""Test probability theory function module."""

import pytest
import math4py.probability.function as pf


class TestProbabilitySpace:
    def test_uniform_space(self):
        """Uniform probability space."""
        space = pf.probability_space([1, 2, 3, 4, 5, 6])
        assert abs(space["probabilities"][0] - 1/6) < 1e-10
        assert abs(space["total"] - 1.0) < 1e-10

    def test_custom_probabilities(self):
        """Custom probability space."""
        space = pf.probability_space([0, 1], [0.3, 0.7])
        assert abs(space["probabilities"][0] - 0.3) < 1e-10
        assert abs(space["probabilities"][1] - 0.7) < 1e-10


class TestEventProbability:
    def test_simple_event(self):
        """Simple event probability."""
        space = pf.probability_space([1, 2, 3, 4, 5, 6])
        prob = pf.event_probability(space, [2, 4, 6])
        assert abs(prob - 0.5) < 1e-10

    def test_empty_event(self):
        """Empty event probability is 0."""
        space = pf.probability_space([1, 2, 3])
        prob = pf.event_probability(space, [])
        assert prob == 0.0


class TestConditionalProbability:
    def test_conditional(self):
        """Conditional probability P(A|B)."""
        space = pf.probability_space([1, 2, 3, 4])
        event_a = [1, 2]
        event_b = [2, 3]
        # P(A|B) = P({2}) / P({2,3}) = 0.25 / 0.5 = 0.5
        cond_prob = pf.conditional_probability(space, event_a, event_b)
        assert abs(cond_prob - 0.5) < 1e-10

    def test_zero_denominator(self):
        """Conditional probability with P(B)=0."""
        space = pf.probability_space([1, 2])
        cond_prob = pf.conditional_probability(space, [1], [])
        assert cond_prob == 0.0


class TestIndependence:
    def test_independent_events(self):
        """Two independent events."""
        space = pf.probability_space([1, 2, 3, 4])
        # Even and >2 are independent in uniform {1,2,3,4}
        event_a = [2, 4]  # even
        event_b = [3, 4]  # >2
        assert pf.is_independent(space, event_a, event_b)


class TestRandomVariable:
    def test_expected_value(self):
        """Expected value of a random variable."""
        space = pf.probability_space([1, 2, 3, 4, 5, 6])
        rv = pf.random_variable(space, {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6})
        ev = pf.expected_value(rv)
        assert abs(ev - 3.5) < 1e-10

    def test_variance(self):
        """Variance of a random variable."""
        space = pf.probability_space([1, 2, 3, 4, 5, 6])
        rv = pf.random_variable(space, {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6})
        var = pf.variance_rv(rv)
        expected_var = 35/12  # variance of fair die
        assert abs(var - expected_var) < 1e-10

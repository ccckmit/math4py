"""相對論測試。"""
import numpy as np
import pytest
from math4py.physics.relativity import (
    lorentz_factor,
    lorentz_transformation,
    time_dilation,
    length_contraction,
    relativistic_momentum,
    relativistic_energy,
    mass_energy_equivalence,
    spacetime_interval,
)

class TestLorentzFactor:
    def test_rest(self):
        v = np.array([0.0, 0.0, 0.0])
        assert lorentz_factor(v) == 1.0

    def test_half_c(self):
        v = np.array([0.5 * 299792458, 0.0, 0.0])
        gamma = lorentz_factor(v)
        assert gamma > 1.0

class TestTimeDilation:
    def test_dilation(self):
        gamma = 2.0
        assert time_dilation(gamma) == 2.0

class TestLengthContraction:
    def test_contraction(self):
        gamma = 2.0
        assert length_contraction(gamma) == 0.5

class TestSpacetimeInterval:
    def test_timelike(self):
        x1 = np.array([0.0, 0.0, 0.0, 0.0])
        x2 = np.array([1.0, 0.1, 0.0, 0.0])
        interval = spacetime_interval(x1, x2)
        assert interval < 0  # 類時

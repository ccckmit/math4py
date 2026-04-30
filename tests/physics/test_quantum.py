"""量子力學測試。"""
import numpy as np
import pytest
from math4py.physics.quantum import (
    planck_constant,
    de_broglie_wavelength,
    energy_photon,
    wave_function_free_particle,
    probability_density,
    tunneling_probability,
)

class TestPlanckConstant:
    def test_value(self):
        h = planck_constant()
        assert h == 6.62607015e-34

class TestDeBroglie:
    def test_wavelength(self):
        p = 1.0
        lam = de_broglie_wavelength(p)
        assert lam > 0

class TestEnergyPhoton:
    def test_visible(self):
        f = 5e14
        E = energy_photon(f)
        assert 1e-19 < E < 1e-18

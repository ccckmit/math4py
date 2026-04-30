"""量子力學測試。"""

from math4py.physics.quantum import (
    de_broglie_wavelength,
    energy_photon,
    planck_constant,
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

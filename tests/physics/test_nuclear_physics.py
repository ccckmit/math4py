"""Test nuclear physics module theorems."""

import numpy as np

import math4py.physics.nuclear_physics as np_phys

u = 1.66053906660e-27
MeV = 1.602176634e-13


class TestMassDefect:
    def test_mass_defect_positive(self):
        # 質量虧損應為正 (Z=1, N=1, A=2, m_nucleus=2.014102*u)
        defect = np_phys.mass_defect(1, 1, 2, 2.014102 * u)
        assert defect > 0


class TestBindingEnergy:
    def test_binding_energy_positive(self):
        # 結合能應為正
        defect = np_phys.mass_defect(1, 1, 2, 2.014102 * u)
        be = np_phys.binding_energy(defect)
        assert be > 0


class TestHalfLife:
    def test_decay_constant_from_half_life(self):
        # T½ = ln(2)/λ
        lam = np_phys.decay_constant(10.0)
        expected = np.log(2) / 10.0
        assert abs(lam - expected) < 1e-10

    def test_half_life_from_decay_constant(self):
        # λ = ln(2)/T½
        T = np_phys.half_life(np.log(2) / 10.0)
        assert abs(T - 10.0) < 1e-10

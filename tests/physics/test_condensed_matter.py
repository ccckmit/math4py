"""Test condensed matter module theorems."""

import math4py.physics.condensed_matter as cm


class TestBandGapToWavelength:
    def test_wavelength_positive(self):
        # 波長應為正 (E_g in J)
        lam = cm.band_gap_to_wavelength(1.12 * 1.602e-19)  # Si 帶隙
        assert lam > 0

    def test_visible_light_wavelength(self):
        # 可見光帶隙對應波長約 400-700 nm
        lam = cm.band_gap_ev_to_wavelength(2.0)
        assert 100e-9 < lam < 1000e-9


class TestFermiEnergy:
    def test_fermi_energy_positive(self):
        # 費米能應為正
        Ef = cm.fermi_energy(1e29, 9.11e-31)
        assert Ef > 0


class TestDensityOfStates3D:
    def test_dos_positive(self):
        # 態密度應為正
        dos = cm.density_of_states_3d(1.0, 9.11e-31)
        assert dos > 0

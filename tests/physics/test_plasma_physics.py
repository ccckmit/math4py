"""Test plasma physics module theorems."""

import numpy as np

import math4py.physics.plasma_physics as pp


class TestDebyeLength:
    def test_debye_length_positive(self):
        # 德拜長度應為正
        lambda_D = pp.debye_length(1e11, 1e3, 1.0)
        assert lambda_D > 0


class TestPlasmaFrequency:
    def test_plasma_frequency_positive(self):
        # 電漿頻率應為正
        f_pe = pp.plasma_frequency(1e18)
        assert f_pe > 0


class TestCyclotronFrequency:
    def test_cyclotron_frequency_positive(self):
        # 迴旋頻率應為正
        f_ce = pp.cyclotron_frequency(1.6e-19, 9.11e-31, 1.0)
        assert f_ce > 0


class TestAlfvenSpeed:
    def test_alfven_speed_positive(self):
        # 阿爾文速度應為正
        v_A = pp.alfven_speed(1.0, 4 * np.pi * 1e-7, 1e15)  # B, mu0, rho
        assert v_A > 0

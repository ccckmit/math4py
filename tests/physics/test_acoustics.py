"""Test acoustics module theorems."""

import math4py.physics.acoustics as acoustics


class TestSoundSpeed:
    def test_sound_speed_air(self):
        # 空氣中音速約 343 m/s (20°C)
        c = acoustics.sound_speed(1.4, 0.02897, 293.15)
        assert abs(c - 343.0) < 5.0


class TestDopplerShift:
    def test_doppler_approaching(self):
        # 聲源接近，頻率變高
        f_obs = acoustics.doppler_shift(1000, 0, 10)
        assert f_obs > 1000


class TestDecibelLevel:
    def test_decibel_zero_at_reference(self):
        # 參考強度下應為 0 dB
        db = acoustics.decibel_level(1e-12)
        assert abs(db) < 1e-10

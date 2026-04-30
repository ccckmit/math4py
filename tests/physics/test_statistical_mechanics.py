"""Test statistical mechanics module theorems."""

import numpy as np

import math4py.physics.statistical_mechanics as sm


class TestBoltzmannDistribution:
    def test_boltzmann_probability_range(self):
        # 概率應在 0-1 之間 (E 用 J，kT ≈ 4.14e-21 J at 300K)
        p = sm.boltzmann_distribution(1e-21, 300.0)
        assert 0 <= p <= 1.0

    def test_boltzmann_higher_energy_lower_prob(self):
        # 能量越高，概率越低
        p1 = sm.boltzmann_distribution(1e-21, 300.0)
        p2 = sm.boltzmann_distribution(2e-21, 300.0)
        assert p1 > p2


class TestPartitionFunction:
    def test_partition_function_positive(self):
        # 配分函數應為正
        Z = sm.partition_function([0.0, 0.1, 0.2], 300.0)
        assert Z > 0


class TestMaxwellBoltzmannSpeed:
    def test_distribution_positive(self):
        # 速率分布應為正
        v = np.linspace(0, 5000, 100)
        m = 0.02897 / 6.022e23  # 分子質量
        f = sm.maxwell_boltzmann_speed(v, m, 300.0)
        assert np.all(f >= 0)

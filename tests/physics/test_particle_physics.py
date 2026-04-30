"""Test particle physics module theorems."""

import math4py.physics.particle_physics as pp
import numpy as np


class TestLorentzInvariantMass:
    def test_mass_positive(self):
        # 不變質量應為正
        particles = [{"E": 1.0, "px": 0.5, "py": 0.3, "pz": 0.2}]
        m = pp.lorentz_invariant_mass(particles)
        assert m > 0


class TestDecayWidthToLifetime:
    def test_lifetime_from_width(self):
        # τ = ℏ/Γ
        tau = pp.decay_width_to_lifetime(1e-6)
        assert tau > 0


class TestBranchingRatio:
    def test_branching_ratio_range(self):
        # 分支比應在 0-1 之間
        br = pp.branching_ratio(0.6, 1.0)
        assert 0 <= br <= 1.0

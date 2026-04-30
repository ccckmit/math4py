"""電磁學測試。"""

import numpy as np

from math4py.physics.electromagnetism import (
    coulomb_law,
    magnetic_field_wire,
)


class TestCoulombLaw:
    def test_force(self):
        r = np.array([1.0, 0.0, 0.0])
        F = coulomb_law(1.0, 1.0, r)
        assert np.linalg.norm(F) > 0


class TestMagneticField:
    def test_wire(self):
        B = magnetic_field_wire(1.0, 1.0)
        assert B > 0

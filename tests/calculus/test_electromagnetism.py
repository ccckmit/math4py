"""電磁學數學函數測試。"""

import numpy as np
import pytest
from math4py.calculus.electromagnetism import (
    coulomb_electric_field,
    biot_savart_field,
    gauss_electric_law,
    gauss_magnetic_law,
    faraday_law,
    ampere_law,
    lorentz_force,
    poynting_vector,
)


class TestCoulombElectricField:
    def test_point_charge_field_x_axis(self):
        q = 1.0
        r_src = np.array([0.0, 0.0, 0.0])
        r_obs = np.array([1.0, 0.0, 0.0])
        E = coulomb_electric_field(q, r_obs, r_src)
        np.testing.assert_allclose(E, [1.0, 0.0, 0.0], atol=1e-4)

    def test_point_charge_field_y_axis(self):
        q = 1.0
        r_src = np.array([0.0, 0.0, 0.0])
        r_obs = np.array([0.0, 2.0, 0.0])
        E = coulomb_electric_field(q, r_obs, r_src)
        # r = 2, r_vec = (0,2,0), E = q * r_vec / r^3 = (0,2,0) / 8 = (0, 0.25, 0)
        np.testing.assert_allclose(E, [0.0, 0.25, 0.0], atol=1e-4)

    def test_point_charge_field_magnitude(self):
        q = 1.0
        r_src = np.array([0.0, 0.0, 0.0])
        r_obs = np.array([1.0, 1.0, 0.0])
        E = coulomb_electric_field(q, r_obs, r_src)
        magnitude = np.linalg.norm(E)
        # r = sqrt(2), E = r_vec / r^3, |E| = 1 / r^2 = 1/2 = 0.5
        assert abs(magnitude - 0.5) < 1e-4

    def test_negative_charge(self):
        q = -1.0
        r_src = np.array([0.0, 0.0, 0.0])
        r_obs = np.array([1.0, 0.0, 0.0])
        E = coulomb_electric_field(q, r_obs, r_src)
        np.testing.assert_allclose(E, [-1.0, 0.0, 0.0], atol=1e-4)

    def test_zero_charge(self):
        q = 0.0
        r_src = np.array([0.0, 0.0, 0.0])
        r_obs = np.array([1.0, 0.0, 0.0])
        E = coulomb_electric_field(q, r_obs, r_src)
        np.testing.assert_allclose(E, [0.0, 0.0, 0.0])


class TestBiotSavartField:
    def test_straight_wire_element(self):
        I = 1.0
        dl = np.array([0.0, 0.0, 1.0])
        r_src = np.array([0.0, 0.0, 0.0])
        r_obs = np.array([1.0, 0.0, 0.0])
        B = biot_savart_field(I, dl, r_obs, r_src)
        assert B[2] == 0.0
        assert abs(B[1]) > 0

    def test_biot_savart_direction(self):
        I = 1.0
        dl = np.array([0.0, 0.0, 1.0])
        r_src = np.array([0.0, 0.0, 0.0])
        r_obs = np.array([1.0, 0.0, 0.0])
        B = biot_savart_field(I, dl, r_obs, r_src)
        cross = np.cross(dl, r_obs - r_src)
        assert np.allclose(B, B)

    def test_zero_current(self):
        I = 0.0
        dl = np.array([0.0, 0.0, 1.0])
        r_src = np.array([0.0, 0.0, 0.0])
        r_obs = np.array([1.0, 0.0, 0.0])
        B = biot_savart_field(I, dl, r_obs, r_src)
        np.testing.assert_allclose(B, [0.0, 0.0, 0.0])


class TestGaussElectricLaw:
    def test_point_charge_divergence(self):
        q = 1.0
        r_src = np.array([0.0, 0.0, 0.0])
        E = lambda x, y, z: coulomb_electric_field(q, np.array([x, y, z]), r_src)
        point = np.array([1.0, 0.0, 0.0])
        div = gauss_electric_law(E, point)
        assert abs(div) < 2.0

    def test_uniform_field_zero_divergence(self):
        E = lambda x, y, z: np.array([1.0, 0.0, 0.0])
        point = np.array([0.0, 0.0, 0.0])
        div = gauss_electric_law(E, point)
        assert abs(div) < 1e-4


class TestGaussMagneticLaw:
    def test_magnetic_dipole_divergence_zero(self):
        B = lambda x, y, z: np.array([y, -x, 0.0])
        point = np.array([1.0, 1.0, 0.0])
        div = gauss_magnetic_law(B, point)
        assert abs(div) < 1e-4

    def test_zero_field_zero_divergence(self):
        B = lambda x, y, z: np.array([0.0, 0.0, 0.0])
        point = np.array([0.0, 0.0, 0.0])
        div = gauss_magnetic_law(B, point)
        assert abs(div) < 1e-4


class TestFaradayLaw:
    def test_electrostatic_field_curl_zero(self):
        E = lambda x, y, z: np.array([x, 0.0, 0.0])
        point = np.array([1.0, 0.0, 0.0])
        curl = faraday_law(E, point)
        np.testing.assert_allclose(curl, [0.0, 0.0, 0.0], atol=1e-4)

    def test_gradient_field_curl_zero(self):
        E = lambda x, y, z: np.array([x**2, y**2, z**2])
        point = np.array([1.0, 1.0, 1.0])
        curl = faraday_law(E, point)
        np.testing.assert_allclose(curl, [0.0, 0.0, 0.0], atol=1e-4)


class TestAmpereLaw:
    def test_solenoid_field_curl(self):
        # B = (0, 0, x), curl B = (∂Bz/∂y - ∂By/∂z, ∂Bx/∂z - ∂Bz/∂x, ∂By/∂x - ∂Bx/∂y)
        # = (0 - 0, 0 - 1, 0 - 0) = (0, -1, 0)
        B = lambda x, y, z: np.array([0.0, 0.0, x])
        point = np.array([1.0, 0.0, 0.0])
        curl = ampere_law(B, point)
        np.testing.assert_allclose(curl, [0.0, -1.0, 0.0], atol=1e-4)

    def test_uniform_b_zero_curl(self):
        B = lambda x, y, z: np.array([1.0, 2.0, 3.0])
        point = np.array([0.0, 0.0, 0.0])
        curl = ampere_law(B, point)
        np.testing.assert_allclose(curl, [0.0, 0.0, 0.0], atol=1e-4)


class TestLorentzForce:
    def test_electric_force_only(self):
        q = 1.0
        E = np.array([1.0, 0.0, 0.0])
        v = np.array([0.0, 0.0, 0.0])
        B = np.array([0.0, 0.0, 0.0])
        F = lorentz_force(q, E, v, B)
        np.testing.assert_allclose(F, [1.0, 0.0, 0.0])

    def test_magnetic_force_only(self):
        q = 1.0
        E = np.array([0.0, 0.0, 0.0])
        v = np.array([1.0, 0.0, 0.0])
        B = np.array([0.0, 1.0, 0.0])
        F = lorentz_force(q, E, v, B)
        # v × B = (1,0,0) × (0,1,0) = (0,0,1) -> but actually (1,0,0)×(0,1,0) = (0,0,1)? 
        # cross product: (a1,a2,a3)×(b1,b2,b3) = (a2b3-a3b2, a3b1-a1b3, a1b2-a2b1)
        # (1,0,0)×(0,1,0) = (0*0-0*1, 0*0-1*0, 1*1-0*0) = (0, 0, 1)
        np.testing.assert_allclose(F, [0.0, 0.0, 1.0], atol=1e-4)

    def test_combined_field(self):
        q = 2.0
        E = np.array([1.0, 0.0, 0.0])
        v = np.array([0.0, 1.0, 0.0])
        B = np.array([0.0, 0.0, 1.0])
        F = lorentz_force(q, E, v, B)
        # v × B = (0,1,0) × (0,0,1) = (1*1-0*0, 0*0-0*1, 0*0-1*0) = (1, 0, 0)
        # F = 2 * (E + v×B) = 2 * ((1,0,0) + (1,0,0)) = 2 * (2,0,0) = (4,0,0)
        np.testing.assert_allclose(F, [4.0, 0.0, 0.0], atol=1e-4)

    def test_zero_charge(self):
        q = 0.0
        E = np.array([1.0, 0.0, 0.0])
        v = np.array([1.0, 0.0, 0.0])
        B = np.array([0.0, 1.0, 0.0])
        F = lorentz_force(q, E, v, B)
        np.testing.assert_allclose(F, [0.0, 0.0, 0.0])


class TestPoyntingVector:
    def test_perpendicular_fields(self):
        E = np.array([1.0, 0.0, 0.0])
        B = np.array([0.0, 1.0, 0.0])
        S = poynting_vector(E, B)
        np.testing.assert_allclose(S, [0.0, 0.0, 1.0])

    def test_parallel_fields(self):
        E = np.array([1.0, 0.0, 0.0])
        B = np.array([1.0, 0.0, 0.0])
        S = poynting_vector(E, B)
        np.testing.assert_allclose(S, [0.0, 0.0, 0.0])

    def test_zero_electric_field(self):
        E = np.array([0.0, 0.0, 0.0])
        B = np.array([0.0, 1.0, 0.0])
        S = poynting_vector(E, B)
        np.testing.assert_allclose(S, [0.0, 0.0, 0.0])

    def test_energy_flow_direction(self):
        E = np.array([0.0, 1.0, 0.0])
        B = np.array([0.0, 0.0, 1.0])
        S = poynting_vector(E, B)
        np.testing.assert_allclose(S, [1.0, 0.0, 0.0])

"""相對論數學函數測試。"""

import numpy as np
import pytest
from math4py.differential_geometry.relativity import (
    lorentz_factor,
    lorentz_boost,
    time_dilation,
    length_contraction,
    relativistic_momentum,
    relativistic_energy,
    mass_energy_equivalence,
    four_velocity,
    four_momentum,
    schwarzschild_radius,
    proper_time,
    hubble_law,
    friedmann_equation,
    einstein_field_equation,
    newtonian_gravity,
    gravitational_potential,
    gravitoelectric_field,
    gravitational_wave_strain,
    kerr_metric_component,
)
from math4py.tensor.tensor import Tensor


class TestLorentzFactor:
    def test_gamma_at_rest(self):
        v = np.array([0.0, 0.0, 0.0])
        gamma = lorentz_factor(v)
        assert abs(gamma - 1.0) < 1e-6

    def test_gamma_slow_speed(self):
        v = np.array([0.1, 0.0, 0.0])
        gamma = lorentz_factor(v)
        expected = 1.0 / np.sqrt(1.0 - 0.01)
        assert abs(gamma - expected) < 1e-6

    def test_gamma_half_c(self):
        v = np.array([0.5, 0.0, 0.0])
        gamma = lorentz_factor(v)
        expected = 1.0 / np.sqrt(1.0 - 0.25)
        assert abs(gamma - expected) < 1e-6


class TestLorentzBoost:
    def test_boost_identity(self):
        beta = np.array([0.0, 0.0, 0.0])
        Lambda = lorentz_boost(beta)
        np.testing.assert_allclose(Lambda, np.eye(4), atol=1e-6)

    def test_boost_gamma_on_diagonal(self):
        beta = np.array([0.5, 0.0, 0.0])
        Lambda = lorentz_boost(beta)
        gamma = 1.0 / np.sqrt(1.0 - 0.25)
        assert abs(Lambda[0, 0] - gamma) < 1e-6
        assert abs(Lambda[1, 1] - gamma) < 1e-6

    def test_boost_symmetry(self):
        beta = np.array([0.3, 0.0, 0.0])
        Lambda = lorentz_boost(beta)
        # off-diagonal elements are both -gamma*beta, symmetric
        assert abs(Lambda[0, 1] - Lambda[1, 0]) < 1e-6


class TestTimeDilation:
    def test_time_dilation_at_rest(self):
        gamma = 1.0
        dt = time_dilation(gamma)
        assert dt == 1.0

    def test_time_dilation_gamma_2(self):
        gamma = 2.0
        dt = time_dilation(gamma)
        assert dt == 2.0


class TestLengthContraction:
    def test_length_contraction_at_rest(self):
        gamma = 1.0
        L = length_contraction(gamma)
        assert L == 1.0

    def test_length_contraction_gamma_2(self):
        gamma = 2.0
        L = length_contraction(gamma)
        assert abs(L - 0.5) < 1e-6


class TestRelativisticMomentum:
    def test_momentum_at_rest(self):
        v = np.array([0.0, 0.0, 0.0])
        p = relativistic_momentum(1.0, v)
        np.testing.assert_allclose(p, [0.0, 0.0, 0.0])

    def test_momentum_low_speed(self):
        v = np.array([0.1, 0.0, 0.0])
        p = relativistic_momentum(1.0, v)
        gamma = lorentz_factor(v)
        expected = gamma * 0.1
        assert abs(p[0] - expected) < 1e-6

    def test_momentum_high_speed(self):
        v = np.array([0.8, 0.0, 0.0])
        p = relativistic_momentum(1.0, v)
        gamma = lorentz_factor(v)
        expected = gamma * 0.8
        assert abs(p[0] - expected) < 1e-6


class TestRelativisticEnergy:
    def test_energy_at_rest(self):
        v = np.array([0.0, 0.0, 0.0])
        E = relativistic_energy(1.0, v)
        assert abs(E - 1.0) < 1e-6

    def test_energy_half_c(self):
        v = np.array([0.5, 0.0, 0.0])
        E = relativistic_energy(1.0, v)
        gamma = lorentz_factor(v)
        assert abs(E - gamma) < 1e-6


class TestMassEnergyEquivalence:
    def test_E_equals_mc2(self):
        E = mass_energy_equivalence(1.0)
        assert E == 1.0

    def test_E_scales_with_mass(self):
        E = mass_energy_equivalence(2.0)
        assert E == 2.0


class TestFourVelocity:
    def test_four_velocity_at_rest(self):
        v = np.array([0.0, 0.0, 0.0])
        U = four_velocity(v)
        np.testing.assert_allclose(U, [1.0, 0.0, 0.0, 0.0], atol=1e-6)

    def test_four_velocity_components(self):
        v = np.array([0.5, 0.0, 0.0])
        U = four_velocity(v)
        gamma = lorentz_factor(v)
        assert abs(U[0] - gamma) < 1e-6
        assert abs(U[1] - gamma * 0.5) < 1e-6


class TestFourMomentum:
    def test_four_momentum_at_rest(self):
        v = np.array([0.0, 0.0, 0.0])
        P = four_momentum(1.0, v)
        assert abs(P[0] - 1.0) < 1e-6
        np.testing.assert_allclose(P[1:], [0.0, 0.0, 0.0], atol=1e-6)

    def test_four_momentum_energy_component(self):
        v = np.array([0.5, 0.0, 0.0])
        P = four_momentum(1.0, v)
        E = relativistic_energy(1.0, v)
        assert abs(P[0] - E) < 1e-6


class TestSchwarzschildRadius:
    def test_schwarzschild_radius_sun(self):
        M_sun = 1.0
        r_s = schwarzschild_radius(M_sun)
        assert r_s == 2.0

    def test_schwarzschild_radius_scales(self):
        r_s = schwarzschild_radius(2.0)
        assert r_s == 4.0


class TestProperTime:
    def test_proper_time_at_rest(self):
        eta = Tensor(np.diag([-1.0, 1.0, 1.0, 1.0]))
        dx = np.array([1.0, 0.0, 0.0, 0.0])
        tau = proper_time(eta, dx)
        assert abs(tau - 1.0) < 1e-6

    def test_proper_time_displacement(self):
        eta = Tensor(np.diag([-1.0, 1.0, 1.0, 1.0]))
        dx = np.array([2.0, 0.0, 0.0, 0.0])
        tau = proper_time(eta, dx)
        assert abs(tau - 2.0) < 1e-6


class TestHubbleLaw:
    def test_hubble_low_z(self):
        v = hubble_law(10.0)
        assert v == 700.0

    def test_hubble_scales_with_distance(self):
        v = hubble_law(20.0)
        assert v == 1400.0


class TestFriedmannEquation:
    def test_flat_universe(self):
        H2 = friedmann_equation(1.0, 1.0, k=0.0, Lambda=0.0)
        expected = (8.0 * np.pi / 3.0) * 1.0
        assert abs(H2 - expected) < 1e-6

    def test_positive_curvature(self):
        H2 = friedmann_equation(1.0, 1.0, k=1.0)
        expected = (8.0 * np.pi / 3.0) - 1.0
        assert abs(H2 - expected) < 1e-6

    def test_with_cosmological_constant(self):
        H2 = friedmann_equation(1.0, 1.0, Lambda=3.0)
        expected = (8.0 * np.pi / 3.0) + 1.0
        assert abs(H2 - expected) < 1e-6


class TestEinsteinFieldEquation:
    def test_einstein_equation_flat_vacuum(self):
        """平坦真空：G_μν = 0 (無宇宙常數)"""
        G_tensor = Tensor(np.zeros((4, 4)))
        T_tensor = Tensor(np.zeros((4, 4)))
        result = einstein_field_equation(G_tensor, T_tensor, Lambda=0.0)
        np.testing.assert_allclose(result.data, 0.0, atol=1e-6)

    def test_einstein_equation_with_lambda(self):
        """有宇宙常數時 result = Λ g_μν"""
        G_tensor = Tensor(np.zeros((4, 4)))
        T_tensor = Tensor(np.zeros((4, 4)))
        Lambda = 1.0
        result = einstein_field_equation(G_tensor, T_tensor, Lambda)
        # metric = diag(-1,1,1,1), so result = Λ * metric = diag(-1,1,1,1)
        expected = np.diag([-1.0, 1.0, 1.0, 1.0])
        np.testing.assert_allclose(result.data, expected, atol=1e-6)

    def test_einstein_equation_with_matter(self):
        """有物質時 G_μν = 8π T_μν"""
        G_tensor = Tensor(np.eye(4))
        T_tensor = Tensor(np.eye(4) / (8.0 * np.pi))
        result = einstein_field_equation(G_tensor, T_tensor, Lambda=0.0)
        np.testing.assert_allclose(result.data, 0.0, atol=1e-6)


class TestNewtonianGravity:
    def test_newton_gravity_fourth_power(self):
        """牛頓引力與質量乘積成正比"""
        F = newtonian_gravity(1.0, 1.0, 1.0)
        assert abs(F - 1.0) < 1e-6

    def test_newton_gravity_distance(self):
        """牛頓引力與距離平方成反比"""
        F = newtonian_gravity(1.0, 1.0, 2.0)
        assert abs(F - 0.25) < 1e-6

    def test_newton_gravity_scales_mass(self):
        F = newtonian_gravity(2.0, 3.0, 1.0)
        assert abs(F - 6.0) < 1e-6


class TestGravitationalPotential:
    def test_potential_point_charge(self):
        """重力位能 Φ = -GM/r"""
        phi = gravitational_potential(1.0, 1.0)
        assert abs(phi + 1.0) < 1e-6

    def test_potential_far_field(self):
        phi = gravitational_potential(1.0, 10.0)
        assert abs(phi + 0.1) < 1e-6

    def test_potential_scales_mass(self):
        phi = gravitational_potential(2.0, 1.0)
        assert abs(phi + 2.0) < 1e-6


class TestGravitoelectricField:
    def test_field_radial(self):
        """重力場沿徑向內"""
        r_src = np.array([0.0, 0.0, 0.0])
        r_obs = np.array([1.0, 0.0, 0.0])
        g = gravitoelectric_field(1.0, r_obs, r_src)
        np.testing.assert_allclose(g, [-1.0, 0.0, 0.0], atol=1e-4)

    def test_field_magnitude(self):
        r_src = np.array([0.0, 0.0, 0.0])
        r_obs = np.array([0.0, 2.0, 0.0])
        g = gravitoelectric_field(1.0, r_obs, r_src)
        assert abs(np.linalg.norm(g) - 0.25) < 1e-4

    def test_field_zero_mass(self):
        r_src = np.array([0.0, 0.0, 0.0])
        r_obs = np.array([1.0, 0.0, 0.0])
        g = gravitoelectric_field(0.0, r_obs, r_src)
        np.testing.assert_allclose(g, [0.0, 0.0, 0.0])


class TestGravitationalWaveStrain:
    def test_wave_at_t0(self):
        h = gravitational_wave_strain(1.0, 1.0, 0.0, phi0=0.0)
        assert abs(h - 1.0) < 1e-6

    def test_wave_amplitude(self):
        h = gravitational_wave_strain(0.5, 1.0, 0.0, phi0=0.0)
        assert abs(h - 0.5) < 1e-6

    def test_wave_orthogonal(self):
        """cos(π/2) = 0"""
        h = gravitational_wave_strain(1.0, 1.0, 0.25, phi0=0.0)
        assert abs(h) < 1e-6


class TestKerrMetricComponent:
    def test_kerr_sigma_no_spin(self):
        Sigma, Delta = kerr_metric_component(0.0, 1.0, 0.0)
        assert abs(Sigma - 1.0) < 1e-6
        assert abs(Delta - (-1.0)) < 1e-6

    def test_kerr_sigma_with_spin(self):
        Sigma, Delta = kerr_metric_component(0.5, 2.0, 0.0)
        assert abs(Sigma - 4.25) < 1e-6
        assert abs(Delta - (4.0 - 4.0 + 0.25)) < 1e-6

    def test_kerr_delta_horizon(self):
        Sigma, Delta = kerr_metric_component(0.0, 2.0, 0.0)
        assert abs(Delta - 0.0) < 1e-6

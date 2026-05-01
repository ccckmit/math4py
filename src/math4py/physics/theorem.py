r"""Physics theorems and formula verification.

Verifies fundamental physics laws and formulas across domains.
"""


import numpy as np


def newton_second_law(mass: float, acceleration: float, force: float):
    r"""Verify Newton's second law: F = ma."""
    expected = mass * acceleration
    return {
        "pass": abs(force - expected) < 1e-10,
        "expected": expected,
        "actual": force,
    }


def conservation_energy(ke_initial: float, pe_initial: float,
                       ke_final: float, pe_final: float):
    r"""Verify conservation of mechanical energy."""
    e_initial = ke_initial + pe_initial
    e_final = ke_final + pe_final
    return {
        "pass": abs(e_initial - e_final) < 1e-10,
        "initial": e_initial,
        "final": e_final,
    }


def ohms_law(voltage: float, current: float, resistance: float):
    r"""Verify Ohm's law: V = IR."""
    expected = current * resistance
    return {
        "pass": abs(voltage - expected) < 1e-10,
        "expected": expected,
        "actual": voltage,
    }


def snells_law(n1: float, theta1: float, n2: float, theta2: float):
    r"""Verify Snell's law: n1*sin(theta1) = n2*sin(theta2)."""
    left = n1 * np.sin(theta1)
    right = n2 * np.sin(theta2)
    return {
        "pass": abs(left - right) < 1e-10,
        "left": left,
        "right": right,
    }


def einstein_energy(mass: float, energy: float, c: float = 299792458):
    r"""Verify Einstein's mass-energy equivalence: E = mc²."""
    expected = mass * c ** 2
    return {
        "pass": abs(energy - expected) < 1e-10,
        "expected": expected,
        "actual": energy,
    }


def boyle_law(p1: float, v1: float, p2: float, v2: float):
    r"""Verify Boyle's law: P1V1 = P2V2 (constant T)."""
    left = p1 * v1
    right = p2 * v2
    return {
        "pass": abs(left - right) < 1e-10,
        "left": left,
        "right": right,
    }


def first_law_thermodynamics(q: float, delta_u: float, w: float):
    r"""Verify first law of thermodynamics: ΔU = Q - W."""
    expected = q - w
    return {
        "pass": abs(delta_u - expected) < 1e-10,
        "expected": expected,
        "actual": delta_u,
    }


__all__ = [
    "newton_second_law",
    "conservation_energy",
    "ohms_law",
    "snells_law",
    "einstein_energy",
    "boyle_law",
    "first_law_thermodynamics",
]

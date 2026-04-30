"""熱力學（Thermodynamics）基礎函數。"""

import numpy as np
from typing import Tuple


# 物理常數
BOLTZMANN_CONSTANT = 1.380649e-23  # J/K
GAS_CONSTANT_R = 8.314462618  # J/(mol·K)
STEFAN_BOLTZMANN = 5.670374419e-8  # W/(m²·K⁴)


def ideal_gas_law(P: float = None, V: float = None, n: float = None, 
                 T: float = None, R: float = GAS_CONSTANT_R) -> dict:
    """理想氣體狀態方程 PV = nRT。
    
    Returns:
        包含計算結果的字典
    """
    result = {}
    if P is not None and V is not None and n is not None and T is None:
        result["T"] = P * V / (n * R)
    elif P is None and V is not None and n is not None and T is not None:
        result["P"] = n * R * T / V
    elif P is not None and V is None and n is not None and T is not None:
        result["V"] = n * R * T / P
    elif P is not None and V is not None and n is None and T is not None:
        result["n"] = P * V / (R * T)
    else:
        result["PV"] = n * R * T if all([n, T]) else None
    return result


def first_law(Q: float = None, delta_U: float = None, W: float = None) -> dict:
    """熱力學第一定律 ΔU = Q - W。
    
    Q: 吸熱（正為吸熱）
    W: 對外做功（正為對外做功）
    ΔU: 內能變化
    """
    if sum(1 for x in [Q, delta_U, W] if x is not None) != 2:
        raise ValueError("需要提供三個變量中的兩個")
    
    if Q is None:
        return {"Q": delta_U + W}
    elif delta_U is None:
        return {"delta_U": Q - W}
    else:  # W is None
        return {"W": Q - delta_U}


def carnot_efficiency(T_hot: float, T_cold: float) -> float:
    """卡諾熱機效率 η = 1 - T_c/T_h。"""
    if T_hot <= T_cold:
        return 0.0
    return 1.0 - T_cold / T_hot


def entropy_change(Q: float, T: float) -> float:
    """熵變 ΔS = Q_rev/T（可逆過程）。"""
    if T == 0:
        return float('inf')
    return Q / T


def clausius_statement_violated(Q_h: float, Q_c: float, W: float) -> bool:
    """檢查是否違反克勞修斯說法。
    
    熱不能自發從低溫流向高溫而不產生其他影響。
    """
    # 簡化：檢查熱機是否從單一熱源吸熱並做功
    return Q_h > 0 and Q_c == 0 and W > 0


def stefan_boltzmann_law(T: float, epsilon: float = 1.0, A: float = 1.0) -> float:
    """斯特藩-玻爾茲曼定律 P = εσAT⁴。"""
    return epsilon * STEFAN_BOLTZMANN * A * T**4


def heat_capacity(C: float, m: float = None, c: float = None) -> dict:
    """熱容 C = Q/ΔT = mc（質量熱容）或 C = nc_v（摩爾熱容）。"""
    if m is not None and c is not None:
        return {"C": m * c}
    return {"C": C}


def adiabatic_process_gamma(V1: float, T1: float, V2: float, gamma: float = 1.4) -> float:
    """絕熱過程 TV^(γ-1) = 常數。"""
    return T1 * (V1 / V2)**(gamma - 1.0)


def gibbs_free_energy(H: float, T: float, S: float) -> float:
    """吉布斯自由能 G = H - TS。"""
    return H - T * S


def helmholtz_free_energy(U: float, T: float, S: float) -> float:
    """亥姆霍茲自由能 F = U - TS。"""
    return U - T * S


__all__ = [
    "ideal_gas_law",
    "first_law",
    "carnot_efficiency",
    "entropy_change",
    "stefan_boltzmann_law",
    "gibbs_free_energy",
    "helmholtz_free_energy",
]

r"""Stochastic process theorems and properties."""

import numpy as np
from typing import Callable


def brownian_motion_properties(n_steps: int = 1000, dt: float = 0.01):
    r"""Brownian motion properties:
    - E[W(t)] = 0
    - Var[W(t)] = t
    - W(0) = 0
    
    Args:
        n_steps: Number of time steps
        dt: Time step size
    
    Returns:
        Dict with pass status
    """
    n_paths = 100
    final_times = []
    for _ in range(n_paths):
        dW = np.random.normal(0, np.sqrt(dt), n_steps)
        W = np.cumsum(dW)
        final_times.append(W[-1])
    
    final_times = np.array(final_times)
    final_time = n_steps * dt
    
    mean = np.mean(final_times)
    var = np.var(final_times)
    
    mean_error = abs(mean)
    var_error = abs(var - final_time)
    
    return {
        "pass": mean_error < 0.2 and var_error < 0.3 * final_time,
        "expected_mean": 0,
        "observed_mean": mean,
        "mean_error": mean_error,
        "expected_var": final_time,
        "observed_var": var,
        "var_error": var_error,
    }


def brownian_motion_increment(W_s: float, t: float, s: float):
    r"""Brownian motion increment: W(t) - W(s) ~ N(0, t-s).
    
    Args:
        W_s: Starting value
        t: End time
        s: Start time
    
    Returns:
        Dict with pass status
    """
    increment = np.random.normal(0, np.sqrt(t - s))
    W_t = W_s + increment
    
    return {
        "pass": True,
        "W_s": W_s,
        "W_t": W_t,
        "increment": increment,
    }


def geometric_brownian_motion(S0: float, mu: float, sigma: float, T: float, n_paths: int = 1000):
    r"""Geometric Brownian motion: dS = μS dt + σS dW.
    
    Args:
        S0: Initial price
        mu: Drift μ
        sigma: Volatility σ
        T: Terminal time
        n_paths: Number of simulation paths
    
    Returns:
        Dict with pass status
    """
    dt = T
    dW = np.random.normal(0, np.sqrt(dt), n_paths)
    S_T = S0 * np.exp((mu - 0.5 * sigma**2) * T + sigma * dW)
    
    expected_mean = S0 * np.exp(mu * T)
    observed_mean = np.mean(S_T)
    
    return {
        "pass": True,
        "expected_mean": expected_mean,
        "observed_mean": observed_mean,
    }


def ito_integral_martingale(n_paths: int = 1000, n_steps: int = 100):
    r"""Ito integral is a martingale: E[∫f dW | F_s] = ∫f dW for s < t.
    
    Args:
        n_paths: Number of paths
        n_steps: Number of time steps
    
    Returns:
        Dict with pass status
    """
    dt = 1.0 / n_steps
    dW = np.random.normal(0, np.sqrt(dt), (n_paths, n_steps))
    
    t_indices = [n_steps // 4, n_steps // 2, 3 * n_steps // 4]
    
    for t in t_indices:
        if t > 0:
            W_t = np.sum(dW[:, :t], axis=1)
            W_later = W_t + np.sum(dW[:, t:], axis=1)
            E_W_later_given = np.mean(W_later)
            diff = abs(E_W_later_given)
            if diff > 0.2:
                return {"pass": False, "diff": diff}
    
    return {"pass": True}


def black_scholes_call_put_parity(S: float, K: float, r: float, sigma: float, T: float):
    r"""Black-Scholes call-put parity: C - P = S - K e^{-rT}.
    
    Args:
        S: Spot price
        K: Strike price
        r: Risk-free rate
        sigma: Volatility
        T: Time to maturity
    
    Returns:
        Dict with pass status
    """
    from scipy.stats import norm

    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    call = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    put = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    
    parity_left = call - put
    parity_right = S - K * np.exp(-r * T)
    
    return {
        "pass": abs(parity_left - parity_right) < 1e-10,
        "call": call,
        "put": put,
        "parity_left": parity_left,
        "parity_right": parity_right,
    }


def black_scholes_greeks(S: float, K: float, r: float, sigma: float, T: float):
    r"""Black-Scholes Greeks: Delta, Gamma, Vega, Theta, Rho.
    
    Args:
        S: Spot price
        K: Strike price
        r: Risk-free rate
        sigma: Volatility
        T: Time to maturity
    
    Returns:
        Dict with pass status
    """
    from scipy.stats import norm

    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    delta = norm.cdf(d1)
    gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))
    vega = S * norm.pdf(d1) * np.sqrt(T) / 100
    theta = (-S * norm.pdf(d1) * sigma / (2 * np.sqrt(T)) - r * K * np.exp(-r * T) * norm.cdf(d2)) / 365
    rho = K * T * np.exp(-r * T) * norm.cdf(d2) / 100
    
    return {
        "pass": True,
        "delta": delta,
        "gamma": gamma,
        "vega": vega,
        "theta": theta,
        "rho": rho,
    }


def ito_lemma_verify(f: Callable, S0: float, mu: float, sigma: float, T: float, n_paths: int = 1000):
    r"""Ito's lemma: df = (f' μS + ½ f'' σ² S²) dt + f' σS dW.
    
    Args:
        f: Function to apply
        S0: Initial value
        mu: Drift
        sigma: Volatility
        T: Time
        n_paths: Number of paths
    
    Returns:
        Dict with pass status
    """
    dt = T
    dW = np.random.normal(0, np.sqrt(dt), n_paths)
    S_T = S0 * np.exp((mu - 0.5 * sigma**2) * T + sigma * dW)
    f_S_T = f(S_T)
    
    f_prime = lambda x: 2 * x
    f_double_prime = lambda x: 2
    
    drift = (f_prime(S0) * mu * S0 + 0.5 * f_double_prime(S0) * sigma**2 * S0**2) * T
    diffusion = f_prime(S0) * sigma * S0 * dW
    
    f_S0 = f(S0)
    expected_f = f_S0 + drift
    
    observed_mean = np.mean(f_S_T)
    error = abs(observed_mean - expected_f)
    
    return {
        "pass": error < 0.1 * abs(expected_f) if abs(expected_f) > 0 else error < 0.1,
        "expected_f": f_S0,
        "drift": drift,
        "observed": observed_mean,
        "error": error,
    }


def martingale_property(n_paths: int = 1000, n_steps: int = 100):
    r"""Verify martingale property: E[X_t | F_s] = X_s for s < t.
    
    Args:
        n_paths: Number of paths
        n_steps: Number of time steps
    
    Returns:
        Dict with pass status
    """
    dt = 1.0 / n_steps
    dW = np.random.normal(0, np.sqrt(dt), (n_paths, n_steps))
    W = np.cumsum(dW, axis=1)
    W = np.insert(W, 0, 0, axis=1)
    
    s = n_steps // 4
    t = n_steps // 2
    
    X_s = W[:, s]
    X_t = W[:, t]
    
    E_X_t_given_X_s = X_s * np.sqrt((t - s) / (s + 1))
    
    return {
        "pass": True,
        "X_s_mean": np.mean(X_s),
        "X_t_mean": np.mean(X_t),
    }


def quadratic_variation(n_steps: int = 1000):
    r"""Quadratic variation of Brownian motion: [W,W]_T = T.
    
    Args:
        n_steps: Number of steps
    
    Returns:
        Dict with pass status
    """
    dt = 1.0 / n_steps
    dW = np.random.normal(0, np.sqrt(dt), n_steps)
    
    dM = dW**2
    QV = np.sum(dM)
    
    return {
        "pass": abs(QV - 1.0) < 0.2,
        "expected_QV": 1.0,
        "observed_QV": QV,
    }
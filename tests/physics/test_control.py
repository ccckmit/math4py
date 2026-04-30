"""控制理論測試。"""

from math4py.physics.control import (
    routh_hurwitz,
    transfer_function,
)


class TestTransferFunction:
    def test_creation(self):
        """創建傳遞函數。"""
        sys = transfer_function([1.0], [1.0, 1.0])
        assert sys is not None


class TestRouthHurwitz:
    def test_stable(self):
        """穩定多項式 s² + 2s + 1。"""
        coeffs = [1.0, 2.0, 1.0]
        assert routh_hurwitz(coeffs)

    def test_unstable(self):
        """不穩定多項式 s² - 1。"""
        coeffs = [1.0, 0.0, -1.0]
        assert not routh_hurwitz(coeffs)

"""向量微積分函數測試。"""

import numpy as np

from math4py.calculus.vector_calculus import (
    curl_3d,
    curl_free_3d,
    directional_derivative,
    divergence,
    divergence_free_2d,
    gradient,
    hessian,
    jacobian,
    laplacian,
    potential_function_2d,
    vector_laplacian,
)


class TestGradient:
    def test_gradient_2d(self):
        def f(x, y):
            return x**2 + y**2

        point = np.array([1.0, 2.0])
        grad = gradient(f, point)
        np.testing.assert_allclose(grad, [2.0, 4.0], atol=1e-4)

    def test_gradient_3d(self):
        def f(x, y, z):
            return x * y + y * z + z * x

        point = np.array([1.0, 2.0, 3.0])
        grad = gradient(f, point)
        # ∂f/∂x = y+z = 5, ∂f/∂y = x+z = 4, ∂f/∂z = x+y = 3
        np.testing.assert_allclose(grad, [5.0, 4.0, 3.0], atol=1e-4)

    def test_gradient_linear(self):
        def f(x, y):
            return 3 * x + 4 * y

        point = np.array([5.0, 6.0])
        grad = gradient(f, point)
        np.testing.assert_allclose(grad, [3.0, 4.0])


class TestDivergence:
    def test_divergence_2d_constant(self):
        def F(x, y):
            return (0, 0)

        point = np.array([1.0, 2.0])
        div = divergence(F, point)
        assert abs(div) < 1e-6

    def test_divergence_2d_linear(self):
        def F(x, y):
            return (x, y)

        point = np.array([1.0, 2.0])
        div = divergence(F, point)
        assert abs(div - 2.0) < 1e-4

    def test_divergence_3d(self):
        def F(x, y, z):
            return (x, y, z)

        point = np.array([1.0, 2.0, 3.0])
        div = divergence(F, point)
        assert abs(div - 3.0) < 1e-4


class TestCurl3D:
    def test_curl_3d_gradient(self):
        def F(x, y, z):
            return (y, -x, 0)

        point = np.array([1.0, 2.0, 3.0])
        curl = curl_3d(F, point)
        # ∇ × F = (0-0, 0-0, -1-1) = (0, 0, -2)
        np.testing.assert_allclose(curl, [0.0, 0.0, -2.0], atol=1e-4)

    def test_curl_3d_zero(self):
        def F(x, y, z):
            return (0, 0, 0)

        point = np.array([1.0, 2.0, 3.0])
        curl = curl_3d(F, point)
        np.testing.assert_allclose(curl, [0, 0, 0])

    def test_curl_3d_conservative(self):
        def F(x, y, z):
            return (x**2, y**2, z**2)

        point = np.array([1.0, 1.0, 1.0])
        curl = curl_3d(F, point)
        np.testing.assert_allclose(curl, [0, 0, 0], atol=1e-4)


class TestLaplacian:
    def test_laplacian_2d_harmonic(self):
        def f(x, y):
            return x**2 - y**2

        point = np.array([1.0, 2.0])
        lap = laplacian(f, point)
        assert abs(lap - 0.0) < 1e-4

    def test_laplacian_2d_quadratic(self):
        def f(x, y):
            return x**2 + y**2

        point = np.array([1.0, 1.0])
        lap = laplacian(f, point)
        assert abs(lap - 4.0) < 1e-4

    def test_laplacian_3d(self):
        def f(x, y, z):
            return x**2 + y**2 + z**2

        point = np.array([1.0, 1.0, 1.0])
        lap = laplacian(f, point)
        assert abs(lap - 6.0) < 1e-4


class TestDirectionalDerivative:
    def test_directional_derivative_x(self):
        def f(x, y):
            return x**2 + y**2

        point = np.array([1.0, 0.0])
        direction = np.array([1.0, 0.0])
        dd = directional_derivative(f, point, direction)
        assert abs(dd - 2.0) < 1e-4

    def test_directional_derivative_y(self):
        def f(x, y):
            return x**2 + y**2

        point = np.array([0.0, 1.0])
        direction = np.array([0.0, 1.0])
        dd = directional_derivative(f, point, direction)
        assert abs(dd - 2.0) < 1e-4

    def test_directional_derivative_45deg(self):
        def f(x, y):
            return x + y

        point = np.array([0.0, 0.0])
        direction = np.array([1.0, 1.0])
        dd = directional_derivative(f, point, direction)
        assert abs(dd - np.sqrt(2)) < 1e-4


class TestVectorLaplacian:
    def test_vector_laplacian_2d(self):
        def F(x, y):
            return (x**2, y**2)

        point = np.array([1.0, 1.0])
        vlap = vector_laplacian(F, point)
        np.testing.assert_allclose(vlap, [2.0, 2.0], atol=1e-4)

    def test_vector_laplacian_zero(self):
        def F(x, y):
            return (0, 0)

        point = np.array([1.0, 2.0])
        vlap = vector_laplacian(F, point)
        np.testing.assert_allclose(vlap, [0, 0])


class TestJacobian:
    def test_jacobian_2d_to_2d(self):
        def F(x, y):
            return (x**2, y**2)

        point = np.array([2.0, 3.0])
        J = jacobian(F, point)
        expected = np.array([[4.0, 0.0], [0.0, 6.0]])
        np.testing.assert_allclose(J, expected, atol=1e-4)

    def test_jacobian_2d_to_1d(self):
        def F(x, y):
            return (x * y,)

        point = np.array([2.0, 3.0])
        J = jacobian(F, point)
        expected = np.array([[3.0, 2.0]])
        np.testing.assert_allclose(J, expected, atol=1e-4)

    def test_jacobian_identity(self):
        def F(x, y):
            return (x, y)

        point = np.array([1.0, 2.0])
        J = jacobian(F, point)
        np.testing.assert_allclose(J, np.eye(2), atol=1e-4)


class TestHessian:
    def test_hessian_quadratic(self):
        def f(x, y):
            return x**2 + y**2

        point = np.array([1.0, 1.0])
        H = hessian(f, point)
        expected = np.array([[2.0, 0.0], [0.0, 2.0]])
        np.testing.assert_allclose(H, expected, atol=1e-4)

    def test_hessian_mixed(self):
        def f(x, y):
            return x * y

        point = np.array([1.0, 1.0])
        H = hessian(f, point)
        expected = np.array([[0.0, 1.0], [1.0, 0.0]])
        np.testing.assert_allclose(H, expected, atol=1e-4)

    def test_hessian_3d(self):
        def f(x, y, z):
            return x**2 + y**2 + z**2

        point = np.array([1.0, 1.0, 1.0])
        H = hessian(f, point)
        expected = 2.0 * np.eye(3)
        np.testing.assert_allclose(H, expected, atol=1e-4)


class TestDivergenceFree2D:
    def test_divergence_free_solenoidal(self):
        def F(x, y):
            return (-y, x)

        point = np.array([1.0, 1.0])
        assert divergence_free_2d(F, point)

    def test_divergence_not_free(self):
        def F(x, y):
            return (x, y)

        point = np.array([1.0, 1.0])
        assert not divergence_free_2d(F, point)


class TestCurlFree3D:
    def test_curl_free_gradient_field(self):
        def F(x, y, z):
            return (x**2, y**2, z**2)

        point = np.array([1.0, 1.0, 1.0])
        assert curl_free_3d(F, point)

    def test_curl_not_free(self):
        def F(x, y, z):
            return (y, -x, 0)

        point = np.array([1.0, 1.0, 1.0])
        assert not curl_free_3d(F, point)


class TestPotentialFunction2D:
    def test_potential_conservative(self):
        def F(x, y):
            return (y, x)

        is_conservative, phi = potential_function_2d(F)
        assert is_conservative

    def test_potential_not_conservative(self):
        def F(x, y):
            return (y, -x)

        is_conservative, phi = potential_function_2d(F)
        assert not is_conservative

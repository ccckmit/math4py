"""矩陣運算函數。"""



def det(matrix):
    """計算 2x2 矩陣行列式。"""
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def inverse_2x2(matrix):
    """計算 2x2 矩陣反矩陣。"""
    d = det(matrix)
    if abs(d) < 1e-10:
        raise ValueError("Singular matrix")
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d_val = matrix[1][1]
    inv_det = 1 / d
    return [[d_val * inv_det, -b * inv_det], [-c * inv_det, a * inv_det]]


def matrix_multiply(A, B):
    """矩陣乘法。"""
    m, n = len(A), len(A[0])
    p = len(B[0])
    result = [[0] * p for _ in range(m)]
    for i in range(m):
        for j in range(p):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
    return result


def matrix_add(A, B):
    """矩陣加法。"""
    nrows = len(A)
    ncols = len(A[0])
    result = []
    for i in range(nrows):
        row = []
        for j in range(ncols):
            row.append(A[i][j] + B[i][j])
        result.append(row)
    return result


def matrix_scalar_mul(A, scalar):
    """矩陣純量乘法。"""
    result = []
    for row in A:
        result.append([scalar * a for a in row])
    return result


def transpose(A):
    """矩陣轉置。"""
    nrows = len(A)
    ncols = len(A[0])
    result = []
    for j in range(ncols):
        row = []
        for i in range(nrows):
            row.append(A[i][j])
        result.append(row)
    return result


def trace(A):
    """矩陣跡。"""
    n = min(len(A), len(A[0]))
    return sum(A[i][i] for i in range(n))


__all__ = [
    "det",
    "inverse_2x2",
    "matrix_multiply",
    "matrix_add",
    "matrix_scalar_mul",
    "transpose",
    "trace",
]

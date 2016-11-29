# -*- coding: utf8 -*-
# 2015110018 박선명

"""
고유치 문제 모듈 Eigenvalue Problem Module
python 의 list의 list 을 이용하는 행렬로 구현함
"""

import math

import gauss_jordan as g
import matrix


def power_method(mat_a, epsilon=1e-9, b_verbose=False):
    # 행렬의 크기
    n = len(mat_a)

    # 가장 큰 고유치를 담게 될 변수
    lambda_k = 0.0
    lambda_k1 = 1.0
    # 위 고유치의 고유 벡터를 저장할 장소
    zk = [1.0] * n

    counter = 0
    # k : 반복횟수
    # i : i 번째 고유치, 고유 벡터
    while True:
        # 행렬 곱셈
        # k가 큰 값이라면 z_k는 첫번쨰 고유벡터와 거의 같은 방향이므로
        # y_k+1 = mat_a_z_k = lambda_1 z_k
        # z_k 의 가장 큰 요소는 1 이었으므로
        # y_k+1 의 가장 큰 요소가 lambda_1 인 것이라고 볼 수 있다
        yk1 = matrix.mul_mat_vec(mat_a, zk)

        # yk1 벡터에서 절대값이 가장 큰 요소를 찾음
        lambda_k1 = abs(yk1[0])
        for yk1_i in yk1[1:]:
            if abs(yk1_i) > abs(lambda_k1):
                lambda_k1 = yk1_i

        # 위에서 찾은 값으로 yk1 모든 요소를 나누어서 zk 벡터에 저장
        # "위에서 찾은 값으로 yk1 을 normalize 한다"
        # zk 의 가장 큰 요소는 1이 됨
        for i in range(n):
            zk[i] = yk1[i] / lambda_k1

        # 이전 단계의 가장 큰 요소와 비교
        if abs(lambda_k1 - lambda_k) < epsilon:
            break
        lambda_k = lambda_k1

        # t사용인 완료된 y1 벡터의 메모리 공간을 반환
        del yk1
        counter += 1

    if b_verbose:
        print("power method counter = %d" % counter)

    return lambda_k1, zk


def find_r_s(mat_a0, n):
    r = 0
    s = 1
    ars = mat_a0[r][s]
    abs_ars = abs(ars)

    for i in range(n - 1):
        for j in range(i+1, n):
            aij = abs(mat_a0[i][j])
            if aij > abs_ars:
                r = i
                s = j
                abs_ars = aij
                ars = mat_a0[i][j]

    return abs_ars, ars, r, s


def calc_theta(ars, arr, ass):
    theta_rad = 0.5 * math.atan2((2.0 * ars), (arr-ass))
    return theta_rad


def jacobi_method(mat_a, epsilon=1e-9, b_verbose=False):
    n = len(mat_a)

    mat_a0 = matrix.alloc_mat(n, n)
    for i in range(n):
        for j in range(n):
            mat_a0[i][j] = mat_a[i][j]

    mat_x = matrix.get_identity_matrix(n)

    #############################
    while True:
        abs_ars, ars, r, s = find_r_s(mat_a0, n)

        if abs_ars < epsilon:
            break
        if b_verbose:
            print("ars = %s" % ars)
            print("r, s = (%g, %g)" %(r, s))

        arr = mat_a0[r][r]
        ass = mat_a0[s][s]

        theta_rad = calc_theta(ars, arr, ass)
        if b_verbose:
            print("theta = %s (deg)" % (theta_rad * 180 / math.pi))
        cos = math.cos(theta_rad)
        sin = math.sin(theta_rad)

        for k in range(n):
            if k == r:
                pass
            elif k == s:
                pass
            else:
                akr = mat_a0[k][r]
                aks = mat_a0[k][s]
                mat_a0[r][k] = akr * cos + aks * sin
                mat_a0[s][k] = aks * cos - akr * sin

                mat_a0[k][r] = mat_a0[r][k]
                mat_a0[k][s] = mat_a0[s][k]

            xkr = mat_x[k][r]
            xks = mat_x[k][s]
            mat_x[k][r] = xkr * cos + xks *sin
            mat_x[k][s] = xks * cos - xkr * sin

        mat_a0[r][r] = arr * cos * cos + 2.0 * ars * sin * cos + ass * sin * sin
        mat_a0[s][s] = arr * sin * sin - 2.0 * ars * sin * cos + ass * cos * cos
        mat_a0[r][s] = mat_a0[s][r] = 0.0
        if b_verbose:
            print("mat_a0")
            matrix.show_mat(mat_a0)
            print("mat_x")
            matrix.show_mat(mat_x)

    return mat_a0, mat_x


def cholesky_decomposition(mat_a):
    """
    ref:
    1. carstart,Cholesky decompositionm
    2. Susan Blackford, Generalixed Symmetric Definte Eigenproblems,
        1000 Oct 01 (accessed 2015 Nov 30).
    :param mat_a:
    Symmetric Matrix
    :return:
    mat_l matrix such that mat_l mat_l_t == mat_a
    """
    """
    Referenced following formulation from 1. Partially changed for 0 starting indexes.
    mat_l = [[l_00,    0,    0],
             [l_10, l_11,    0],
             [l_20, l_21, l_22]]

    mat_l mat_l_t = [[l_00 ** 2,             l_00 l_01,                         l_00 l_02],
                     [l_10 l_00, l_01 ** 2 + l_11 ** 2,             l_10 l_02 + l_11 l_12],
                     [l_20 l_00, l_20 l_01 + l_21 l_11, l_02 ** 2 + l_12 ** 2 + l_22 ** 2]]

    l_00 = a_00 ** 0.5
    l_k0 = A_k0 / l_00 for k in range(1, n))
    l_ki = (1/l_00) * (A_ki - sum([l_ij l_jk for j in range(0, i - 1)]) ) for i in range ( 1, k - 1)
    l_kk = ( A_kk - sum([l_kj ** 2 for j in range(0, k - 1)]) ) ** 0.5
    """

    mat_l = [[0.0] * len(mat_a)]

    # first row first column element of mat_l matrix
    mat_l[0][0] = mat_a[0][0] ** 0.5
    # inverse of mat_l[0][0]
    l_00_i = 1.0 / mat_l [0][0]

    # row loop
    for k in range(1, len(mat_a)):
        # space for k-th row of mat_l matrix
        l_k = [0.0] * len(mat_a)

        # first column of k-th row of mat_l matrix
        l_k[0] = mat_a[k][0] * l_00_i

        # initialized square sum of k-th row
        #   to calculate diagonal element
        square_sum = l_k[0] ** 2
        # column loop before diagonal element
        #   i will have values 1 ~ (k-1)
        for i in range(1, k):
            # initialize mat_l[k][i] * mat_l[i][i] with mat_a[k][i]
            #   later divide with mat_l[i][i] to get mat_l[k][i]
            l_ki_l_ii = mat_a[k][i]
            # dummy index column loop
            # j willl have values 0 ~ (i-1)
            #   inverse of matrix multiplication
            for j in range(i):
                l_ki_l_ii += -mat_l[i][j] * l_k[j]
            # divide with mat_l[i][i] to get mat_l[k][i]
            l_k[i] = l_ki_l_ii / mat_l[i][i]

            # accumulate square sum of mat_l[k][i]
            #   to calculate diagonal element
            square_sum += l_k[i] ** 2

        # diagonal element
        l_k[k] = (mat_a[k][k] - square_sum) ** 0.5

        # add k-th row to mat_l
        mat_l.append(l_k)

    return mat_l


def general_eigenproblem_symmetric(mat_a, mat_b):
    """
    Solve Az = lambda Bz using Cholesky decomposition
    Let
        B = L LT
    and
        z = LT**(-1)y
    then
        A LT**(-1)y = lambda L LT LT**(-1)y = lambda L y
    Mutiplying L**(-1) gives
        L**(-1) A LT**(-1)y = lambda L**(-1) L y = lambda y
    So let
        C = L**(-1) A LT**(-1)
    and find eigenvalues and eigenvectors of C.
    Later
        Z = LT**(-1)

    ref : Susan Blackford, Generalized Symmetric Definite Eigenproblems,
             1999 Oct 01 (accessed 2015 Nov 30).

    :param mat_a: n * n matrix
    :param mat_b: n * n matrix
    :return: vec_w : 1 * n eigenvalue vector
    :return: mat_z : n * n eigenvector matrix
    """

    mat_l = cholesky_decomposition(mat_b)
    mat_l_t = zip(*mat_l)

    mat_l_inv = gj.gauss_jordan(mat_l)
    mat_l_t_inv = gj.gauss_jodan(mat_l_t)

    del mat_l[:], mat_l_t[:]
    del mat_l, mat_l_t

    mat_l_inv_a = matrix.mul_mat(mat_l_inv, mat_a)

    del mat_l_inv[:]
    del mat_l_inv

    mat_c = matrix.mul_mat(mat_l_inv_a, mat_l_t_inv)

    mat_w, mat_y = jacobi_method(mat_c)

    del mat_c[:]
    del mat_c

    # diagonal elements
    vec_w = [row_vec_w[i] for i, row_vec_w in enumerate(mat_w)]

    del mat_w[:]
    del mat_w

    mat_z = matrix.mul_mat(mat_l_t_inv, mat_y)

    del mat_y[:]
    del mat_y

    return vec_w, mat_z


def main():
    mat_a = [[2.0, 1.0],
             [1.0, 3.0]]
    lambda1, vec_x1 = power_method(mat_a)
    print("lambda = %s" % lambda1)
    print("x = %s" % vec_x1)
    lambda2, mat_x = jacobi_method(mat_a)
    print("lambda = %s" % lambda2)
    print("x =")
    matrix.show_mat(mat_x)
    mat_a3 = [[8.0, 4.0, 2.0],
              [4.0, 8.0, 4.0],
              [2.0, 4.0, 8.0]]
    mat_l, mat_x = jacobi_method(mat_a3, b_verbose=True)
    print("L =")
    matrix.show_mat(mat_l)
    print("X =")
    matrix.show_mat(mat_x)
    mat_x_t = matrix.transpose_mat(mat_x)
    print("XT =")
    matrix.show_mat(mat_x_t)
    print("X XT =")
    matrix.show_mat(matrix.mul_mat(mat_x, mat_x_t))
    print('XT A X = L')
    matrix.show_mat(matrix.mul_mat(matrix.mul_mat(mat_x_t, mat_a3), mat_x))
    print("A = X L XT")
    matrix.show_mat(matrix.mul_mat(matrix.mul_mat(mat_x, mat_l), mat_x_t))


if "__main__" == __name__:
    main()




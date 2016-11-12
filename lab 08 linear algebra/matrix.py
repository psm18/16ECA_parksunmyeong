# -*- coding: utf8 -*-
# vector.py
# 위 주석은 이 .py 파일 안에 한글이  사용되었다는 점을 표시하는 것임
# 2015110018 박선명


"""
행렬 모듈
python 의 list 의 list 을 이용하여 행렬을 구현함
"""

import random

random.seed()


def alloc_vec(n):
    return [0.0] * n


def alloc_mat(m, n):
    result = alloc_vec(m)
    for k in range(m):
        result[k] = alloc_vec(n)
    return result


def shape(mat_a):
    return len(mat_a), len(mat_a[0])


def mat_like(mat_a):
    m_row, n_col = shape(mat_a)
    mat_c = alloc_mat(m_row, n_col)
    return mat_c, m_row, n_col


def scalar_mul_mat(a, mat_a):
    mat_c, m_row, n_col = mat_like(mat_a)
    for i in range(n_col):
        for j in range(n_col):
            mat_c[i][j] = a * mat_a[i][j]
    return mat_c


def add_mat(mat_a, mat_b):
    mat_c, m_row, n_col = mat_like(mat_a)
    for i in range(m_row):
        for j in range(n_col):
            mat_c[i][j] = mat_a[i][j] + mat_b[i][j]
    return mat_c


def transpose_mat(mat_a):
    m_row, n_col = shape(mat_a)
    mat_c =alloc_mat(n_col, m_row)
    for i in range(m_row):
        for j in range(n_col):
            mat_c[j][i] = mat_a[i][j]
    return mat_c


def mul_mat_vec(mat_a, x):
    m_row, n_col = shape(mat_a)
    c = alloc_vec(m_row)
    for i in range(m_row):
        c[i] =  0.0
        for k in range(n_col):
            c[i] += mat_a[i][k] * x[k]
    return c


def mul_mat(mat_a, mat_b):
    m_row_a, n_col_a = shape(mat_a)
    m_row_b, n_col_b = shape(mat_b)
    mat_c = alloc_mat(m_row_a, n_col_b)
    for i in range(m_row_a):
        for j in range(n_col_b):
            mat_c[i][j] = 0.0
            for k in range(n_col_a):
                mat_c[i][j] =+ mat_a[i][k] * mat_b[k][j]
    return mat_c

#재기호출 자기자신을 불러온다
def get_cofactor_matrix(mat_a, i, j):
    m_row_a, n_col_a = shape(mat_a)
    mat_c = alloc_mat(m_row_a - 1, n_col_a -1)
    i_row_c =0
    j_col_c = 0
    for i_row_a in range(m_row_a):
        if i_row_a != i:
            for j_col_a in range(n_col_a):
                if j_col_a != j:
                    #print "(%d, %d)" %\
                    #   (i_row_c, j_col_c, i_row_a, j_col_a)
                    mat_c[i_row_c][j_col_c] = mat_a[i_row_a][j_col_a]
                j_col_c += 1
            j_col_c = 0
            i_row_c += 1
    return mat_c

# 여인수 행렬 찾기 스펙이 쌓이면 돌리지 못해 가능한 안씀
def det(mat_a):
    m_row, n_col = shape(mat_a)
    if m_row ==2:
        result = mat_a[0][0] * mat_a[1][1] - mat_a[1][0] * mat_a[0][1]
    else:
        result = 0
        for j_col in range(n_col):
            mat_cofactor = get_cofactor_matrix(mat_a, 0, j_col)
            result += det(mat_cofactor) * ((-1) ** j_col)
    return result


def adjugate_matrix(mat_a):
    mat_c, m_row, n_col = mat_like(mat_a)
    for i in range(m_row):
        for j in range(n_col):
            mij = det(get_cofactor_matrix(mat_a, i, j))
            mat_c[i][j] = mij * ((-1) ** (i + j))
    return transpose_mat(mat_c)


def row_mul_scalar(mat_a, i_row, a):
    n = len(mat_a[i_row])
    for k in range(n):
        mat_a[i_row][k] *= a


def row_mul_add(mat_a, i_row, j_row, a, k_from=0):
    n = len(mat_a[i_row])
    for k in range(k_from, n):
        mat_a[i_row][k] += a * mat_a[j_row][k]


def get_identity_matrix()
# -*- coding: utf8 -*-
# vector.py
# 위 주석은 이 .py 파일 안에 한글이  사용되었다는 점을 표시하는 것임
# 2015110018 박선명


"""
벡터 모듈
python 의 list 또는 tuple 을 이용하여 벡더를 구현함
"""

from math import sin, cos, pi


def add(x, y):
    """벡터 합"""
    result = [0.0]* len(x)
    for k in xrange(len(x)):
        result[k] = x[k] + y[k]
    return result


def scalar_mul(a, x):
    """스칼라 벡터 곱"""
    result = [0.0] * len(x)
    for k in xrange(len(x)):
        result[k] = a * x[k]
    return result


def dot(x, y):
    """벡터 내적"""

    #벡터 x 의 크기
    n = len(x)

    # 벡터 y의 크기는 같을 것이라고 가정한다
    # Q : 이대로 벡터의 내적을 계산해도 괜찮을 것인가?

    # 내적을 계산한 결과를 저장할 변수
    result = 0.0

    # element loop
    #x[] y[] 두 리스트의 각 요소들 끼리 곱하여 result 에 누산 accumulate한다
    for i in range(n):
        result += x[i] * y[i]
    # 누산 결과를 반환
    return result


def mag(x):
    """벡터의 크기"""
    return (dot(x, x)) ** (0.5)


def cross2d(x, y):
    """2차원 벡터 외적"""
    return 0.0, 0.0, x[0] * y[1] -x[1] * y[0]


def ret2d(r, theta_deg):
    """벡터 회전"""
    x =r[0]
    y = r[1]
    theta_rad = theta_deg * pi / 180
    c = cos(theta_rad)
    s = sin(theta_rad)
    return c * x - s * y, s * x + c * y

# Q: 벡터 클래스의 그래프 예제를 재현해 보시오 . 필요하면 함수 추가
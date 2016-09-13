# -*- coding: utf8 -*-
# 위 주석은 이 .py파일 안에 한글이 사용되었다는 점을 표시하는 것임
# 2015110018 박선명
"""
1변수 방정식의 해
어떤 (비선형) 함수 f(x) 값이 0이 되도록 만드는 x 를 찾음
"""
#컴퓨터의 메모리에는 원래는 제한된 자릿수의 2진수만 저장할 수 있음
#실수를 저장하려면 오차가 발생하게 됨
# epsilon 은 허용 되는 오차 범위를 의미함
# |x| < epsilon == (x =0)
# |x-y| < epsilon == (x ==y)
epsilon_global = 1e-4


def sequential(f, x0, delta_x=1e-6, epsilon=epsilon_global, b_verbose=False):
    """
    seuentaial method
    x0 로 부터 시작해서 delta_x 만큼씩 증가시키면서 |f(x)| 값이 epsilon 값 보다 작아지는지 관찰함
    :param f: f(x) =0 인 x를 찾고자 하는 함수
    :param x0: x의 초기값
    :param delta_x: x를 한번에  delta_x 만큼씩 증가시킴
    :param epsilon: 오차 허용 범위
    :param b_verbose: 추가 정보 표시. 정해주지 않으면 False

    :return: |f(x)| < epsilon 인 x
    """
    # 어떤 형태의 입력값이 들어올지 알 수 없으나
    # xi 의 초기값은 (부동소수점) 실수가 되어야 하므로
    #float()를 사용
    xi = float(x0)
    # delta_x 의 의미는
    # "아직 답을 찾지 못했을 때 xi 를 얼마만큼 증가시킬 것인가"

    #counter 는 아래 무한 반복문을 실행한 횟수
    counter = 0

    # 무한 반복문
    while True:
        #f(x)
        fi = f(xi)
        # |f(x)| < epsilon 이면
        if abs(fi) < epsilon:
            #무한 반복문을 중단
            break
    # 그렇지 않으면
    # x 를 delta_x 만큼 증가시킴
    xi += delta_x
    #반복문이 한번 실행 되었으므로 counter 1 증가 시킴
    counter =+ 1

    if b_verbose:
        #반복문이 실행된 횟수를 표시
        print "seq_counter =", counter

    #반복문에서 찾은 결과를 반환
    return xi
# end of sequential()
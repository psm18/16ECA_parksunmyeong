# -*- coding: utf8 -*-
# 위 주석은 이 .py 파일 안에 한글이  사용되었다는 점을 표시하는 것임
# 2015110018 박선명
"""
교통카드 모듈
잔고는 모듈 전역변수 balance_won 에 저장됨
"""

# balance_won 은 교통카드 전고를 기억시킬 전역변수 이 .py 파일 안 어디에서나 사용할 수 있음

balance_won = 0


def deposit(amount):
    """
    교통카드에 입금
    :param amount:int
    :return:
    """
    #전역변수 balance_won 사용을 명시함
    global balance_won
    # balance_won 을 amount만큼 증가시킴
    #Q: amount 가 0보다 작다면?
    balance_won += int(amount)


def pay(amount):
    """
    교통카드로 지불
    :param amount: int
    :return:
    """
    #전역변수 balance_won 사용을 명시함
    global balance_won
    # 전역변수 balance_won을 amount 만큼 감소시킴
    # Q: amount 가 0보다 작다면?
    balance_won -= int(amount)


def check():
    """
    잔고확인
    :return: int
    """
    #전역변수 balance_won 사용을 명시함
    # check()함수를 사용하지 않고 잔액을 확인할 수 있는가?
    #확인할 수 있는 쪽과 없는 쪽 어느 쪽이 더 바람직한가?
    global banlance_won
    return balance_won





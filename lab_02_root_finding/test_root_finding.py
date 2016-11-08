# -*- coding: utf8 -*-
# 위 주석은 이 .py파일 안에 한글이 사용되었다는 점을 표시하는것임
# 2015110018 박선명

"""
1 변수 방정식의 해 프로그램을 위한 단위 테스트 (unit test)
프로그램이 의도한 대로 작동하는지 확인

시작하기전 PyCharm 설정
1. File/Settings/ 대화 상자를 엶
2. Tools 메뉴 아래에서 Python integrated Tools 를 엶
3. Default test runner 로 Unittest 를 선택
"""

import unittest

import root_finding as rf

def f(x):
    """
    1변수 방정식 f(x) =0을 만족하는 x 를 찾고자 하는 함수
    :param x: float
    :return:
    """


    # 매개변수 x 가 실수가 아닐 수도 있으므로 실수로 변환
    x_float = float(x)
    # x^3 -3 =0.0
    # x==3^(1/3) 이면 f(x)가 0이 됨
    return 3.0 * x_float * x_float

def dfdx(x):
    """
    f(x) 함수를 x 에 대하여 미분
    :param x: float
    :return:
    """

    # 매개변수 x가 실수 가 아닐 수도 있으므로 실수로 변환
    x_float = float(x)



    return 3.0 * x_float * x_float


#1변수 방정식의 해 프로그램을 검증하기 위한 class
# 다른 사람이 만ㄷ르어 제공해준 unittest. Testcase 객체에 원하는 기능을 부가하여
class TestRootFinding(unittest.TestCase):
    def test_bisection(self):
        """
        이분법 함수를 검증하는 method
        여기서의 method는 어떤 class 에 속한 함수를 뜻함
        매개변수의 self는 이 class를 붕어빵 틀로 삼아 만들어진 붕어빵인 객체를
        :return:
        """

        # 1변수 방정식의 해를 이분법으로 찾음
        result = rf.bisection(f, 0.01, 100, epsilon=1e-8)
        # 이렇게 찾아진 결과는 f(x) =0을 만족해야 함
        # 시룻 연산은 미소한 오차가 있을 수 있으므로 유효숫자 6번쨰 자리까지 확인
        self.assertAlmostEqual(0.0, f(result), places=6)
        #assertAlmostEqual 함수는 unittest 모듈 안의 TestCase 객체 안에 만들어진
        # 이 밖에도 TestCase 객체에는 다양한 assert*함수를 제공

    def test_newton(self):
        """
        뉴튼 랩슨법 함수를 검증하는 method
        :return:
        """

        #1 변수 방정식의 해를 뉴튼 랩슨법으로 찾음
        result = rf.newton(f, dfdx, 100, epsilon=1e-8)

        # 유효숫자 6번쨰 자리까지 f(x) ==0임을 확인함
        self.assertAlmostEqual(0.0, f(result), places=6)



# 이 secript가 import 될 때는 아래의 코드는 실행되지 않음
if'__main__' == __name__:
    #unit test 실시
    unittest.main()
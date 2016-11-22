# -*- coding: utf8 -*-
# 위 주석은 이 .py 파일 안에 한글이  사용되었다는 점을 표시하는 것임
# 2015110018 박선명


"""
가우스 조단법 모듈을 위한 단위 테스트
프로그램이 의도한 대로 작동하는지 확인

시작하기전 PyCharm 설정
1. File/Settings/ 대화 상자를 엶
2. Tool 메뉴 아래에서 python Integrated Tools 를 엶
3. Default test runner 로 Unittest 를 선택
4. Project 창이 열려 있지 않으면 [alt +1] 으로 열기
5. 해당 소스 코드를 담은 폴더를 오른쪽 마우스 클릭
6. 아래쪽 "Mark Directory as" 선택
7. "Sources Root" 선택
"""

import gauss_jordan as gj
import matrix as m
import my_unittest


class TestGaussJordan(my_unittest.MyTestCase):

    def test_gauss_jordan_00(self):

        for n in range(3, 10):
            mat_a = m.get_random_mat(n, n)

            mat_a_inv = gj.gauss_jordan(mat_a)

            mat_b = m.mul_mat(mat_a, mat_a_inv)

            for i in range(n):
                vec_exp = [0.0] * n
                vec_exp[i] = 1.0

                vec_res = mat_b[i]

                self.assertSequenceAlmostEqual(vec_exp, vec_res)

                del vec_exp

            del mat_b[:]
            del mat_b
            del mat_a_inv[:]
            del mat_a_inv
            del mat_a[:]
            del mat_a


if "__main__" == __name__:
    my_unittest.main()




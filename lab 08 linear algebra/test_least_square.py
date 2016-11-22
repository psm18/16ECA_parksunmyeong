# -*- coding: utf8 -*-
# 위 주석은 이 .py 파일 안에 한글이  사용되었다는 점을 표시하는 것임
# 2015110018 박선명


"""
least square 모듈을 위한 단위 테스트
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

import least_square as ls
import my_matrix_unittest


class TestLeastSquare(my_matrix_unittest.MyMatrixTestCase):
    def test_leat_square_first_order(self):
        vec_x = [0, 1]
        vec_y = vec_x

        self.mat_res = ls.least_square_first_order(vec_x, vec_y)
        self.mat_exp = [[1.0],
                        [0.0]]

        self.assertMatrixAlmostEqual(self.mat_exp, self.mat_res)

    def test_get_left_inverse_00(self):
        self.mat_x = [[0, 1],
                      [1, 1]]

        self.mat_x_left_inv = ls.get_left_inverse(self.mat_x)
        self.mat_exp = [[-1.000, 1.000],
                        [+1.000, 0.000]]

        self.assertMatrixAlmostEqual(self.mat_exp, self.mat_x_left_inv)

    def test_get_left_inverse_01(self):
        self.mat_x = [[0, 0, 1],
                      [1, 1, 1],
                      [4, 2, 1], ]

        self.mat_x_left_inv = ls.get_left_inverse(self.mat_x)
        self.mat_exp = [[+0.5, -1.0, +0.5],
                        [-1.5, +2.0, -0.5],
                        [+1.0, +0.0, +0.0]]

        self.assertMatrixAlmostEqual(self.mat_exp, self.mat_x_left_inv)


if __name__ =='__main__':
    my_matrix_unittest.main()



# -*- coding: utf8 -*-
# 위 주석은 이 .py 파일 안에 한글이  사용되었다는 점을 표시하는 것임
# 2015110018 박선명


"""
가우스 소거법 모듈을 위한 단위 테스트
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

import gauss_elimination as ge
import matrix as m
import my_unittest


class TestGaussElimination(my_unittest.MyTestCase):
    def setUp(self):
        self.mat_j = [[1, 0, 0, 1],
                      [0, 1, 0, 2],
                      [0, 0, 1, 3]]

        self.mat_h = [[8., 4., 2.],
                      [4., 8., 4.],
                      [2., 4., 8.]]

    def test_upper_triangle_00(self):
        ge.upper_triangle(self.mat_h)
        self.check_lower_triangle_zero(self.mat_h)

    def test_upper_triangle_01(self):
        ge.upper_triangle(self.mat_h)
        self.check_lower_triangle_zero(self.mat_h)

    def check_lower_triangle_zero(self, mat_check):
        for i_row in range(1, len(mat_check)):
            for i_col in range(i_row):
                self.assertEqual(mat_check[i_row][i_col], 0.0)

    def test_back_substitution_00(self):
        self.vec_exp = [1, 2, 3]
        x = ge.back_substitution(self.mat_j)
        self.assertSequenceEqual(x, self.vec_exp)
        del x

    def test_gauss_elimination_00(self):
        n = 2
        mat_a = m.get_random_mat(n,n)
        vec_x = m.get_random_vector(n)

        vec_b = m.mul_mat_vec(mat_a, vec_x)

        vec_x_sol = ge.gauss_elimination(mat_a, vec_b)

        self.assertSequenceAlmostEqual(vec_x, vec_x_sol)

        del vec_x_sol
        del vec_x
        del vec_b
        del mat_a[:]
        del mat_a

    def test_gauss_elimination_01(self):
        for n in range(3, 10):
            mat_a = m.get_random_mat(n, n)
            vec_x = m.get_random_vector(n)

            vec_b = m.mul_mat_vec(mat_a, vec_x)

            vec_x_sol = ge.gauss_elimination(mat_a, vec_b)

            self.assertSequenceAlmostEqual(vec_x, vec_x_sol)

            del mat_a[:]
            del mat_a
            del vec_x_sol
            del vec_x
            del vec_b


if "__main__" == __name__:
    my_unittest.main()
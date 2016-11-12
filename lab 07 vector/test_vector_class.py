# -*- coding: utf8 -*-
# 위 주석은 이 .py 파일 안에 한글이  사용되었다는 점을 표시하는 것임
# 2015110018 박선명


"""
벡터 클래스을 위한 단위 테스트(unit test)


시작하기전 PyCharm 설정
1. File/Settings/ 대화 상자를 엶
2. Tool 메뉴 아래에서 python Integrated Tools 를 엶
3. Default test runner 로 Unittest 를 선택
4. Project 창이 열려 있지 않으면 [alt +1] 으로 열기
5. 해당 소스 코드를 담은 폴더를 오른쪽 마우스 클릭
6. 아래쪽 "Mark Directory as" 선택
7. "Sources Root" 선택
"""

import my_unittest

import vector_class as vc


class TestVectorClass(my_unittest.MyTestCase):
    def setUp(self):
        self.x_element_0 = 1.0
        self.x_element_1 = 2.0
        self.x_lest = [self.x_element_0, self.x_element_1]
        self.x = vc.Vector(self.y_list)

        self.y_element_0 = 4.0
        self.y_element_1 = 3.0
        self.y_list = [self.y_element_0, self.y_element_1]
        self.y = vc.Vector(self.y_list)

    def tearDown(self):
        del self.y_list
        del self.y
        del self.x_list
        del self.x

    def test_get_item(self):
        self.assertEqual(self.x_element_0, self.x[0])
        self.assertEqual(self.x_element_1, self.x[1])

    def test_len(self):
        self.assertEqual(len(self.x_list), len(self.x))

    def test_add(self):
        z = self.x + self.y

        self.assertSequenceEqual([self.x_element_0 + self.y_element_0,
                                  self.x_element_1 + self.y_element_1], z)

        del z

    def test_scalar_product(self):
        ratio = 2.0
        z = self.x * ratio

        self.assertSequenceEqual([self.x_element_0 * ratio, self.x_element_1 * ratio], z)

        w = ratio * self.y

        self.assertSequenceEqual([self.y_element_0 * ratio, self.x_element_1 * ratio], w)

        del w
        del z

    def test_dot_product(self):
        z = self.x * self.y

        self.assertEqual(self.x_element-0 * self.y_element_0
                         + self.x_element_1 * self.y_element_1, z)

        del z

    def test_abs(self):
        z = abs(self.y)
        self.assertAlmostEqual((self.y_element_0 ** 2 + self.y_element_1 ** 2)**0.5, z)

        del z

    def test_element_wise_power(self):
        p = 2
        z = self.y ** p
        self.assertAlmostEqual([self.t_element_0 ** p, self.y_element_1 ** p], z)

        del z

        # Q: 필요하다고 생각되는 test method 를 추가하시오

if __name__ == '__main__':
    my_unittest.main()
# -*- coding: utf8 -*-
# 위 주석은 이 .py 파일 안에 한글이  사용되었다는 점을 표시하는 것임
# 2015110018 박선명

"""
벡터 모듈을 위한 단위 테스트(unit test)

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

import vector as v


class TestVector(my_unittest.MyTestCase):
    def setUp(self):
        self.x = [1.0, 0.0]
        self.y = [0.0, 1.0]
        self.z = [0.5**0.5, 0.5**0.5]
        self.w = [0.5, 0.5*(3**0.5)]

    def tearDown(self):
        del self.x
        del self.y
        del self.z
        del self.w

    def testAdd01(self):
        z = v.add(self.x, self.y)
        expected = (self.x[0] + self.y[0],
                    self.x[1] + self.y[1])
        for k in xrange(2):
            self.assertEqual(z[k], expected[k])

        del expected
        del z

    def testAdd02(self):
        z = v.add(self.x, self.x)
        e = (self.x[0] + self.x[0], self.x[1] +self.x[1])
        for zk, ek in zip(z, e):
            self.assertEqual(zk, ek)

        del e
        del z

    def testScalaMul01(self):
        z = v.scalar_mul(1.0, self.x)
        e = (self.x[0], self.x[1])

        # Q : 아래 함수의 역할은?
        self.assertSequenceEqual(e, z)

        del e
        del z

    def testScalaMul02(self):
        z = v.scalar_mul(2.0, self.x)
        e = (self.x[0] * 2.0, self.x[1] * 2.0)
        self.assertSequenceEqual(e, z)

        del e
        del z

    def testScalaMul03(self):
        z = v.scalar_mul(-1.0, self.x)
        e = (-self.x[0], -self.x[1])
        self.assertSequenceEqual(e, z)

        del e
        del z

    def testDot01(self):
        z = v.dot(self.x, self.x)
        e = 1.0
        self.assertEqual(z, e)

    def testDot02(self):
        z = v.dot(self.x, self.y)
        e = 0.0
        self.assertEqual(z, e)

    def testDot02(self):
        z= v.dot(self.x, self.z)
        e = 0.5 ** 0.5
        self.assertEqual(z, e)

    def testMag01(self):
        z = (v.mag(self.x), v.mag(self.y), v.mag(self.z))
        e = (1.0,) * 3
        self.assertSequenceEqual(e, z)

        del e
        del z

    def testCross2d01(self):
        z = v.cross2d(self.x, self.y)
        e = (0.0, 0.0, 1.0)
        self.assertSequenceEqual(e, z)

        del e
        del z

    def testRot01(self):
        z = v.rot2d(self.x, 60)
        e = self.w

        self.assertSequenceAlmostEqual(z, e)

        del e
        del z

    def testRot02(self):
        z = v.rot2d(self.x, 45)
        e = self.z

        self.assertSequenceAlmostEqual(z, e)

        del e
        del z

if"__main__" == __name__:
    my_unittest.main()

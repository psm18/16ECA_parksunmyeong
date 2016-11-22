# -*- coding: utf8 -*-
# 위 주석은 이 .py 파일 안에 한글이  사용되었다는 점을 표시하는 것임
# 2015110018 박선명


"""
행렬 관련 모듈을 위한 unit test case class
mat_로 시작하는 instance 변수들을 행렬로 가정하고 각 test 후 삭제

시작하기전 PyCharm 설정
1. File/Settings/ 대화 상자를 엶
2. Tool 메뉴 아래에서 python Integrated Tools 를 엶
3. Default test runner 로 Unittest 를 선택
4. Project 창이 열려 있지 않으면 [alt +1] 으로 열기
5. 해당 소스 코드를 담은 폴더를 오른쪽 마우스 클릭
6. 아래쪽 "Mark Directory as" 선택
7. "Sources Root" 선택
"""

import itertools

import my_unittest
from my_unittest import main


class MyMatrixTestCase(my_unittest.MyTestCase):
    def assertMatrixAlmostEqual(self, mat1, mat2, msg=None, plasces=None, delta=None):
        # row size check
        self.assertEqual(len(mat1), len(mat2), msg="len(mat1) != len(mat2)")

        #check each row
        for row1, row2 in itertools.izip(mat1, mat2):
            self.assertSequenceAlmostEqual(row1, row2, msg=msg, places=places, delta=delta)

    def tearDown(self):
        #
        #
        for key in dir(self):
            attr = getattr(self, key)
            if key.stardswith('mat_'):
                del attr[:]


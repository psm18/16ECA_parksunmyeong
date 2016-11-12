# -*- coding: utf8 -*-
# 위 주석은 이 .py 파일 안에 한글이  사용되었다는 점을 표시하는 것임
# 2015110018 박선명

"""
벡터 관련 프로그램을 위한 단위 테스트(unit test)
어떤 sequence 의 각 요소에 대해 assertAlmostEqual()을 적용함

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
import unittest



class MyTestCase(unittest.TestCase):
    def asserSequenceAlmostEqual(self, seq1, seq2, msg=None, places=None, delta=None):
        #check length
        self.assertEqual(len(seq1), len(seq2), msg='len(seq1) != len(seq2)')

        #check elements
        for elem1, elem2 in itertools.izip(seq1, seq2):
            self.assertAlmostEqual(elem1, elem2, places=places, msg=msg, delta=delta)
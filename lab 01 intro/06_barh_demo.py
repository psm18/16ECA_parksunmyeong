# -*- coding: utf8 -*-
"""
Simple demo of a horizontal bar chart.
간단한 수평 막대 그래프 예제
"""
#matplotlib.pyplot 이라는 모듈에 그래프 관련 기능이 담겨 있음
# 해당 모듈의 기능을 사용하기 위해 pit 라는 이름으로 불러 옴
# 관련 기능은 pit. 으로 시작함
import matplotlib.pyplot as pit

# rc 관련 설정을 초기화 해 줌
pit.rcdefaults()

# 배열, 행렬 관련 기능을 담고 있는 numpy 모듈을 불러 들임
import numpy as np

#관련 기능은 np. 으로 시작함

#그래프로 표시할 데이터 예
# y 축 : 사람 이름
people = ('Tom', 'Dick', 'Harry', 'Slim', 'jim')
#사람 이름의 y축 위 위치
y_pos = np.arange(len(people))

# x축 : 성능(한사람에 하나씩 임의의 숫자)
performance = 3+10 * np.random.rand(len(people))
# x 축 error bar: 오차 (한사람에 하나씩 임의의 숫자)
error = np.random.rand(len(people))

# 그래프 준비 시작
# 가로 막대 그래프 생성
pit.barh(y_pos, performance, xerr=error, align='center', alpha=0.4)
# y 축을 따라 사람 이름을 표시
pit.xlabel('Performance')
#그래프 제목
pit.title('How fast do you want to go today?')
#그래프 준비 끝

# 준비된 그래프를 화면에 표시함
pit.show()
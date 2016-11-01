# -*- coding: utf8 -*-
# 위 주석은 이 .py 파일 안에 한글이  사용되었다는 점을 표시하는 것임
# 2015110018 박선명


class TrafficCardClass(object):
    """
     교통카드 클래스

     object 라는 다른 이름의 클래스에 원하는 기능을 추가하여 만듦
     이 때 object 를 "교통카드 클래스의 superclasee" 라고 부르고,
     교통카드 클래스는 "object 클래스의 subclass" 라고 부름

     각각의 교통카드는 이 교통카드 클래스의 "인스턴스 instance"가 됨
     클래스가 붕어빵 들 이라면, 인스턴스(==객체)는 그 틀로 만든 붕어빵이라고 할 수 있음
     모양은 같지만 각각의 붕어빵은 각기 다른 "객체"가 됨

     각 교통카드 인스턴스의 잔고는 "인스턴스 변수" balance 에 저장됨
    """
    def __init__(self):
        """
        생성자 constructor 함수로 이 클래스의 인스턴스를 만들 떄 호출됨
        잔고를 저장할 instance 변수를 초기화 함
        """
        # 필요에 따라 superclass 의 생성자를 불러야 할 떄는 아래와 같이 함
        # super(TrafficCardClass, self).__init__()

        # instance 변수를 초기화
        self.balance_won =0

    def deposit(self, amount):
        """
        교통카드에 입금
        :param amount: int
        :return: None
        """
        #balance_won 을 amount 만큼 증가시킴
        self.balance_won += int(amount)
        # no return balue ->None

    def pay(self,amount):
        """
        교통카드로 지불
        :param amount: int
        :return: None
        """
        #balance_won 을 amount 만큼 감소시킴
        self.balance_won -= int(amount)

    def check(self):
        """
        잔고확인
        :return: int
        """
        return self.balance_won


#"__name__" 변수의 내용을 확인해봄
import os
print("__name__ in %s = %s" % (os.path.basename(__file__), __name__))

if"__main__" == __name__:
    # 이 파일이 import 될 경우 아래의 행은 실행되지 않음

    # my_card 인스턴스를 생성함
    my_card = TrafficCardClass()
    # 아래의 실행 예에서 인스턴스 변수 my_card.balance 를 직접 변경하거나 읽지 않음: 캡슐화 encapsulation
    #instance 생성 후 잔고 확인
    print("my_card.check() = %s" % my_card.check())
    # my_card충전
    print("my_card.deposit(10000) = %s" % my_card.deposit(10000))
    # my_card로 비용 지불
    print("my_card.pay(1250) = %s" % my_card.pay(1250))
    #my_card 잔고 확인
    print ("my_card.check() = %s" % my_card.check())

    # 여러장의 카드를 만들 수 있는지 알아 보기 위해 your_card 인스턴스를 생성
    your_card = TrafficCardClass()
    # instance 생성 후 잔고 확인
    # Q: 같은 카드인가? 다른 카드인가?
    print("your_card.check() = %s" % your_card.check())

    # 충전은 안하고 계속 쓰기만 하면 어떻게 될까?
    print("my_card.pay(1250) = %s" % my_card.pay(1250))
    print("my_card.check() = %s" % my_card.check())
    print("my_card.pay(1250) = %s" % my_card.pay(1250))
    print("my_card.check() = %s" % my_card.check())
    print("my_card.pay(1250) = %s" % my_card.pay(1250))
    print("my_card.check() = %s" % my_card.check())
    print("my_card.pay(1250) = %s" % my_card.pay(1250))
    print("my_card.check() = %s" % my_card.check())
    print("my_card.pay(1250) = %s" % my_card.pay(1250))
    print("my_card.check() = %s" % my_card.check())
    print("my_card.pay(1250) = %s" % my_card.pay(1250))
    print("my_card.check() = %s" % my_card.check())
    print("my_card.pay(1250) = %s" % my_card.pay(1250))
    print("my_card.check() = %s" % my_card.check())
    print("my_card.pay(1250) = %s" % my_card.pay(1250))
    print("my_card.check() = %s" % my_card.check())

    #Q: Unit test 를 작성해 보시오





# -*- coding: utf8 -*-
import traffic_card_class_02 as tcc

#파일 이름일 너무 길어서 tcc로 줄여 쓰기로 함





class NoOverChargeCard(tcc.TrafficCardClass):
    """
    잔고가 0 이하로 내려가지 않는 교통 카드
    TrafficCardClass 를 기반으로 만듦
    TrafficCardClass 를 만들 때 이미 만들었던 대부분의 기능을 그대로 변경 없이 사용함
    """
    def pay(self, amount):
        """
        superclass 의 지불 함수를 "덮어 씀 override"
        지불한 결과, 잔고가 0보다 작을 것으로 예상되면 오류 메세지를 발생시킴
        :param amount: int
        :return:
        """
        # 잔고가 충분하면
        if self.balance_won > int(amount):
            # 정상적으로 지불
            super(NoOverChargeCard, self).pay(amount)
        else:
            #그렇지 않으면 ==잔고가 충분하지 않으면
            #오류 메시지 발생
            #amount 매개 변수의 값에 문제가 있으므로 ValueError 를 발생시킴
            raise ValueError('Nor enough balance')


#"__name__" 변수의 내용을 확인해 봄
import os


print("__name__ in %s =%s" % (os.path.basename(__file__), __name__))


if"__main__" == __name__:
    # 이 파일이 import 될 경우 아래의 행은 실행되지 않음

    # my_card 인스턴스를 생성함
    my_card = NoOverChargeCard()
    # instance 생성 후 잔고 확인
    print("my_card.check() = %s" % my_card.check())
    #my_card충전
    print("my_card.deposit(10000) = %s" % my_card.deposit(10000))
    #my_card로 비용지불
    print("my_card.pay(1250) = %s" % my_card.pay(1250))
    #my_card 잔고 확인
    print("my_card.check() = %s" % my_card.check())

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
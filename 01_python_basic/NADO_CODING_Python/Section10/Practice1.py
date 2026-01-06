'''
01_python_basic.NADO_CODING_Python.Section10.Practice1의 Docstring
__init__ 은 생성자 즉 마린이라던지 탱크 같은 객체가 만들어질 때 자동으로 호출되는 부분이다.
마린과 탱크는 유닛 클래스의 인스턴스라고 표현한다
'''


class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)
# marine3 = Unit("마린") 생성자 함수의 인자 개수랑 다르면 오류 뜸
# marine3 = Unit("마린", 40) 생성자 함수의 인자 개수랑 다르면 오류 뜸


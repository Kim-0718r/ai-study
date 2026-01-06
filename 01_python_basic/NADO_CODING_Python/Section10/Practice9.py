# super 2번째

class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flayble 생성자")

class FlyableUnit(Unit, Flyable): #Super 를 쓰면 맨 처음 클래스만 상속이 된다
    def __init__(self):
        # super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)
# 드랍쉽
dropship = FlyableUnit()
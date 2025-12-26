# 지역 변수와 전역 변수
gun = 10

def checkpoint(soldiers): # 경계 근무
    global gun #  전역 공간에 있는 gun 사용
    gun = gun - soldiers # 지역변수 밖에서는 사용 불가능
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpint_ret(gun, soliders):
    gun = gun - soliders
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
# checkpoint(2) # 2명이 경계 근무 나감
gun = checkpint_ret(gun, 2)
print("남은 총 : {0}".format(gun))
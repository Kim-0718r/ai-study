'''
01_python_basic.NADO_CODING_Python.Section6.Quiz의 Docstring

Quiz ) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

조건1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
조건2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

(출력문 예제)
[0] 1번째 손님 (소요시간 : 15분)
[ ] 2번째 손님 (소요시간 : 50분)
[0] 3번째 손님 (소요시간 : 5분)
...
[ ] 50번째 손님 (소요시간 : 16분)

총 탑승 승객 : 2분
'''
from random import *
customer = 0
for i in range(1,51):
    customer_time = randint(5,50)
    if customer_time >= 5 and customer_time <= 15:
        print("[o] {0}번째 손님 (소요시간 : {1}분)".format(i,customer_time))
        customer += 1
        
    else:
        print("[] {0}번째 손님 (소요시간 : {1}분)".format(i,customer_time))

print("총 탑승 승객 : {0} 분".format(customer))



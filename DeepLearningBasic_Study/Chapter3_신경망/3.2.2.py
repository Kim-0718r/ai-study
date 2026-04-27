#3.2.2 계단 함수 구현하기
import numpy as np
x = np.array([-1.0, 1.0, 2.0])
print(x)
y  = x > 0
print(y)
y = y.astype(int)
print(y)
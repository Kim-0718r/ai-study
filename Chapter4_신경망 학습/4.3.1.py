#4.3.1 미분
import numpy as np

# 나쁜 구현 예
def numerical_diff(f, x):
    h = 1e-50
    return (f(x+h)-f(x)) / h

print(np.float32(1e-50)) # 0.0 도출

# 좋은 미분 
def numerical_diff1(f,x):
    h = 1e-4 
    return (f(x+h)- f(x-h)) / (2*h)
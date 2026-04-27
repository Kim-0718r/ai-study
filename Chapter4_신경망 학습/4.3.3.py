#4.3.3 편미분
import numpy as np

def numerical_diff1(f,x):
    h = 1e-4 
    return (f(x+h)- f(x-h)) / (2*h)

# 편미분의 기본 식
def function_2(x):
    return x[0]**2 + x[1]**2
# 문제 1 x0 = 3, x1 = 4 일 때, x0에 대한 편미분을 구하여라
def function_tmp1(x0):
    return x0*x0 + 4.0**2.0

print(numerical_diff1(function_tmp1,3.0))

# 문제 2 x0 = 3, x1 =4 일 때, x1에 대한 편미분을 구하여라

def function_tmp2(x1):
    return 3.0**2.0 + x1 ** 2.0

print(numerical_diff1(function_tmp1,4.0))
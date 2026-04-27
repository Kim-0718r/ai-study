#4.4 기울기
import numpy as np

def numerical_gradient(f,x):
    h = 1e-4
    grad = np.zeros_like(x) # x와 크기와 같은 배열의 모든 값을 다 0으로 채움

    for idx in range(x.size):
        tmp_val = x[idx]
        # f(x+h) 계산
        x[idx] = tmp_val + h
        fxh1 = f(x)

        # f(x-h) 계신
        x[idx] = tmp_val - h
        fxh2 = f(x)

        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = tmp_val # 값 복원
    
    return grad

def function_1(x):
    return x[0]**2 + x[1]**2

print(numerical_gradient(function_1,np.array([3.0, 4.0])))
# [6. 8.]
print(numerical_gradient(function_1,np.array([0.0, 2.0])))
# [0. 4.]
print(numerical_gradient(function_1,np.array([3.0, 0.0])))
# [6. 0.]

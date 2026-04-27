#3.3.3 신경망에서의 행렬 곱
import numpy as np
X = np.array([1,2])
print(X.shape)
W = np.array([[1,3,5],[2,4,6]])
print(W)
print(W.shape)
y = np.dot(X,W)
print(y)

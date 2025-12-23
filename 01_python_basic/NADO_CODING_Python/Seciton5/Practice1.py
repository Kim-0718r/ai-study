'''
01_python_basic.NADO_CODING_Python.Seciton5.Practice1의 Docstring

사전(딕셔너리)
'''

cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3)) # 3번 키값을 가져옴
# print(cabinet[5]) 키 값이 없으면 오류가 뜸
print(cabinet.get(5)) # 오류가 안 뜨고 none 만 뜸
print(cabinet.get(5, "사용 가능")) #none 값을 안 뜨게하고 사용가능 값으로 바꿈
# print("hi")

print(3 in cabinet) # True 3이라는 값이 cabinet에 있으면 
print(5 in cabinet) # False 5이라는 값이 cabinet에 없어서 False

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국" #value 값을 바꿈
cabinet["C-20"] = "조세호"
print(cabinet)

# 간 손님
del cabinet["A-3"] # 키 값을 제거
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear() # 모든 값을 다 제거
print(cabinet)
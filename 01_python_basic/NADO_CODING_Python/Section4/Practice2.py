'''
01_python_basic.NADO_CODING_Python.Section4.Practice2의 Docstring
문자열 처리 함수
'''

python = "Python is Amazing"
print(python.lower()) #전체 다 소문자로 변환
print(python.upper()) #전체 다 대문자로 변환
print(python[0].isupper()) #0번째 인덱스가 대문자인지 확인하는 것
print(len(python)) #문자열의 길이 출력
print(python.replace("Python", "Java")) # 앞의 문자를 뒤에 문자로 변환
index = python.index("n") # n의 위치를 찾아줌
print(index) # 5 , 5번째 인덱스
index = python.index("n", index + 1) # 기존 인덱스 n에서 다음번째 n 찾는것
print(index)

print(python.find("Java")) # -1 을 반환 오류는 나지 않음
# print(python.index("Java")) 오류가 남 

print(python.count("n")) # n이 몇번 등장하는지 알아내는 함수
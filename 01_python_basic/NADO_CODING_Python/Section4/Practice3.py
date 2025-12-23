'''
01_python_basic.NADO_CODING_Python.Section4.Practice3의 Docstring
문자열 포맷
+ , 로 출력을 안하는 새로운 방식
'''

# 방법 1
print("나는 %d살입니다." % 20) # %d 는 정수형
print("나는 %s을 좋아해요." % "파이썬") # %s는 문자열
print("Apple 은 %c로 시작해요." % "A") # %c는 문자 한개

print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# 방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간")) #숫자로 순서를 적용
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간", age = 20))

# 방법 4 (Python 버전 3.6 이상 ~)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

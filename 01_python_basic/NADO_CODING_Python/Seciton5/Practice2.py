'''
01_python_basic.NADO_CODING_Python.Seciton5.Practice2의 Docstring

튜플 
속도는 리스트 보다 빠른 대신 변경이 불가능함
괄호로 열고 닫고 가능
'''

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스") 값 변경 불가능

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

(name, age , hobby) = ("김종국", 20, "코딩") 
print(name, age, hobby)
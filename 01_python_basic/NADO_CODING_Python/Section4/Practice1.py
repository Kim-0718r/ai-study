'''
01_python_basic.NADO_CODING_Python.Section4.Practice1의 Docstring
슬라이싱
'''
jumin = "990120-1234567"
print("성별 : " + jumin[7]) # 인덱스 넘버 7 : 1 
print("연 : " + jumin[0:2]) # 0부터 2번째 직전 값까지 인덱스 0, 1
print("월 : " + jumin[2:4]) # 2부터 4번째 직전 값까지
print("일 : " + jumin[4:6]) # 4부터 6번째 직전 값까지

print("생년월일 : " + jumin[:6]) #0부터 6번째 직전 값까지 앞에 숫자를 안 적게되면 처음부터 6번째 직전값까지 인덱싱
print("뒤 7자리 : " + jumin[7:]) #7부터 끝까지
print("뒤 7자리 (뒤에부터) : " + jumin[-7:]) 
# 맨 뒤에서 7번째부터 끝까지 맨 뒤에인덱스가 -1부터
'''
표준 입출력
'''

import sys
print("Python", "Java",  sep=",", end="?") # 띄어쓰기에 , 가 들어감
# end : 문장의 끝 부분을 주어진 값으로 넣고 띄어쓰기를 안함
print("무엇이 더 재밌을까요?") # 띄어 쓰기가 안됨 
print("Python", "Java", file=sys.stdout)
print("Python", "Java", file=sys.stderr)

scores = {"수학": 0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":") #ljust(8) 왼쪽정렬 8개의 공간을 확보
    #rjust(4) 오른쪽 4개의 공간을 확보후 오른쪽 정렬

# 은행 대기순번표
# 001, 002, 003, ...
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3)) #zfill(3) 3개의 크기를 확보하고 값이 없는 빈 공간에 대해서는 0으로 채우는것


answer = input("아무 값이나 입력하세요 : ")
print("입력하신 값은 " + answer + "입니다.")

# 사용자 값을 받을 때는 항상 문자열로 담긴다
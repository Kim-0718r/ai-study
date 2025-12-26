'''
01_python_basic.NADO_CODING_Python.Section6.Practice의 Docstring
if 문
조건이 맞을 경우 if 문 실행 if문 조건이 다르면 elif 로
아예 안 맞을경우 else로 적용
'''
# weather = input("오늘 날씨는 어때요? ")
# if weather == "비" or weather == "눈": #or 로 조건을 추가 할 수 있다.
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요.")

temp = int(input("기온은 어때요? "))
if 30 <= temp:
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에요")
elif 0 <= temp and temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요")
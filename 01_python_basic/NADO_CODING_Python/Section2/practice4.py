'''
01_python_basic.NADO_CODING_Python.Section2.practice4의 Docstring

변수
'''

# 애완동물을 소개해 주세요~

# print("우리집 강아지의 이름은 연탄이에요")
# print("연탄이는 4살이며, 산책을 아주 좋아해요")
# print("연탄이는 어른일까요?  True")

'''
만약 위에 코드에서 강아지의 이름이 바뀌면 문장의 사용되어진 이름들을 
다 바꿔야 된다. 현재 코드가 3줄 밖에 없지만 코드가 많아지면 비효율적이기에 
변수라는 개념을 사용한다.
변수는 값이 저장되는 공간
'''

animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3 # age 가 3 이상일 시 True

print("우리집 " + animal + "의 이름은 " + name + " 예요")
hobby = "공놀이"
print(name, "는 " , age , "살이며," , hobby , "을 아주 좋아해요")  # , 로도 문장 출력이 가능하고 정수형을 굳이 문자열로 안 바꿔도 된다. ,를 사용하면 자동으로 띄어 쓰기가 된다.
print(name + "는 " + str(age) + "살이며," + hobby + "을 아주 좋아해요")  #정수형은 + print문으로 출력되려면 str로 형 변환을 해줘야됨
print(name + "는 어른일까요? " + str(is_adult))


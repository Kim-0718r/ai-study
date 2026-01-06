# pickle
# 프로그램 상에서 우리가 사용하고 있는 데이터를 파일 형태로 저장을 해서 주는 것

import pickle
profile_file = open("profile.pickle", "wb") #b는 binary 타입인데 pickle 은 항상 binary를 선언해줘야된다. pickle 은 따로 encoidng 안해줘도됨
profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
print(profile)
#pickle.dump 이 내용을 파일에 적을 때 사용하는것
pickle.dump(profile, profile_file) # profile 에 있는 정보를 file 에 저장
profile_file.close()

profile_file1 = open("profile.pickle", "rb")
profile = pickle.load(profile_file1) # file에 있는 정보를 profile 에 불러오기
print(profile)
profile_file1.close()
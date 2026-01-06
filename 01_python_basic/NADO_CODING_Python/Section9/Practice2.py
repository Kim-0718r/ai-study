score_file = open("score.txt", "w", encoding="utf-8") #w 쓰는 목적
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

score_file1 = open("score.txt", "a", encoding="utf-8") # a 는 기존 파일에 이어 쓰기
score_file1.write("과학 : 80")
score_file1.write("\n코딩 : 100")
score_file1.close()

score_file2 = open("score.txt", "r", encoding="utf-8") # 해당 파일을 읽어오기
print(score_file2.read())
score_file2.close()

score_file3 = open("score.txt", "r", encoding="utf-8")
print(score_file3.readline(), end="") # 줄별로 읽기 , 한 줄 읽고 커서는 다음 줄로 이동
print(score_file3.readline(), end="") # 줄별로 읽기 , 한 줄 읽고 커서는 다음 줄로 이동
print(score_file3.readline(), end="") # 줄별로 읽기 , 한 줄 읽고 커서는 다음 줄로 이동
print(score_file3.readline()) # 줄별로 읽기 , 한 줄 읽고 커서는 다음 줄로 이동
score_file3.close()

score_file4 = open("score.txt", "r", encoding="utf-8") # while 문을 이용한 파일 입출력
while True:
    line = score_file4.readline()
    if not line:
        break
    print(line, end="")
score_file4.close()
print("")

score_file5 = open("score.txt", "r", encoding="utf-8")
lines = score_file5.readlines() # 모든 내용을 list에 저장
for line in lines:
    print(line, end="")

score_file5.close()



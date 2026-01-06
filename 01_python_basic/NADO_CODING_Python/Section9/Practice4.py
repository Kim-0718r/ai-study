'''
01_python_basic.NADO_CODING_Python.Section9.Practice4의 Docstring
with
'''
import pickle
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

    # 파일을 열어 profile_file에 넣는 과정

with open("study.txt", "w", encoding="utf-8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt", "r", encoding="utf-8") as study_file:
    print(study_file.read())
'''
06-6 하위 디렉터리 검색하기
특정 디렉터리부터 시작해서 그 하위의 모든 파일 중 파이썬 파일(*.py)만 출력해 주는 프로그램을 만들려면 어떻게 해야 할까?
'''

import os

pyNum = 0;

def searchDir(root):
    try:
        fileNames = os.listdir(root)
        for fileName in fileNames:
            fullFileName = os.path.join(root, fileName)  # join 서로 합쳐 주는 함수
            if os.path.isdir(fullFileName):  # directory 인지 확인
                searchDir(fullFileName)  # 더 하위로 가기 위해 재귀로 만듦
            else :
                ext = os.path.splitext(fullFileName)[-1]  # path를 split 해줌
                if ext == ".py" :
                    print(fullFileName)
                    global pyNum #전역변수를 사용하기 전에 미리 전역변수라고 선언해줘야 한다.
                    pyNum = pyNum + 1
    except PermissionError :
        pass

searchDir("D:/")
print(str(pyNum)+"개")
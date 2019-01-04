'''
06-4 간단한 메모장 만들기
원하는 메모를 파일에 저장하고 추가 및 조회가 가능한 간단한 메모장을 만들어 보자.

필요한 기능은? 메모 추가하기, 메모 조회하기
입력 받는 값은? 메모 내용, 프로그램 실행 옵션
출력하는 값은? memo.txt
가장 먼저 해야 할 일은 메모를 추가하는 것이다. 다음과 같은 명령을 실행했을 때 메모를 추가할 수 있도록 만들어 보자.

python memo.py -a "Life is too short"

memo.py는 우리가 작성할 파이썬 프로그램명이다. -a는 이 프로그램의 실행 옵션이고 "Life is too short"는 추가할 메모 내용이 된
'''

#f = open("memo.txt", "w") # mode : r - read, w - write, a - add

import sys
option = sys.argv[1]
memo = sys.argv[2]

for n in sys.argv:
    print(n)

if option == "-a" :
    f = open("memo.txt", "a") #file 객체 생성
    f.write(memo) #file에다가 memo 내용 쓰기
    f.write("\n") #다음을 위해 한줄 띄기
    f.close() #객체닫기
elif option == "-v" :
    f = open("memo.txt") #file 객체 생성
    print(f.read()) #file 객체 읽기 -> 프린트 까지
    f.close() #객체닫기


'''
06-5 탭을 4개의 공백으로 바꾸기
이번에는 문서 파일을 읽어서 그 문서 파일 내에 있는 탭(tab)을 공백(space) 4개로 바꾸어주는 스크립트를 작성해 보자.

필요한 기능은? 문서 파일 읽어 들이기, 문자열 변경하기
입력 받는 값은? 탭을 포함한 문서 파일
출력하는 값은? 탭이 공백으로 수정된 문서 파일
다음과 같은 형식으로 프로그램이 수행되도록 만들 것이다.

python tabto4.py src dst
tabto4.py는 우리가 작성해야 할 파이썬 프로그램명이고 src는 탭을 포함하고 있는 원본 파일명이다. dst는 파일 내의 탭을 공백 4개로 변환한 결과를 저장할 파일명이다.

예를 들어 a.txt라는 파일에 있는 탭을 4개의 공백으로 바꾸어 b.txt라는 파일에 저장하고 싶다면 다음과 같이 수행해야 한다.

python tabto4.py a.txt b.txt
'''
import sys

asIs = sys.argv[1]
toBe = sys.argv[2]

af = open(asIs)
asIsCntn = af.read()
print("as is : "+asIsCntn)
af.close()

toBeCntn = asIsCntn.replace("\t", " "*4)
print("to be : "+toBeCntn)
bf = open(toBe,"w")
bf.write(toBeCntn)
bf.close
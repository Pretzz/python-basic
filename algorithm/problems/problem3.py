'''
3. 반복문을 사용하여 1부터 n까지 출력하기
con1. 1부터 순서대로 화면에 출력한다.
con2. 출력하는 숫자가 n이 되면 프로그램을 종료한다.
'''

def printNum(num):
    #for문
    for n in range(1,num+1):
        print(n)
    #while문
    c = 1
    while c<num+1:
        print(c)
        c += 1


if __name__ == "__main__":
    printNum(100)
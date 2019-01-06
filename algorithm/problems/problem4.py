'''
4. 재귀 호출을 사용하여 n부터 1까지 출력하기
con1. n부터 1까지 역순으로 화면에 출력해야 한다.
con2. 출력하는 숫자가 1이되면 프로그램을 종료한다.
'''

def recurv(num):
    print(num)
    if num > 1:
       recurv(num-1)


if __name__ == "__main__":
    recurv(20)
'''
1. 반복문을 사용하여 0부터 n까지의 합 출력하기
0부터 n까지의 연속된 숫자의 합을 계산하여 화면에 출력하는 프로그램을 작성해보자.
단, n은 사용자로부터 입력 받아도 되고 직접 코드에 작성해도 상관없다.
'''
result = 0
def add(max):
    global result
    for n in range(0, max+1):
        result += n
    return result

if __name__ == "__main__":
    print(add(100))
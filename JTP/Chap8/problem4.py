'''
[문제4] DashInsert
DashInsert 함수는 숫자로 구성된 문자열을 입력받은 뒤, 문자열 내에서 홀수가 연속되면 두 수 사이에 - 를 추가하고, 짝수가 연속되면 * 를 추가하는 기능을 갖고 있다. (예, 454 => 454, 4546793 => 454*67-9-3)

DashInsert 함수를 완성하자.

입력 - 화면에서 숫자로 된 문자열을 입력받는다.
4546793
출력 - *, -가 적절히 추가된 문자열을 화면에 출력한다.
454*67-9-3
'''
#
# def dashInsert(_data):
#     answer = ""
#     dataLen = len(_data)
#     for n in range(dataLen-1, 0, -1):
#         i = dataLen-1 - n
#         cur = int(_data[i]) % 2
#         next = int(_data[i+1]) % 2
#         if cur != next:
#             answer = answer + _data[i]
#         else :
#             if cur == 1:
#                 # 서로 홀수 일 때
#                 answer = answer + _data[i] + "-"
#             else:
#                 # 서로 짝수 일 때
#                 answer = answer + _data[i] + "*"
#     return answer+_data[dataLen-1]
#
# # data = input()
# data = "4546793"
# print(dashInsert(data))

def dashInsert(data):
    numbers = list(map(int,data))
    result = []
    for i, num in enumerate(numbers):
        result.append(str(num)) #마지막 숫자 때문에 앞쪽으로 위치
        if i<len(numbers)-1:
            isOdd = num%2 == 1
            isNextOdd = numbers[i+1]%2 == 1
            if isOdd and isNextOdd:
                result.append("-")
            elif not isOdd and not isNextOdd:
                result.append("*")
    print(result)
    print("".join(result))

data = "4546793"
dashInsert(data)
'''
답
data = "4546793"

numbers = list(map(int, data))  # 숫자 문자열을 숫자 리스트로 변경 ##핵심!!
result = []

    
for i, num in enumerate(numbers): ##핵심!!

    print("i:"+str(i)+", num:"+str(num))
    
    result.append(str(num))
    if i < len(numbers)-1:  # 다음수가 있다면
        is_odd = num % 2 == 1  # 현재수가 홀수                 ## true, false 방식을 저렇게 쓸 수도 있다. 확인!
        is_next_odd = numbers[i+1] % 2 == 1  # 다음수가 홀수
        if is_odd and is_next_odd: # 연속 홀수
            result.append("-")
        elif not is_odd and not is_next_odd: # 연속 짝수       ## 조건문을 이렇게도 쓸 수 있다 확인!
            result.append("*")
            
print(result)
print("".join(result)) ##list를 하나의 문자열로 바꿔준다.
'''



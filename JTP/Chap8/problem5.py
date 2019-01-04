'''
[문제5] 문자열 압축하기
문자열을 입력 받아 같은 문자가 연속적으로 반복되는 경우에 그 반복 횟수를 표시하여 문자열을 압축하여 표시해 보자.

입력 예시: aaabbcccccca
출력 예시: a3b2c6a1
'''

data = "aaabbcccccca"

# list = [0] * 26
# print(list)
# for c in data:
#     pos = ord(c) - 97
#     list[pos] = list[pos] + 1
#
# print(list)
# answer = ""
# for i in range(0,len(list)) :
#     apb = chr(i+97)
#     if list[i] != 0 :
#         answer = answer + apb+str(list[i])
#
# print(answer)

sum = 0
answer = ""
for i in range(0, len(data)) :
    if i != len(data)-1 :
        if data[i] == data[i+1]:
            sum = sum + 1
        else:
            sum = sum + 1
            answer = answer+ data[i]+str(sum)
            sum = 0
    else:
        if data[i-1] == data[i]:
            sum = sum + 1
            answer = answer + data[i] + str(sum)
        else:
            answer = answer + data[i] + "1"

print(answer)

'''
답
def compress_string(s):
    _c = ""
    cnt = 0
    result = ""
    for c in s:
        if c!=_c:
            _c = c
            if cnt: result += str(cnt)    ## if cnt : 의 의미.. cnt가 0이면 false, 그외 숫자면 true
            result += c
            cnt = 1
        else:
            cnt +=1
    if cnt: result += str(cnt)
    return result

print (compress_string("aaabbcccccca")) #a3b2c6a1 출력
'''

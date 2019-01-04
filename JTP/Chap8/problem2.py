'''
[문제2] 합의 제곱과 제곱의 합의 차
1부터 10까지 자연수를 각각 제곱해 더하면 다음과 같다. (제곱의 합)

12+22+...+102=385
1부터 10을 먼저 더한 다음에 그 결과를 제곱하면 다음과 같다. (합의 제곱).

(1+2+...+10)2=552=3025
따라서 1부터 10까지 자연수에 대해 "합의 제곱"과 "제곱의 합" 의 차이는 3025 - 385 = 2640 이 된다.

그러면 1부터 100까지 자연수에 대해 "합의 제곱"과 "제곱의 합"의 차이는 얼마일까?
import numpy as np
x = np.arange(1, 100, 1)
'''

# 합의 제곱
def sumOfSqare(max) :
    sum = 0
    for n in range(1, max+1): # for문은 range 마지막은 포함하지 않는다. for(int i=1; i<max; i++)와 같은 의미
        sum = sum + n

    sos = sum * sum
    return sos

# 제곱의 합
def sqareOfSum(max) :
    sum = 0
    for n in range(1, max+1):
        sum = sum + (n * n)
    return sum

sumOf = sumOfSqare(100)
squOf = sqareOfSum(100)
print("합의 제곱 - 제곱의 합 : "+ str(sumOf - squOf))

# 합의 제곱 :25502500, 제곱의 합 : 338350

'''
답
sum1 = 0
sum2 = 0

for i in range(1, 100+1):
    sum1 += i
    sum2 += i**2  # 제곱의 합

sum1 = sum1 ** 2  # 합의 제곱

print(sum1 - sum2)
'''
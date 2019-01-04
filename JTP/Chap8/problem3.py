'''
[문제3] 1부터 100까지의 각 숫자의 갯수 구하기
10 ~ 15 까지의 각 숫자의 개수는 다음과 같이 구할 수 있다.

10 = 1, 0
11 = 1, 1
12 = 1, 2
13 = 1, 3
14 = 1, 4
15 = 1, 5
그러므로 이 경우의 답은 0:1개, 1:7개, 2:1개, 3:1개, 4:1개, 5:1개

위와 같은 방식으로 1부터 100까지의 각 숫자의 개수를 구하시오.
'''
numList = [0,0,0,0,0,0,0,0,0,0]

def devider(_num, _list):
    strNum = str(_num)
    lenNum = len(strNum)
    for n in range(0,lenNum):
        c = int(strNum[n])
        _list[c] = _list[c] + 1
    return _list

for n in range(1, 101):
    numList = devider(n,numList)

ans = ""
for n in range(0, len(numList)):
    ans = ans + str(n)+":"+str(numList[n])+"개 "

print(ans)
# 0:11개 1:21개 2:20개 3:20개 4:20개 5:20개 6:20개 7:20개 8:20개 9:20개

'''
답
from collections import defaultdict

d = defaultdict(int)
for number in range(1, 100+1):
    for c in str(number):
        d[c] += 1

print(dict(d)) #dictionary 로 변환
'''

from collections import defaultdict

d = defaultdict(int)
print(d)
for number in range(1, 100+1):
    for c in str(number):
        d[c] += 1
print(dict(d))
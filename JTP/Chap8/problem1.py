'''
[문제1] 이름 분석
주어진 문자열(공백 없이 쉼표로 구분되어 있음)을 가지고 아래 문제에 대한 프로그램을 작성하세요.

이의덕,이재명,권종수,이재수,박철호,강동희,이재수,김지석,최승만,이성만,박영희,박수호,전경식,송우환,김재식,이유정
1.김씨와 박씨는 각각 몇 명 인가?
2."이재수"란 이름이 몇 번 반복되나?
3.중복을 제거한 이름을 출력하시오.
4.중복을 제거한 이름을 오름차순으로 정렬하여 출력하시오.
'''
# 1
names = "이의덕,이재명,권종수,이재수,박철호,강동희,이재수,김지석,최승만,이성만,박영희,박수호,전경식,송우환,김재식,이유정"
namesArr = names.split(",")
kimCnt = 0;
parkCnt = 0;

for name in namesArr:
    if name[0] == "김" :  # if name.startswith('박'):
        kimCnt = kimCnt + 1
    elif name[0] == "박":
        parkCnt = parkCnt + 1


'''
for(int i=0; i<namelist.length; i++){
    String name = namelist[i]
}

for name in naemsArr:

'''

print("1. 김씨 총 "+str(kimCnt)+"명, 박씨 총 "+str(parkCnt)+"명")

# 2 ans : print(names.count('이재수'))
dupCnt = 0;
for name in namesArr:
   if name == "이재수":
       dupCnt = dupCnt + 1

print("2. 이재수 중복 개수 : "+str(dupCnt)+"개")

# 3

aftDupArr = list(set(namesArr));
print("3. 중복 제거 후 : ")
print(aftDupArr)

# 4 버블 정렬 이용 ans : print(sorted(names))
temp = ""
for i in range(len(namesArr)-1, 0, -1):
    for j in range(0, i):
        if namesArr[j] > namesArr[j+1]:
            temp = namesArr[j]
            namesArr[j] = namesArr[j+1]
            namesArr[j+1] = temp

print("4. 오름 차순 정렬 :")
print(namesArr)



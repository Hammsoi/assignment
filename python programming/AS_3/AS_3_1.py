import random
import math
#숫자목록을 저장할 배열
arr=[]
#배열 안의 최대, 최소값을 저장할 배열
arr2=[]
#길이 50의 배열을 랜덤한 정수값으로 저장
for i in range(50):
    arr.append(random.randint(1,50))
#arr2에 최대, 최소값 저장
arr2.append(max(arr))
arr2.append(min(arr))
#출력
print(f'생성된 숫자 목록: {arr}')
print(f'선택된 숫자 목록: {arr2}')
print(f'최대공약수: {math.gcd(arr2[0],arr2[1])}')
print(f'최소공배수: {math.lcm(arr2[0],arr2[1])}')

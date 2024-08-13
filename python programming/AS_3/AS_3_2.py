import random
import math
arr=[]
pair=[]
def start_program():
    a=int(input("정수범위 최솟값: "))
    b=int(input("정수범위 최댓값: "))
    for i in range(50):
        arr.append(gen_random(a,b))
    


def gen_random(a,b):
    return random.randint(a,b)

def select_number():
    return [arr[random.randint(0,49)], arr[random.randint(0,49)]]

def find_gcd(list):
    return math.gcd(list[0],list[1])
def find_lcm(list):
    return math.lcm(list[0],list[1])
def result_program(nums):
    print(f'최대공약수: {find_gcd(nums)}')
    print(f'최소공배수: {find_lcm(nums)}')

start_program()
print("생성된 숫자 목록: ",arr)
pair=select_number()
print("선택된 숫자 목록: ", pair)
result_program(pair)
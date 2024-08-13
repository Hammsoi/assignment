import random
#모든 손님의 정보를 저장할 배열
arr=[]
#매칭된 손님만 저장할 배열
sorted_arr=[]

#입력받은 손님의 수에 맞춰 소요시간을 랜덤한 정수값으로 받고, 소요시간이 15분 이하라면 sorted_arr과 arr에 저장하고, 아니라면 arr에만 저장.
def matching(sum):
    for i in range(sum):
        arr.append([i+1,random.randint(5,50)])
        if(arr[-1][1] <= 15):
            sorted_arr.append(arr[-1])
#주어진 배열을 순회하며 소요시간이 15분 이하라면 매칭되었음을 표시와 함께 출력하고, 아니라면 표시가 없이 출력.
def result(narr):
    for i in range(len(narr)):
        sig=' '
        if(narr[i][1]<=15):
            sig='0'
        print(f'[{sig}]{narr[i][0]}번째 손님 (소요시간: {narr[i][1]} )')

#실행할 기능을 입력받는다. 1번이라면 result()함수에 arr배열을 보내고, 2번이라면 result()함수에 sorted_arr배열을 보낸다. 3번이라면 프로그램을 종료.
def menu():
    while(True):
        print("실행번호를 선택하세요:")
        print("1. 자세한 매칭 결과")
        print("2. 요약 매칭 결과")
        print("3. 프로그램 종료")
        num=int(input("입력: "))
        if(num==1):
            result(arr)
        elif(num==2):
            result(sorted_arr)
        elif(num==3):
            break


#초기에 손님의 수를 입력받고, matching()함수에 보내어 배열을 만든다. 이후 menu()함수 호출
def start_program():
    print("Starting matching program...")
    num=int(input("Input number of Guest: "))
    matching(num)
    print("Matching Finish")
    menu()
#초기 실행 함수 호출
start_program()
import os
from tkinter import filedialog
#초기 작업 위치 지정
os.chdir(os.getcwd()+"/P04")
#파일이 업로드 되었는지 표시하는 변수
sig=0
#파일의 경로를 저장할 변수
file=None
#학생의 이름과 점수를 저장할 딕셔너리
Info={}
#학생의 이름을 저장할 리스트
Names=[]
#과목을 저장하는 리스트
Sub=[]

#메뉴 인터페이스를 출력하고 입력한 수를 center()함수로 매개변수로 보냄
def menu():
    while(True):
        print("======menu======")
        print("1. read file")
        if(sig==1):
            print("2. calc sum and mean")
            print("3. sort")
            print("4. find student")
            print("5. save file")
            print("6. print")
        print("0. End")
        print("================")
        m=input("Enter number: ")
        if m==0:
            exit()
        center(m)
#입력한 수에 따라 동작할 함수를 호출하는 함수
def center(inp):
    if(not inp.isdigit()):
        print("Input Error.")
        return
    inp=int(inp)
    if((sig==0 and (inp > 1 or inp < 0)) or (sig==1 and (inp > 6 or inp < 0))):
        print("Error Select Number.")
        return 
    #inp에 따라 함수 호출
    if(inp==1):
        reader()
    if(inp==2):
        calc()
    if(inp==3):
        sort_by_name()
    if(inp==4):
        search()
    if(inp==5):
        save()
    if(inp==6):
        print_file()
#파일을 읽는 함수
def reader():
    global file
    global Info
    global Names
    global Sub
    global sig
    #파일 읽었음을 표시
    sig=1
    #파일이 갱신되었을 경우를 대비하여 리스트 비우기
    Names=[]
    #파일 불러오기
    file=filedialog.askopenfilename()
    text=open(file, 'r', encoding="utf-8")
    lst=text.readlines()
    #학생 이름을 key로 성적을 value로 저장 => 이름을 Names에 저장
    for i in range(1,len(lst)):
        lst[i]=lst[i].replace('\n','')
        tmp=lst[i].split(' ')
        Info[tmp[0]]=tmp[1:]
        Names.append(tmp[0])
    print("-------------read file-------------")
    lst[0]=lst[0].replace('\n','')
    Sub=lst[0].split(' ')
    for i in range(len(Sub)):
        print(f"{Sub[i]}    ",end="")
    print()
    for i in range(len(Names)):
        print(f"{Names[i]}: {Info[Names[i]]}")
    print("-----------------------------------")
    

def calc():
    global Sub
    print("---------calc sum and mean---------")
    #상단에 총점과 평균을 프린트 하기 위해 과목 리스트에 추가
    Sub+=['총점', '평균']
    #총점, 평균값을 계산, 저장
    for i in range(len(Names)):
        sum=0
        for j in Info[Names[i]]:
            sum+=int(j)
        Info[Names[i]].append(sum)
        Info[Names[i]].append(sum/5)
    #출력
    for i in range(len(Sub)):
        print(f"{Sub[i]}    ",end="")
    print()
    for i in range(len(Names)):
        print(f"{Names[i]}: {Info[Names[i]]}")
    print("-----------------------------------")
#이름순으로 정렬하는 함수
def sort_by_name():
    global Names
    #Name 리스트를 정렬하기
    Names=sorted(Names)
    #출력
    print("----------------sort---------------")
    for i in range(len(Sub)):
        print(f"{Sub[i]}   ",end="")
    print()
    for i in range(len(Names)):
        print(f"{Names[i]}: {Info[Names[i]]}")
    print("-----------------------------------")
#학생 이름을 입력받고 성적을 출력하는 함수
def search():
    name=input("Enter student name: ")
    #찾는 학생이 없을시 메시지 출력후 돌아가기
    if name not in Info:
        print("non-existent student")
        print("-----------------------------------")
        return
    for i in range(len(Sub)):
        print(f"{Sub[i]}    ", end="")
    print()
    print(f"{name:<6}", end='')
    for i in range(len(Info[name])):
        print(f"{Info[name][i]:<3}    ", end="")
    print()

#정리된 정보를 파일로 저장하는 함수
def save():
    global Names
    name=input("Enter file name: ")
    Nfile=open(f"{name}", 'w+', encoding='utf-8')
    #파일에 작성함과 동시에 출력
    for i in range(len(Sub)):
        print(f"{Sub[i]}    ", end="", file=Nfile)
        print(f"{Sub[i]}    ", end="")
    print('',file=Nfile)
    print('')
    #
    for k in range(len(Names)):
        print(f"{Names[k]:<6}", end='', file=Nfile)
        print(f"{Names[k]:<6}", end='')
        for i in range(len(Info[Names[k]])):
            print(f"{Info[Names[k]][i]:<3}    ", end="", file=Nfile)
            print(f"{Info[Names[k]][i]:<3}    ", end="")
        print('',file=Nfile)
        print('')
#현재의 정보를 출력. 만약 총점, 평균이 없거나 이름순으로 정렬되지 않았더라도 그대로 출력
def print_file():
    print("----------------print---------------")
    for i in range(len(Sub)):
        print(f"{Sub[i]}    ",end="")
    print()
    for i in range(len(Names)):
        print(f"{Names[i]}: {Info[Names[i]]}")
    print("------------------------------------")

#초기에 menu()함수 호출
menu()
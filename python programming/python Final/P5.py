
names=[]
dict={}

def menu():
    global names
    global dict
    try:
            file=open("result.txt","r",encoding="utf-8")

    except:
        stu=int(input("Enter number of students: "))
        for i in range(stu):
            name=input("student name: ")
            score=input("student score: ")
            names.append(name)
            dict[name]=score
        print("sucess")
    while(1):
        print("=====menu====")
        print("1. Find by name")
        print("2. Change a score")
        print("3. save to file")
        print("4. print student list")
        print("0. End program")
        m=int(input("Select Menu: "))
        if(m==0):
            print("Good bye")
            exit()
        center(m)


def center(m):
    if(m==1):
        find_name()
    if(m==2):
        Change()
    if(m==3):
        savefile()
    if(m==4):
        printlist()

def find_name():
    name=input("Enter student name: ")
    if(name in names):
        print(f"name: {name}  score: {dict[name]}")
    else:
        print("name:Error score:can not find student")
def Change():
    name=input("Enter student name: ")
    try:
        tmp=dict[name]
    except:
        print("key error")
        return
    score=int(input("Enter score: "))
    dict[name]=score
    print("success")

def savefile():
    text=open("result.txt", "w+", encoding="utf-8")
    print("Name   Score", file=text)
    for i in range(len(names)):
        print(f'{names[i]}  {dict[names[i]]}', file=text)
    print("saved")
def printlist():
    print(dict)
menu()
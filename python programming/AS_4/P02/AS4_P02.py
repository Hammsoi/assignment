#key를 저장하는 리스트
Info=[]
#딕셔너리
dict={}

#입력된 숫자에 따라 수행
def center(n):
  #key val를 입력받고 저장
  if(n==1):
    Key=input("Enter key: ")
    val=input("Enter val: ")
    Info.append(Key)
    dict[Key]=val
  #Key를 입력 받으면 value 출력. 없다면 Key not found 출력
  if(n==2):
    Key=input("Enter Key: ")
    if(Key in Info):
      print(dict[Key])
    else:
      print("Key not found")
  #key와 value를 튜플로 묶어서 출력
  if(n==3):
    tup=list(zip(dict.keys(),dict.values()))
    print("value: ", tup)
  #key 삭제
  if(n==4):
    Key=input("Enter Key to delete: ")
    if(Key in Info):
      del dict[Key]
      Info.remove(Key)
    else:
      print("Key not found")
#인터페이스 출력 및 center()로 선택한 메뉴 보내기
def menu():
  while(1):
    print(f'Info list: {Info}')
    print("====Select Menu====")
    print("1. Enter Info")
    if(len(Info)!=0):
      print("2. Find Info")
      print("3. Print all")
      print("4. Delete")
    print("0. End program")
    print("===================")
    sel=int(input(": "))
    if(sel==0):
      print("Adios")
      exit()
    center(sel)
    print("-------------------")
menu()
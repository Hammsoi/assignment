
while(1):
    try:
        num=int(input("Enter number for interation: "))
    except:
        print("Enter only Intigers!")
        
    for i in range(1,num):
        if(i % 10==0):
            print(i)
        else:
            print(i,end=",")
    break
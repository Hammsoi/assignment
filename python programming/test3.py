num=int(input("Enter size of Matrix(less then 100): "))
print("     ",end="")
for i in range(1,num+1):
    print(f'{i:<3}',end="")
print("")
for i in range(1,num+1):
    print(f'{i:<3}',end=" ")
    tmp=[]
    for j in range(1,num+1):
        if(i==j):
            tmp.append(1)
        else:
            tmp.append(0)
    print(tmp)
        
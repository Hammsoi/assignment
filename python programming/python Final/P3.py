import random as ran


inp=int(input("Enter number: "))
arr=[]
for i in range(inp):
    arr.append(ran.randint(10,100))
arr=tuple(arr)
tmp=list(arr)
tmp.sort()
arr2=tuple(tmp)
idx1=0
idx2=0
while(1):
    print(f"Original: ",end="")
    for j in range(10):
        if(idx1==len(arr)):
            break
        print(f"{arr[idx1]}    ",end="")
        idx1+=1
    print()
    print(f"  Sorted: ",end="")
    for j in range(10):
        if(idx2==len(arr)):
            break
        print(f"{arr[idx2]}    ",end="")
        idx2+=1
    print()
    if(idx2==len(arr)):
        break
        






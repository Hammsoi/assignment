num=input("Input Data: ")
if(num.isdigit()):
    num=int(num)
    print(type(num))
    print("Change to intiger")
else:
    for i in num:
        if(i.isalpha() or (i!='.' and i.isdigit()==False)):
            print(type(num))
            print("Keep String type")
            break
    else:
        num=float(num)
        print(type(num))
        print("Change to float")
    



# for i in num:
#     if(i=='.'):


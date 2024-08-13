input=input("Enter text: ")

def rever(str):
    ret=""
    for i in range(len(str)):
        ret = str[i]+ret

    return ret

print("Reverse: "+rever(input))
arr=[['영어',80],['수학',70],['국어',75],['과학',85],['파이',50],
     ['수학',60],['영어',50],['파이',70],['과학',90],['국어',90],
     ['파이',100],['수학',80],['과학',65],['영어',90],['국어',90],
     ]

arr2=[]
arr2.append([arr[0][0],arr[0][1],1])
for i in range(1,len(arr)):
        
    for j in range(len(arr2)):
        if(arr[i][0]==arr2[j][0]):
            arr2[j][1]+=arr[i][1]
            arr2[j][2]+=1
            break
    else:
        arr2.append([arr[i][0],arr[i][1],1])
    
print(arr2)

print('과목명   총점    평균')
for i in range(len(arr2)):
    avg=float(arr2[i][1]/arr2[i][2])
    print(f' {arr2[i][0]:<5}{arr2[i][1]:<7}{avg:5.2f}')
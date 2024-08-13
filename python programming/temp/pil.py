score=open('temp/score.txt', 'w', encoding='utf-8')
sum=0
score.write('국어: '+input('국어: '))
score.write('\n영어: '+input('영어: '))
score.write('\n수학: '+input('수학: '))
score.write('\n과학: '+input('과학: '))
score.write('\n파이썬: '+input('파이썬: '))
sub=['국어','영어','수학','과학','수학','파이썬']
scoreL=[]
for i in range(len(sub)):
    tmp=input(f'{sub[i]}: ')
    score.write(f'{sub[i]} :{}')
    
score=open('temp/score.txt', 'r', encoding='utf-8')

ans=score.readlines()
for i in range(len(ans)):
    str=ans[i].split(':')
    sum+=int(str[1])

score=open('temp/score.txt', 'a', encoding='utf-8') 
sav= f'\n총점: {sum}    평균: {sum/5}'
print(sav)
score.write(sav)


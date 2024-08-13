#해댱 위치에 파일이 없을시 프로그램 종료
try:
  tmp = open('./P01/nameList.txt', 'r', encoding='utf-8')
except:
  print('Can not open the file')
  exit()
#줄별로 나누기
nameList = tmp.read().splitlines()

#정렬전 리스트 출력 => 정렬 => 정렬된 리스트 출력
print(nameList)
nameList.sort()
print("Name List Sorted")
print(nameList)
#파일 이릅 입력
filename = input("Enter save file name: ")
#파일을 추가하지 못할 상황 처리
try:
  tmp = open(f'./P01/{filename}.txt', 'w+', encoding='utf-8')
except:
  print(f'Error! output file')
  exit()
#만들어진 파일에 정렬된 리스트 작성
tmp.write('\n'.join(nameList))

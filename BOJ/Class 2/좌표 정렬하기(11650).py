import sys
N=int(sys.stdin.readline().rstrip())                    #정수 N을 입력받는다.
location=[]                                             #튜플 자료형 (x,y)를 저장하기 위한 리스트 선언한다.
for i in range(N):
    x,y=map(int,sys.stdin.readline().split())           #좌표 x,y를 공백으로 구분하여 선언하고
    location.append((x,y))                              #location 리스트에 삽입한다.
location.sort(key = lambda x: (int(x[0]), int (x[1])))  #lambda함수를 이용해서 x좌표가 증가하는 순으로(x의 값이 동일하다면), y좌표가 증가하는 순으로 정렬한다.
for i in location:
    print(i[0],i[1])                                    #정렬된 location 리스트에서 x,y좌표를 출력한다.
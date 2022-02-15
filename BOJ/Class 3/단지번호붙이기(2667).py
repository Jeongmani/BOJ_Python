import sys

def dfs(x,y):                            #재귀 함수를 이용한 dfs를 구현
    global numbering
    if x<=-1 or x>=N or y<=-1 or y>=N:   #범위를 나가는 x,y값에 대해서는 Fasle값을 리턴
        return False
    if graph[x][y]==1:                   #graph[x][y]의 값이 1이라면 그 수를 0으로 바꾸고 재귀함수를 실행
        numbering+=1                     #단지를 구성한 곳의 수를 count하기 위해서 재귀함수가 실행될 때 마다 numbering이 증가되도록함
        graph[x][y]=0
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False

N=int(sys.stdin.readline().rstrip())
graph=[]                                 #2차원 리스트를 저장하기 위한 초기 리스트를 선언해줌
numbering_list=[]                        #단지를 구성하는 곳의 수를 저장하기 위한 리스트를 선언해줌
for i in range(N):
    graph.append(list(map(int,sys.stdin.readline().rstrip())))

numbering=0                              #단지를 구성하는 곳의 수
count=0                                  #단지의 수
for i in range(N):
    for j in range(N):
        if dfs(i,j)==True:               #dfs를 진행
            numbering_list.append(numbering)    #단지를 구성하는 곳의 수를 리스트에 저장
            count+=1                     #단지의 수를 1씩 증가
            numbering=0                  #단지를 구성하는 곳의 수를 0으로 초기화
print(count)
numbering_list.sort()                    
for i in numbering_list:
    print(i)

from collections import deque                   #덱 함수를 이용해 BFS를 하기 위해서 라이브러리 이용
import sys

N,M=map(int,sys.stdin.readline().split())
graph=[]                                        #graph의 정보를 2차원 리스트로 저장하기 위한 리스트 선언
data=[]                                         #익은 토마토가 있는곳을 저장하기 위한 리스트 선언
for i in range(M):
    graph.append(list(map(int,sys.stdin.readline().split())))   #공백으로 구분하여 리스트에 저장
    for j in range(N):                         
        if graph[i][j]==1:                       
            data.append((i,j))                  #익은 토마토가 있는곳을 data리스트에 저장
dx=[1,-1,0,0]                                   # 상하좌우로 익은 토마토가 전파됨으로 dx,dy를 선언
dy=[0,0,1,-1]
queue=deque(data)
while queue:                                    #queue를 이용한 BFS탐색 진행
    x,y=queue.popleft()
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx>=0 and nx<M and ny>=0 and ny<N:   #graph의 범위를 벗어나는 수는 고려하지 않음(overflow 방지)
            if graph[nx][ny]==0:
                graph[nx][ny]=graph[x][y]+1     #몇번째로 진행되었는지 알기위해서 +1을 해줌
                queue.append((nx,ny))
result=0                                        
for i in graph:
    for j in i:
        if j==0:
            print(-1)                           #아직 익지 않은 토마토가 있는경우 -1을 출력하고 프로그램 종료
            exit(0)
    result=max(result,max(i))
print(result-1)                                 #결과 값 출력
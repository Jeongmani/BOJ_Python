from collections import deque

N,M=map(int,input().split())
graph=[]                                    #2차원 리스트를 저장하기 위한 리스트를 선언한다.
for i in range(N):
    graph.append(list(map(int,input())))    #입력받은 값을 graph에 리스트 형태로 저장한다
dx=[1,-1,0,0]                               #상하 좌우로 움직이기 위해서 dx,dy를 리스트 형태로 만들어 둔다.
dy=[0,0,1,-1]

def bfs(x,y):
    queue=deque()
    queue.append((x,y))                     #큐 자료 구조를 이용해서 bfs를 진행한다.
    while queue:
        x,y=queue.popleft()
        for i in range(4):                  #nx,ny는 상하좌우 갈 수 있는 곳을 말한다
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=M:  #범위를 지나는 경우 건너뛴다
                continue
            if graph[nx][ny]==0:                #상하좌우로 움직일 수 있는 곳이 0이라면 건너뛴다 
                continue
            if graph[nx][ny]==1:                #상하좌우로 움직일 수 있는 곳이 1이라면
                graph[nx][ny]=graph[x][y]+1     #도착한 곳에 1 증가시켜 우측 아래까지의 얼마나 걸리는지 구할 수 있다.
                queue.append((nx,ny))           #(이 경우 (0,0)이 3이 될 수 있지만 단순하게 (N,M)으로의 거리를 구하는 것이므로 정상적으로 답을 도출)
    return graph[N-1][M-1]

print(bfs(0,0))

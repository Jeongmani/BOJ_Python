import sys
from collections import deque                                       #deque함수를 써서 bfs를 구현할 것이다.
input=sys.stdin.readline 

N = int(input())
graph = []                                                          #2차원 배열을 저장할 리스트를 선언한다.
max_number= 0                                                       #2차원 배열에서 가장 높은 위치를 저장할 변수를 선언한다.
 
for i in range(N):
    graph.append(list(map(int, input().split())))                   #미리 선언한 graph에 리스트를 추가한다.
    max_number=max(max(graph[i]),max_number)                        #리스트에서 가장 큰수를 저장한다.
 
 
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(a, b, floor, visited):                                      #bfs함수를 구현한다. 
    queue = deque()
    queue.append((a, b))
    visited[a][b] = 1                                               #매번 초기화 되는 visited함수에 위치를 1로 표시할 것이다.
 
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] > floor and visited[nx][ny] == 0: #물에 잠기지 않는 위치이면서 아직 vistied에 표시되지 않았다면 1로 표시한다.     
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
 
result = 0
for i in range(max_number):                                         #물의 높이를 건물이 모두 잠기는 max_number 바로 전까지 실행할 것이다.
    visited=[[0] * N for i in range(N)]                             #높이는 저장되어 있지 않지만 수면보다 높이가 높다면 1 아니면 0을 저장할 리스트이다.
    count = 0
    for j in range(N):
        for k in range(N):
            if graph[j][k] > i and visited[j][k] == 0:              #조건을 만족하는 곳에서 bfs를 진행하고 안전영역을 1증가 시킨다.
                bfs(j, k, i, visited)
                count += 1
    if result < count:                                              #i번째 높이의 수면애서 가장 큰 값이라면 그 값을 결과로 저장한다.
        result = count
 
print(result)

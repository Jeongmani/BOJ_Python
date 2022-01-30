import sys
from collections import deque
input=sys.stdin.readline

N=int(input())
node=[[]for _ in range(N+1)]                        #노드에 연결된 정보를 저장하기 위한 리스트를 선언하다.
graph=[]                                            #초기 그래프의 정보와 변경된 그래프의 정보를 저장할 리스트이다.

for i in range(N):
    i_node=list(map(int,input().split()))           #i번째 노드의 정보를 입력받아 그래프에 넣어준다.
    graph.append(i_node)
    for j in range(N):
        if graph[i][j]==1:
            node[i+1].append(j+1)                   #만약 j번째 인덱스의 값이 1이라면 i번째 노드에서 j번째 인덱스로 가는 간선이 있다는 뜻임으로 노드 리스트에 넣는다.

def bfs(x):                                         #bfs를 진행하기 위해서 bfs함수를 구현한다.
    q=deque()
    q.append(x)
    visited=[False]*N                               #큐 자료구조를 이용해서 진행할 것이고 각각의 노드에서 다른 노드로 가는 경우를 저장할 리스트를 설정한다.
    while q:
        now=q.popleft()
        for i in node[now]:
            if not visited[i-1]:    
                visited[i-1]=True                   #아직 방문하지 않았다면 방문처리하고
                q.append(i)
    for i in range(N):
        if visited[i]==True:                        #bfs가 끝난 후에 visited리스트에 인덱스의 값이 True인 것들을 1로 바꾸어 준다.
            graph[x-1][i]=1

for i in range(N):
    bfs(i+1)                                        #각각의 노드별로 bfs탐색을 진행하고

for i in range(N):
    for j in range(N):
        print(graph[i][j],end=' ')                  #그래프를 출력한다.
    print()

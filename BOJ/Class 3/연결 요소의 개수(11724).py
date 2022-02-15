import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**4)                #최악의 경우 M이 dfs함수가 500번 실행 될 수 있으면 recursionlimit을 설정해 주었다.
def dfs(x):
    visited[x-1]=True                       #처음 방문한 곳을 True로 반환하고
    for i in graph[x-1]:                    #연결된 곳중에 아직 방문하지 않은 곳이 있다면
        if visited[i-1]==False:
            dfs(i)                          #그 곳에서 dfs를 재귀적으로 실행한다.

N,M=map(int,input().split())
visited=[False]*N                           #N개의 노드를 아직 방문하지 않은곳으로 만든다.
count=0                                     #연결 요소의 개수를 count변수로 선언한다.
graph=[[] for i in range(N)]                #컴프리헨션을 이용해 그래프의 어떤 노드와 연결되어있는지 기록한다.

for _ in range(M):
    A,B=map(int,input().split())
    graph[A-1].append(B)                    #방향성이 없는 노드임으로 A에 B를 추가한다.
    graph[B-1].append(A)                    #B에 A를 추가한다.

for i in range(N):                          #순차적으로 dfs탐색을 진행한다.
    if visited[i]==False:
        count+=1                            #연결요소의 개수를 1씩 증가한다.
        dfs(i)
    
print(count)

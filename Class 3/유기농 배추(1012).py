import sys
sys.setrecursionlimit(10**4)            
input = sys.stdin.readline
Test_case=int(input())                      #테스트 케이스를 입력받는다.

def dfs(x,y):                               #dfs로 탐색하기 위해서 재귀함수를 이용해서 dfs를 구현함.                               
    if x<=-1 or x>=N or y<=-1 or y>=M:  
        return False
    if graph[x][y]==1:                      #현재 방문한 노드가 1이라면
        graph[x][y]=0                       #그 노드를 방문 처리하기 위해서 0으로 변경
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False

for _ in range(Test_case):              
    M,N,K=map(int,input().split())          
    graph=[[0]*M for _ in range(N)]         #2차원 리스트를 초기화

    for _ in range(K):
        x,y=map(int,input().split())
        graph[y][x]=1                       #입력 받은값을 1로 변경해준다 (x,y로 받고 graph[y][x]로 해준 이유는 x는 가로길이 즉, 행을 의미하고 y는 세로 길이 즉, 열을 의미하기 때문  )

    result=0
    for i in range(N):  
        for j in range(M):
            if graph[i][j]==1:              #확인한 그래프의 노드의 값이 1일 경우 dfs함수를 실행하고 result에 1값을 증가시킨다.
                dfs(i,j)
                result+=1
    print(result)

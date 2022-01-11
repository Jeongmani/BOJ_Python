import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)                        #recursion error를 방지하기 위해서
def dfs(x,y):                                       #대각선을 포함한 상하좌우 8개의 방향을 재귀적으로 진행한다.
    if x<=-1 or x>=height or y<=-1 or y>=width:     #범위를 나간 경우는 Fasle값을 리턴한다.
        return False
    if graph[x][y]==1:                              #1, 즉 땅 인경우에는 재귀적으로 dfs함수를 실행한다.
        graph[x][y]=0
        dfs(x-1,y)
        dfs(x-1,y-1)
        dfs(x-1,y+1)
        dfs(x,y-1)
        dfs(x,y+1)
        dfs(x+1,y)
        dfs(x+1,y-1)
        dfs(x+1,y+1)
        return True
    return False
    
while True:
    width,height=map(int,input().split())
    if width==0 and height==0:                      #0,0을 입력받으면 프로그램을 종료한다.
        break
    graph=[]                                        #2차원 그래프를 저장한 리스트를 선언한다.
    result=0
    for i in range(height):
        graph.append(list(map(int,input().split())))
    for i in range(height):
        for j in range(width):
            if dfs(i,j)==True:                      #graph[i][j]에서 탐색을 진행하고 True값을 반환한다면
                result+=1                           #result를 1을 증가한다.
    print(result)

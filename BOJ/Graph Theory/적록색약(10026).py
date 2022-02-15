import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs_0(x,y):                             #적록색약인 경우 
    if x<=-1 or x>=N or y<=-1 or y>=N:
        return False
    if graph_RGB[x][y]==0:
        graph_RGB[x][y]=1
        dfs_0(x-1,y)
        dfs_0(x+1,y)
        dfs_0(x,y-1)
        dfs_0(x,y+1)
        return True
    return False
def dfs_1(x,y):                            #R인경우 그래프에서 1로 변경해서 저장했기 때문에 R인경우 깊이 우선 탐색을 진행한다.
    if x<=-1 or x>=N or y<=-1 or y>=N:     #범위를 나간경우에는 False값을 반환한다
        return False
    if graph_RGB[x][y]==1:
        graph_RGB[x][y]=0                  #적록색약에서 G와 함께 계산하기 위해서 0으로 변경해준다.
        dfs_1(x-1,y)
        dfs_1(x+1,y)
        dfs_1(x,y-1)
        dfs_1(x,y+1)
        return True
    return False
def dfs_2(x,y):                            #G인경우 그래프에서 2로 변경해서 저장했기 때문에 G인경우 깊이 우선 탐색을 진행한다.
    if x<=-1 or x>=N or y<=-1 or y>=N:     #범위를 나간경우에는 False값을 리턴
        return False
    if graph_RGB[x][y]==2:
        graph_RGB[x][y]=0                  #적록색약에서 R과 함께 계산하기 위해서 0으로 변경해준다.
        dfs_2(x-1,y)
        dfs_2(x+1,y)
        dfs_2(x,y-1)
        dfs_2(x,y+1)
        return True
    return False
def dfs_3(x,y):                            #B인경우 그래프에서 3로 변경해서 저장했기 때문에 B인경우 깊이 우선 탐색을 진행한다.
    if x<=-1 or x>=N or y<=-1 or y>=N:
        return False
    if graph_RGB[x][y]==3:
        graph_RGB[x][y]=4                  #적록색약에서 R,G와 함께 계산하지 않기 위해서 4로 변경해서 저장한다.
        dfs_3(x-1,y)
        dfs_3(x+1,y)
        dfs_3(x,y-1)
        dfs_3(x,y+1)
        return True
    return False
    
N=int(input().rstrip())
graph_RGB=[]
for _ in range(N):
    RGB=list(map(str,input().rstrip()))
    for i in range(N):                     #R=1, G=2, B=3으로 바꾸어 2차원 리스트에 저장한다.
        if RGB[i]=='R':
            RGB[i]=1
        elif RGB[i]=='G':
            RGB[i]=2
        else:
            RGB[i]=3
    graph_RGB.append(RGB)
result_RGB=0                               #적록색약이 없는 경우 영역을 저장할 변수를 선언한다.
result_RB=0                                #적록색약이 있는 경우 영역을 저장할 변수를 선언하다.
for i in range(N):
    for j in range(N):
        if graph_RGB[i][j]==1:             #1인 경우에는 dfs_1을 진행하고 적록색약이 아닌 경우의 result를 1추가
            dfs_1(i,j)
            result_RGB+=1
        elif graph_RGB[i][j]==2:           #2인 경우에는 dfs_2을 진행하고 적록색약이 아닌 경우의 result를 1추가
            dfs_2(i,j)
            result_RGB+=1
        elif graph_RGB[i][j]==3:           #3인 경우에는 dfs_3을 진행하고 적록색약이 아닌 경우의 result를 1추가, 적록색약 또한 B를 구분할 수 있으므로 result_RB도 1추가
            dfs_3(i,j)
            result_RGB+=1
            result_RB+=1
for i in range(N):
    for j in range(N):
        if graph_RGB[i][j]==0:             #0인 경우는 R또는 G인 경우임이다 둘다 같이 판단하는 dfs_0을 실행하고 , result_RB를 1추가 한다.
            dfs_0(i,j)
            result_RB+=1

print(result_RGB,result_RB)

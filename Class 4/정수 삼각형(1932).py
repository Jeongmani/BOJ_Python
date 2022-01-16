import sys
input=sys.stdin.readline
N=int(input())
N_tri=[]
for _ in range(N):
    N_tri.append(list(map(int,input().split())))
    
for i in range(1,N):
    for j in range(i+1):
        if j==0:
            N_tri[i][j]=N_tri[i][j]+N_tri[i-1][j]                           #정수 삼각형의 가장 왼쪽에 있는 수는 선택할 수 있는 부모 수가 가장 왼쪽 수이다.
        elif i==j:
            N_tri[i][j]=N_tri[i][j]+N_tri[i-1][j-1]                         #정수 삼각형의 가장 오른쪽에 있는 수는 선택할 수 있는 부모 수가 가장 오른쪽 수이다.
        else:
            N_tri[i][j]=N_tri[i][j]+max(N_tri[i-1][j],N_tri[i-1][j-1])      #두가지의 특수한 경우가 아니라면 부모 수 중에서 큰 수를 취해준다.

print(max(N_tri[N-1]))                                                      #가장 밑의 자식에서 가장 큰 수를 출력한다.

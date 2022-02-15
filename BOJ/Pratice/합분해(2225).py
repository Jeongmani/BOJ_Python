import sys
input=sys.stdin.readline

N,K=map(int,input().split())
dp=[[0 for _ in range(N)]for _ in range(K)]     #dp리스트를 형성한다.
for i in range(N):                              #K가 1인경우는 경우의 수가 1이다.
    dp[0][i]=1  
for i in range(K):                              #N=1일때 K가 증가함에따라 K의 경우가 생긴다 ex)K=3 (0,0,1) (0,1,0) (1,0,0)
    dp[i][0]=i+1
for i in range(1,K):
    for j in range(1,N):
        dp[i][j]=dp[i-1][j]+dp[i][j-1]          #N,K는 N-1, K의 경우의 수와 N,K-1의 경우의 수를 더한 값과 같다.
print(dp[K-1][N-1]%1000000000)

def solution(m, n, puddles):
    map_sample=[[1 for _ in range(m)]for _ in range(n)]
    for i in puddles:
        x=i[0]
        y=i[1]
        map_sample[y-1][x-1]=0
    dp=[[0 for _ in range(m)]for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if map_sample[i][j]==1:
                if i==0 and j==0:
                    dp[i][j]=1
                elif i==0:
                    dp[i][j]=(dp[i][j-1])%1000000007
                elif j==0:
                    dp[i][j]=(dp[i-1][j])%1000000007
                else:
                    dp[i][j]=(dp[i-1][j]+dp[i][j-1])%1000000007
    answer=dp[n-1][m-1]
    return answer

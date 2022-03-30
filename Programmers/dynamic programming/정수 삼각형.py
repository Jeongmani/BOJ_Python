def solution(triangle):
    height=len(triangle)
    dp=[[0]*(i+1) for i in range(height)]
    dp[0][0]=triangle[0][0]
    for i in range(1,height):
        for j in range(len(dp[i])):
            if j==0:
                dp[i][j]=dp[i-1][j]+triangle[i][j]
            if j==(len(dp[i])-1):
                dp[i][j]=dp[i-1][j-1]+triangle[i][j]
            if j !=0 and j != (len(dp[i])-1) : 
                dp[i][j]=max(dp[i-1][j-1],dp[i-1][j])+triangle[i][j]
    return max(dp[height-1])

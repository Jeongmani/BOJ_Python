import sys
input=sys.stdin.readline
n=int(input())
dp=[[0]*10 for _ in range(n+1)]
dp[1]=[0,1,1,1,1,1,1,1,1,1]
for i in range(2,n+1):
    dp[i][0]=dp[i-1][1]                     #0은 1뒤에서만 나올 수 있다.
    dp[i][9]=dp[i-1][8]                     #9는 8뒤에서만 나올 수 있다.
    for j in range(1,9):
        dp[i][j]=dp[i-1][j-1]+dp[i-1][j+1]  #ex) 2는 1,3뒤에 나올 수 있다, 그러므로 i-1번쨰 1과,3을 더 한 값과 같다.
print(sum(dp[n])%1000000000)
    

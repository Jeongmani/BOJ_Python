import sys
input=sys.stdin.readline
A=input().rstrip()                                          
B=input().rstrip()
dp=[[0 for _ in range(len(B)+1)]for _ in range(len(A)+1)]   #DP를 진행하기 위한 리스트를 형성한다.
for i in range(1,len(A)+1):
    for j in range(1,len(B)+1):
        if A[i-1]==B[j-1]:                                  #A[i]와 B[j]에 값이 같다면 
            dp[i][j]=dp[i-1][j-1]+1                         #dp[i][j]에 그 전 값+1을 한다.
        else:
            dp[i][j]=max(dp[i][j-1],dp[i-1][j])             #아니면 dp[i][j-1],dp[i-1][j]값중 큰 값을 결정한다.
            
print(dp[-1][-1])
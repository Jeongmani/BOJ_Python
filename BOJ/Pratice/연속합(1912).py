import sys
input=sys.stdin.readline
A=int(input())
arr=list(map(int,input().split()))
dp=[0 for _ in range(A)]                #다이나믹 프로그래밍을 진행하기 위해 정보를 저장할 리스트를 형성한다.
dp[0]=arr[0]

for i in range(1,A):
    dp[i]=max(dp[i-1]+arr[i],arr[i])    #자기자신or그 전까지의 합+자기자신 중에 큰 것을 선택한다.
print(max(dp))

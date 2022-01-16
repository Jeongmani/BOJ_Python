import sys
input=sys.stdin.readline

N=int(input())
N_list=list(map(int,input().split()))
dp=[1]*N                                    #최소인 경우가 1임으로 모두 1로 초기화한다.
for i in range(1,N):                        #0번째 인덱스는 무조건 1임으로 1번째 인덱스부터 진행한다.
    for j in range(i):                      #i번째 인덱스와 비교대상이 되어질 i이전까지의 인덱스 j이다.
        if N_list[i]>N_list[j]:             #리스트에 i번째 인덱스가 j번째 인덱스보다 크다면
            dp[i]=max(dp[i],dp[j]+1)        #j번째 인덱스에 1추가한값과 dp[i]와 비교해서 큰 값을 취한다.
    
print(max(dp))

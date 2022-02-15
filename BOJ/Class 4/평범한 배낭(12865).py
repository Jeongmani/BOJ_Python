import sys
input=sys.stdin.readline
N,K=map(int,input().split())                                    #물건의 수와 최대 무게를 입력받는다.
thing=[[0,0]]                                                   #물건의 무게와 가치를 저장할 리스트를 선언한다.
dp=[[0]*(K+1) for _ in range(N+1)]                              #2차원 리스트 형태의 dp 테이블을 선언한다.

for i in range(N):
    thing.append(list(map(int,input().split())))                #물건의 무게와 가치를 입력받는다.
    
for i in range(1,N+1):                                          #dp테이블을 채워 나갈 것이다.
    for j in range(1,K+1):
        weight=thing[i][0]                                      #물건의 무게
        value=thing[i][1]                                       #물건의 가치
        if j<weight:                                            #j보다 무게가 큰 경우
            dp[i][j]=dp[i-1][j]                                 #즉, 그 물건을 선택하지 못하는 경우는 i-1 행의 j열의 값과 같다.
        else:                                                   #j보다 무게가 작은 경우
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-weight]+value)    #즉, 그 물건을 선택 할 수 있는경우에는 선택하는 것과 선택하지 않은것 중 큰 값을 가져간다.

print(dp[N][K])                                                 #최종적으로 dp테이블에 가장 끝 부분에 있는 수를 출력한다.

import sys
input=sys.stdin.readline
N=int(input())
list_wine=[]                                                                    #와인의 정보를 저장할 리스트를 생성한다.                                            
for i in range(N):
    list_wine.append(int(input()))                                              #리스트에 와인의 대한 정보를 넣는다.

dp=[0 for i in range(N)]                                                        #다이나믹 프로그래밍을 진행하기위한 리스트를 형성한다.
dp[0]=list_wine[0]                                                              
if N>1:
    dp[1]=max(list_wine[0]+list_wine[1],list_wine[1])                           #N이 1인경우에 선택할 수 있는 것은 첫번째 와인이다.
if N>2:
    dp[2]=max(list_wine[1]+list_wine[2],list_wine[0]+list_wine[2],dp[1])        #N이 2일때 선택할 수 있는 것은 첫번째+두번째와인, 두번째 와인이다. 하지만 와인에 음수가 없음으로 무조건 첫번째+두번째 와인을 선택할 것이다.
for i in range(3,N):
    dp[i]=max(dp[i-1],dp[i-3]+list_wine[i-1]+list_wine[i],dp[i-2]+list_wine[i]) #N이 3이상인 경우에는 앞에 두 와인이 선택되어 i번째 와인을 선택하지 않거나, 바로 전 와인과 i번째 와인을 선택하거나, 전 와인을 선택하지 않고 i번째 와인을 선택하는 경우가 있다.
print(dp[N-1])

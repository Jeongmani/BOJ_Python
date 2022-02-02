import sys
input=sys.stdin.readline

N=int(input())
stair=[0 for i in range(N)]                                     #계단의 정보를 저장할 리스트를 형성한다.
for i in range(N):
    stair[i]=int(input())                                       #계단의 정보를 입력받고
dp=[0 for i in range(N)]                                        #다이나믹프로그래밍을 진행할 리스트를 형성한다.
dp[0]=stair[0]                                                  #첫번째 계단은 무조건 stair의 0번째 인덱스
if N>=2:
    dp[1]=max(stair[1],stair[0]+stair[1])                       #주어진 계단이 2개 이상이라면 dp[1]
if N>=3:
    dp[2]=max(stair[0]+stair[2],stair[1]+stair[2])              #주어진 계단이 3개 이상이라면 dp[2]

for i in range(3,N):                                            #주어진 계단이 3개 이상일때 다이나믹 프로그래밍 
    dp[i]=max(dp[i-2]+stair[i],dp[i-3]+stair[i]+stair[i-1])
    
        
print(dp.pop())

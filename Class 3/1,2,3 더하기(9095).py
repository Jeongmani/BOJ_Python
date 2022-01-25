import sys
input=sys.stdin.readline

dp=[0 for _ in range(11)]           #다이나믹 프로그래밍을 진행하기 위한 리스트를 만든다.
dp[1]=1                             #1을 만들기 위한 경우의 수를 저장한다
dp[2]=2                             #2을 만들기 위한 경우의 수를 저장한다.
dp[3]=4                             #3을 만들기 위한 경우의 수를 저장한다.
for i in range(4,11):               #n을 만들기 위해서는 그거보다 1,2,3 작은 수에 3,2,1을 더하는 문제로 만들 수 있기 때문에 다이나믹 프로그래밍이 가능하다.
    dp[i]=dp[i-3]+dp[i-2]+dp[i-1]
testcase=int(input())
for _ in range(testcase):           #테스트 케이스의 수를 입력받아 그 결과값을 출력한다.
    num=int(input())
    print(dp[num])

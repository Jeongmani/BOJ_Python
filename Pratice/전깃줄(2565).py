import sys
input=sys.stdin.readline
N=int(input())
string=[]                           #전깃줄의 정보를 저장할 리스트를 선언한다.
for i in range(N):
    a,b=map(int,input().split())
    string.append((a,b))            #전깃줄의 정보를 담아 a,b에 각각 연결된 정보를 받고
string.sort(key=lambda x:x[0])      #a에 걸려있는 순서대로 정렬한다.
B=[]                                #이 리스트는 a를 오름차순으로 정렬한 뒤 b에 연결된 정보를 저장할 리스트이다.
dp=[0 for i in range(N)]            #다이나믹 프로그래밍을 진행하기 위해 리스트를 초기화한다.
for i in string:
    B.append(i[1])  
for i in range(N):
    for j in range(i):
        if B[i]>B[j] and dp[i]<dp[j]:   #b에서 가장 긴 증가하는 수열을 구한뒤 N개에서 빼줄 것이다.
            dp[i]=dp[j]                 #이유는 가장 긴 증가하는 수열이 최대 개수 일 것이다.
    dp[i]+=1
print(N-max(dp))

    

import sys
input=sys.stdin.readline
N,M=map(int,input().split())
num=list(map(int,input().split()))
sum_num=0
for i in range(N):
    sum_num+=num[i]                             #미리 누적합을 구하고 거기서 빼는 방식을 이용했다.
    num[i]=sum_num                              #처음에 받은 숫자 리스트를 누적합 리스트로 변경하고

for _ in range(M):
    start,end=map(int,input().split())
    if start==1:                                #구간을 받으면 그 구간만큼의 합을 출력한다.
        print(num[end-1])
    else:
        print(num[end-1]-num[start-2])
    

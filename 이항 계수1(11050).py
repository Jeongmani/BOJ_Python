import sys
N,K=map(int,sys.stdin.readline().split())   #N,K를 공백으로 구분하여 받기(공부하던중 sys에 대해 배워서 input대신 사용)

N_list=[i+1 for i in range(N)]   # 펙토리얼 연산을 위해서 1부터 N까지 수를 리스트에 넣기
K_list=[i+1 for i in range(K)]
del N_list[0:N-K]     # 0<=K<=N 조건에서 이항계수는 n!/(k!(n-k)!) 이므로 n에서 n-k만큼 빼기

n=0  #나머지 N의 리스트를 곱해서 저장할 n,k값 초기화
k=0
for i in N_list:
    if n==0:
        n=i
    else:
        n*=i 
for j in K_list:
    if k==0:
        k=j
    else:
        k*=j
if n==k:         #두개의 값이 같을 경우 0으로 나누어지는 zerodivision error 방지를 위한 코드
    print(1)
else:
    print(n//k)  # 두수의 이항계수 구하기
import sys                                         #처음에는 우선순위 큐를 이용해 제일 작은 값부터 리스트를 돌며 랭킹을 주는 식으로 코딩을 진행했지만 문제에서 시간초과오류가 발생
n=int(sys.stdin.readline().rstrip())
N=list(map(int,sys.stdin.readline().split()))
N_set=sorted(list(set(N)))                         #set 자료형을 이용해 중복이 되는 수를 줄여주고
dic={N_set[i] : i for i in range(len(N_set))}      #사전 자료형을 통해 수 별로 key값을 부여해 
for i in N:                                        #N에서 숫자별로 key값을 출력함                
    print(dic[i],end=' ')   
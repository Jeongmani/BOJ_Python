import sys
from itertools import combinations_with_replacement      #itertools 라이브러리에서 combinations_with_replacement(중복조합)을 이용해서 문제를 푼다.
input=sys.stdin.readline

N,M=map(int,input().split())            #N,M을 input받고 
N_list=[i+1 for i in range(N)]          #리스트 컴프리헨션을 이용해 조합에 사용되는 수를 넣어준다 
if M==1:
    for i in N_list:                    #M이 1인 경우 리스트에 있는 수를 그대로 하나씩 출력한다.
        print(i)
else:
    data=list(combinations_with_replacement(N_list,M))   #중복조합 함수를 이용해 N_list에 있는 수를 M개 뽑는다.
    for i in data:
        for j in i:
            print(j,end=' ')            #사전 순으로 저장됨으로 data에 저장된 N_list에 M개 뽑을 조합을 출력한다
        print()

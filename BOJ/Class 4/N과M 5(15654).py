import sys
from itertools import permutations      #itertools 라이브러리에서 permutations(순열)을 이용해서 문제를 푼다.
input=sys.stdin.readline

N,M=map(int,input().split())            #N,M을 input받고 
N_list=list(map(int,input().split()))   #map함수를 이용하여 N_list에 공백으로 구분해서 저장한다
N_list.sort()                           #입력 받은 N_list을 오름차순으로 정렬한다
if M==1:                                #M이 1인 경우 리스트에 있는 수를 그대로 하나씩 출력한다.
    for i in N_list:                    
        print(i)
else:
    data=list(permutations(N_list,M))   #순열 함수를 이용해 N_list에 있는 수를 M개씩 정렬한다.
    for i in data:
        for j in i:
            print(j,end=' ')            #data에 저장된 N_list에 M개 뽑을 조합을 출력한다
        print()

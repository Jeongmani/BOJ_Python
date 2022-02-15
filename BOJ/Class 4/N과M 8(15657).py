from itertools import combinations_with_replacement         #중복조합을 이용
import sys

N,M=map(int,input().split())
number_list=list(map(int,input().split()))
number_list.sort()                                          #사전순으로 출력하기 위해서 미리 리스트를 sort해준다.
result=list(combinations_with_replacement(number_list,M))   #중복 조합으로 M개를 뽑는다.

for i in result:
    for j in range(M):
        print(i[j],end=' ')                                 #결과를 출력한다.
    print()

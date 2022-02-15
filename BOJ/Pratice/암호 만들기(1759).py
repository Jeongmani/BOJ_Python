import sys
input=sys.stdin.readline
from itertools import combinations

def make_code():                            #가능한 암호를 만드는 함수
    result=[]                               #결과를 저장할 리스트를 형성한다.
    for i in list(combinations(alpha,L)):   #조합을 통해 얻은 alpha에서 L개를 뽑는 경우
        vo_cnt=con_cnt=0                    #자음과 모음의 개수를 저장할 변수를 선언
        for j in i:                         #조합(alpha에서 L개를 뽑은)에서 각각의 알파벳 판별
            if j in vowels:                 #모음의 집합에 있다면 모음의 수 추가
                vo_cnt+=1
            else:
                con_cnt+=1                  #자음의 수를 추가
        if vo_cnt>0 and con_cnt>1:          #요구 조건 모음 최소1개와 자음 최수 2개의 조건을 만족하면 result에 추가
            result.append("".join(i))
    return result

L,C=map(int,input().split())
alpha=list(map(str,input().split()))
alpha.sort()

vowels=set(['a','e','i','o','u'])


for i in make_code():                      #함수에서 return된 리스트에 저장된 결과를 출력
    print(i)
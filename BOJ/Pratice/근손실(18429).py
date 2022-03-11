import sys
import itertools
input=sys.stdin.readline

N,K=map(int,input().split())
kit=list(map(int,input().split()))
permutations=list(itertools.permutations([i for i in kit],N))
result=0
num=0
for i in permutations:
    kg=500
    for j in i:
        if kg<500:
            break
        kg+=j
        kg-=K
    if kg>=500:
        result+=1
print(result)
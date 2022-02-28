import sys
input=sys.stdin.readline

N=int(input())
weight=list(map(int,input().split()))
weight.sort()
target=1

for i in weight:
    if target<i:
        break
    target+=i
print(target)

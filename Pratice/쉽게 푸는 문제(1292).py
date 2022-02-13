import sys
input=sys.stdin.readline

A,B=map(int,input().split())
arr=[0]
for i in range(50):
    for j in range(i):
        arr.append(i)
result=sum(arr[A:B+1])
print(result)
import sys
input=sys.stdin.readline

N=int(input())
test=list(map(int,input().split()))
main,sub=map(int,input().split())
result=0
for i in test:
    if i>=main:
        i-=main
        if i%sub==0:
            result+=i//sub
        else:
            result+=i//sub +1
        
print(result+N)

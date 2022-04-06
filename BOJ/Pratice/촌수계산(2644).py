def dfs(node):
    for n in family[node]:
        if check[n]==0:
            check[n]=check[node]+1
            dfs(n)

N=int(input())
target1,target2=map(int,input().split())
test_case=int(input())
family=[[]for _ in range(N+1)]
for i in range(test_case):
    A,B=map(int,input().split())
    family[A].append(B)
    family[B].append(A)
check=[0]*(N+1)
dfs(target1)
print(check[target2] if check[target2] >0 else -1)

def dfs(computers,v,answer):
    answer[v]=True
    for j in range(len(computers[v])):
        if computers[v][j]==1:
            if answer[j]==False:
                dfs(computers,j,answer)
            
def solution(n, computers):
    answer = [False]*n
    net=0
    for i in range(n):
        if answer[i]==False:
            dfs(computers,i,answer)
            net+=1
    return net

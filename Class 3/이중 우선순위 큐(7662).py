import heapq
import sys

T=int(sys.stdin.readline().rstrip())
for _ in range(T):
    array_min=[]
    array_max=[]
    visited=[False]*1_000_001
    k=int(sys.stdin.readline().rstrip())
    for key in range(k):
        command=sys.stdin.readline().split()
        if command[0]=='I':
            heapq.heappush(array_min,(int(command[1]),key))
            heapq.heappush(array_max,(-int(command[1]),key))
            visited[key]=True
        else:
            if command[1]=='-1':
                while array_min and not visited[array_min[0][1]]:
                    heapq.heappop(array_min)
                if array_min:
                    visited[array_min[0][1]]=False
                    heapq.heappop(array_min)
                
            elif command[1]=='1':
                while array_max and not visited[array_max[0][1]]:
                    heapq.heappop(array_max)
                if array_max:
                    visited[array_max[0][1]]=False
                    heapq.heappop(array_max)
    
    while array_min and not visited[array_min[0][1]]:
        heapq.heappop(array_min)    
    while array_max and not visited[array_max[0][1]]:
        heapq.heappop(array_max)
    if array_min and array_max:
        print(-array_max[0][0],array_min[0][0])
    else:
        print('EMPTY')
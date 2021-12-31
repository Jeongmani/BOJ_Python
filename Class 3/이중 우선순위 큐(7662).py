import heapq
import sys
array_min=[]
array_max=[]
T=int(sys.stdin.readline().rstrip())
for _ in range(T):
    k=int(sys.stdin.readline().rstrip())
    for _ in range(k):
        command=list(map(str,sys.stdin.readline().split()))
        if command[0]=='I':
            heapq.heappush(array_min,int(command[1]))
            heapq.heappush(array_max,-int(command[1]))
        if command[0]=='D':
            if len(array_min)==0 or len(array_max) ==0:
                pass
            else:
                if command[1]=='1':
                    a=-heapq.heappop(array_max)
                    array_min.remove(a)
                elif command[1]=='-1':
                    a=-heapq.heappop(array_min)
                    array_max.remove(a)
    if len(array_min)==0 or len(array_max) ==0:
        print('EMPTY')
    else:    
        print(-heapq.heappop(array_max),heapq.heappop(array_min))
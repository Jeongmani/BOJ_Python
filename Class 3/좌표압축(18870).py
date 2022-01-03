import heapq
import sys
rank=[]
ranking=0
n=int(sys.stdin.readline().rstrip())
N=list(map(int,sys.stdin.readline().split()))
N_set=set(N)
for i in N_set:
    heapq.heappush(rank,i)
while True:
    if len(rank)==0:
        break
    else:
        temp=heapq.heappop(rank)
    for i in range(n):
        if N[i]==temp:
            N[i]=ranking 
    ranking+=1
for i in N:
    print(i,end=' ')   
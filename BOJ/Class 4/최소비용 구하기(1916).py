import sys
import heapq
input=sys.stdin.readline
INF=int(1e9)                                        

n=int(input())                                      #노드의 개수n과 간선의 개수m을 입력받는다.
m=int(input())
graph=[[]for i in range(n+1)]                       #노듸의 개수만큼의 크기에 2차원 배열을 만든다.

for _ in range(m):
    node_1,node_2,cost=map(int,input().split())     #노드1에서 노드2까지의 드는 비용을 입력받고 그래프에 추가
    graph[node_1].append((node_2,cost))             
    
distance=[INF]*(n+1)                                #거리를 무한으로 초기화한다.

def dijkstra(start):                                #다익스트라 알고리즘을 이용해 최단거리를 구한다.
    q=[]                                            
    heapq.heappush(q,(0,start))                     
    distance[start]=0
    while q:
        dist,now=heapq.heappop(q)                   
        if distance[now] < dist:                    
            continue
        for i in graph[now]:                        
            cost=dist+i[1]                          
            if cost < distance[i[0]]:
                distance[i[0]]=cost                 
                heapq.heappush(q,(cost,i[0]))       
start,end=map(int,input().split())                  #start에서 end까지의 거리를 구한다.
dijkstra(start)
print(distance[end])


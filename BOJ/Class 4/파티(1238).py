import sys
import heapq
input=sys.stdin.readline
INF=int(1e9)                                        #다익스트라 알고림즘에서 거리를 무한으로 정의

n,m,start=map(int,input().split())                  #n명의 사람, m개의 노드, 파티가 열리는 사람의 집
graph=[[]for i in range(n+1)]                       #노드의 거리와 비용을 저장하는 그래프를 생성한다.

for _ in range(m):
    node_1,node_2,cost=map(int,input().split())     #노드1에서 노드2로가는 비용을 입력받고
    graph[node_1].append((node_2,cost))             #그래프에 노드1에 (노드2,비용)을 저장한다.
    

def dijkstra(start):                                #다익스트라 알고리즘
    q=[]                                            #우선순위 큐를 위한 리스트를 형성한다.
    distance=[INF]*(n+1)                            #거리를 모두 무한으로 초기화하고
    heapq.heappush(q,(0,start))                     #q에 시작하는 거리 0과 출발지를 저장한다.
    distance[start]=0
    while q:
        dist,now=heapq.heappop(q)                   #지금 우선순위 큐에 있는 비용과 지금 위치를 꺼낸다.
        if distance[now] < dist:                    #지금 방문한 노드에 거리가 최소라면 지나간다.
            continue
        for i in graph[now]:                        #현재 방문한 노드에 있는 정보를 순서대로 
            cost=dist+i[1]                          #비용은 방문 노드의 거리+ 저장된 노드까지의 거리
            if cost < distance[i[0]]:
                distance[i[0]]=cost                 #i[0]까지의 비용을 distance 리스트에 새로 등록한다.
                heapq.heappush(q,(cost,i[0]))       #우선순위 큐에 새로운 비용과 노드를 저장한다.
    return distance

result=0
for i in range(1,n+1):
    go = dijkstra(i)                                #i번째 노드에서 파티가 열리는 곳까지의 정보를 저장할 go
    back=dijkstra(start)                            #파티가 열린 곳에서 각자의 집까지의 최단경로
    result=max(result, go[start]+back[i])           #두개를 더한 값중 최대값을 result에 저장한다.
    
print(result)

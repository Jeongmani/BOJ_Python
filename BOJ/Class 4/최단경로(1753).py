import sys
import heapq
input=sys.stdin.readline
INF=int(1e9)                                        

n,m=map(int,input().split())                            #n개의 노드와 m개의 경로를 입력받는다.
start=int(input())                                      #출발지점으로 할 노드를 입력받는다.
graph=[[]for i in range(n+1)]                           #정보를 입력받을 그래프를 형성한다.

for _ in range(m):
    node_1,node_2,cost=map(int,input().split())         #그래프의 저장될 노드간 정보를 입력받는다.
    graph[node_1].append((node_2,cost))                 #노드1에서 노드2까지가는 비용
    
distance=[INF]*(n+1)                                    #각각 비용을 저장할 distance를 리스트를 형성한다.

def dijkstra(start):                                
    q=[]                                                #우선순위 큐를 만들고
    heapq.heappush(q,(0,start))                         #처음 드는 비용 0과 출발지점을 우선순위 큐에 넣고
    distance[start]=0                                   #자기 자신은 0으로 한다.
    while q:
        dist,now=heapq.heappop(q)                       #우선순위 큐에서 정보를 꺼내 거리와 현재 노드로 명명한다.
        if distance[now] < dist:                        #현재의 비용보다 이전에 방문한 정보가 더 작은 값이라면 무시한다.
            continue
        for i in graph[now]:                            #현재 방문한 노드에서 그래프에 저장된 인접노드들을 방문한다.
            cost=dist+i[1]                              #비용은 현재 방문한 노드에 저장된 거리+비용이다.
            if cost < distance[i[0]]:
                distance[i[0]]=cost                     #새로 얻게된 cost가 저장되어있는 값보다 작다면 최신화 한다.
                heapq.heappush(q,(cost,i[0]))           #우선순위 큐에 인접노드 정보를 넣는다.

dijkstra(start)

for i in distance[1:]:
    if i==1000000000:                                   #방문 할 수 없는 노드는 INF 값을 출력한다.
        print("INF")
    else:
        print(i)

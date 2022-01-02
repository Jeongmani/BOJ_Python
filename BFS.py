#큐와 while문을 이용하여 BFS구현
from collections import deque

def BFS(graph,start,visited):
    queue=deque([start])
    visited[start]=True
    while queue:
        v=queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
                
'''graph=[      #각 노드가 연결된 정보를 리스트 자료형으로 표현 (2차원 리스트)
    [],
    [*,*,*]
    '
    '
    '
]'''

visited=[False]*n
BFS(graph,start,visited)
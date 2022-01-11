#스택과 재귀함수를 이용한 DFS구현
def DFS(graph,v,visited):
    visited[v]=True
    print(v,end=' ')
    for i in graph[v]:
        if not visited[i]:
            DFS(graph,i,visited)

'''graph=[      #각 노드가 연결된 정보를 리스트 자료형으로 표현 (2차원 리스트)
    [],
    [*,*,*]
    '
    '
    '
]'''

visited=[False]*n

DFS(graph,start,visited)
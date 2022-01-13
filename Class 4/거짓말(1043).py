import sys
input=sys.stdin.readline
from collections import deque                                   #덱 함수를 이용해 큐를 구현하기 위해서 deque함수를 import

N,M=map(int,input().split())
first_known=list(map(int,input().split()))[1:]                  #처음부터 알고 있던 사람을 리스트에 추가 [1:] => 입력 받는 값에서 1번째 인덱스 부터 저장
graph=[list(map(int,input().split()))[1:] for _ in range(M)]    #파티별 참가자를 저장하기 위해서 [1:]을 이용해서 파티에 참가한 참가자를 저장
                
people=[False]*(N+1)                                            #N번째 사람까지 저장하기 위해서 N까지의 인덱스를 가진 리스트를 False값으로 초기화
party=[False]*M                                                 #말을 해도 괜찮은 파티를 구별하기 위해 최소에 False값으로 초기화

for i in first_known:                                           
    queue=deque()                                           
    queue.append(i)                                             #처음 부터 알고있던 사람을 queue에 넣고
    people[i]=True                                              #이 사람은 알고있는 사람임으롤 i번째 인덱스를 True로 변경

    while queue:                                                #queue가 빌때까지 진행한다.
        value=queue.popleft()                                   #큐에서 원소를 하나 꺼낸다, 진실을 알고 있는 사람이다.
        for j in range(len(graph)):                             #j는 파티에 참가하는 참가자들의 리스트 이다.
            if value in graph[j]:                               #j파티에 진실을 알고 있는 사람이 있다면
                for k in graph[j]:                              #j파티에 참가한 k가 
                    if not people[k]:                           #people False값이라면 
                        queue.append(k)                         #k를 queue에 추가하고
                        people[k]=True                          #진실을 아는 사람임으로 True값으로 변경해준다.
                    party[j]=True                               #j파티는 거짓말을 할 수 없으므로 True값으로 변경해준다.

print(party.count(False))                                       #False값에서만 거짓말을 할 수 있으므로 False값의 개수를 출력한다.
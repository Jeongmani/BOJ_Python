import heapq                                                            #heapq 우선순위 큐를 이용해서 이 문제를 해결할 것이다.
import sys

T=int(sys.stdin.readline().rstrip())
for _ in range(T):
    array_min=[]                                                        #최소 힙을 구현하기 위한 리스트를 선언했다.
    array_max=[]                                                        #최대 힙을 구현하기 위한 리스트를 선언했다.
    visited=[False]*1_000_001                                           #최대 1,000,000까지의 수가 있으므로 
    k=int(sys.stdin.readline().rstrip())
    for key in range(k):
        command=sys.stdin.readline().split()                            
        if command[0]=='I':                                             # I가 들어온 경우 최대힙과 최소힙에 수를 넣어준다
            heapq.heappush(array_min,(int(command[1]),key))             # 최소 힙과 최대 힙이 따로 구현되어 있기 때문에 식별자 값으로 Key를 부여했다.
            heapq.heappush(array_max,(-int(command[1]),key))
            visited[key]=True                                           #visited[key]값을 True로 변경한다.
        else:
            if command[1]=='-1':                                        #D에 -1이 입력된 경우는 최소 힙에서 
                while array_min and not visited[array_min[0][1]]:       #visited에 false값을 다 빼준다.
                    heapq.heappop(array_min)
                if array_min:
                    visited[array_min[0][1]]=False                      #최소의 수를 꺼내기 전에 최대 힙과 동기화하기 위해서 visited를 false값을 변경하고
                    heapq.heappop(array_min)                            #heappop을 진행한다.
                
            elif command[1]=='1':                                       #D에 1이 입력된 경우에는 최대 힙에서
                while array_max and not visited[array_max[0][1]]:       #visiteddp flase값을 다 빼주고
                    heapq.heappop(array_max)            
                if array_max:
                    visited[array_max[0][1]]=False                      #원하는 최대 수를 visited에서 false로 바꾸어 최소힙과 동기화를 해주고
                    heapq.heappop(array_max)                            #heappop을 진행한다.
    
    while array_min and not visited[array_min[0][1]]:                   #남아 있는 false값을 다 삭제하고
        heapq.heappop(array_min)    
    while array_max and not visited[array_max[0][1]]:
        heapq.heappop(array_max)
    if array_min and array_max:                                         #최대 힙과 최소 힙에 아직 수가 남아 있다면
        print(-array_max[0][0],array_min[0][0])                         #최대값과 최소값을 출력해주고
    else:
        print('EMPTY')                                                  #비어있다면 EMPTY를 출력하며 프로그램을 종료한다.
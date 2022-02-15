import heapq            #절대값 힙을 구하기 위해서 heapq라이브러리를 사용(절댓값 힙을 하기 위해서 최대힙과 최소힙을 적절히 사용)
import sys

N=int(sys.stdin.readline().rstrip())        #N값을 입력받아서
array_plus=[]                               #양수값을 저장할 array_plus를 리스트로 선언
array_minus=[]                              #음수값을 저장할 array_minus를 리스트로 선언
for i in range(N):                          #N번 input을 받으며
    a=int(sys.stdin.readline().rstrip())
    if a==0:                                #0을 입력받으면 절댓값이 작은 수를 출력하고 절댓값이 같으면 작은 수를 출력 , 리스트에 값이 없다면 0을 출력한다
        if len(array_plus)+len(array_minus)==0:     #두 array에 모두 수가 없다면 0을 출력
            print('0')
        else:
            if  len(array_plus)!=0 and len(array_minus)!=0:     #두 array모두에 수가 있을때
                if array_plus[0]>=array_minus[0]:               # array_plus의 최소 절댓값보다 array_minus의 최소 절댓값이 작거나 같다면
                    print(-heapq.heappop(array_minus))
                else:
                    print(heapq.heappop(array_plus))            # array_plus의 최소 절댓값이 더 작다면
            elif len(array_plus)==0:                            # array_plus가 비어있을때
                print(-heapq.heappop(array_minus))
            elif len(array_minus)==0:                           # array_minus가 비어있을때        
                print(heapq.heappop(array_plus))        
    elif a>0:
        heapq.heappush(array_plus,a)             #0이 아닌 양수를 입력받으면 array_plus 리스트에 추가한다.
    elif a<0:
        heapq.heappush(array_minus,-a)           #0이 아닌 음수를 입력받으면 array_minus 리스트에 추가한다
import heapq            #최대힙을 구하기 위해서 heapq라이브러리를 사용(최소힙을 구하는 방식과 같지만 부호를 임시적으로 변경해주는 방법을 사용)
import sys

N=int(sys.stdin.readline().rstrip())        #N값을 입력받아서
array=[]
for i in range(N):                          #N번 input을 받으며
    a=int(sys.stdin.readline().rstrip())
    if a==0:                                #0을 입력받으면 최대값을 출력하고 리스트에 값이 없다면 0을 출력한다
        if len(array)==0:
            print('0')
        else:
            print(-heapq.heappop(array))
    else:
        heapq.heappush(array,-a)             #0이 아닌 자연수를 입력받으면 리스트에 추가한다.
import sys
from collections import deque           #큐를 구현하기 위해서 deque를 사용하기 (큐는 선입선출 구조)
N=int(sys.stdin.readline().rstrip())    #N개의 명령
queue=deque()                           #queue를 deque함수의 형태로 선언
for _ in range(N):
    command=list(map(str,sys.stdin.readline().split()))         #명령을 리스트 형태로 저장     
    if command[0]=='push':              #명령이 'push x'인 경우에는 'x'를 큐에 넣는다
        queue.append(int(command[1]))
    if command[0]=='pop':               #명령이 'pop'인 경우에는 큐의 왼쪽 끝부분에서 한개의 인덱스를 출력하고 큐가 비어있다면 -1을 출력한다.
        if len(queue)==0:
            print(-1)
        else:
            a=queue.popleft()
            print(a)
    if command[0]=='size':              #명령이 'size'인 경우에는 큐의 길이를 출력한다.
        print(len(queue))
    if command[0]=='empty':             #명령이 'empty'인 경우에는 큐가 비어있다면 1(True)값을 출력하고 아니라면 0(False)값을 출력한다.
        if len(queue)==0:
            print(1)
        else:
            print(0)
    if command[0]=='front':             #명령이 'front'인 경우에는 큐의 가장 왼쪽에 있는 인덱스를 알려준다. 큐가 비어있다면 -1을 출력한다.
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])
    if command[0]=='back':              #명령이 'back'인 경우 큐의 가장 오른쪽에 있는 인덱스를 알려준다. 큐가 비어있다면 -1을 출력한다.
        if len(queue)==0:
            print(-1)
        else:
            print(queue[-1])

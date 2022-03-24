from collections import deque
def solution(priorities, location):
    queue=deque([i for i in range(len(priorities))])
    answer=[]
    while True:
        tmp=queue.popleft()
        if len(queue)==0:
            answer.append(tmp)
            break
        if max(priorities)==priorities[tmp]:
            answer.append(tmp)
            priorities[tmp]=0
        else:
            queue.append(tmp)
    for i in range(len(answer)):
        if answer[i]==location:
            return (i+1)
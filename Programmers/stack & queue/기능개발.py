from collections import deque
def solution(progresses, speeds):
    pro=deque(progresses)
    spd=deque(speeds)
    answer = []
    while (pro):
        return_num=0
        for i in range(len(spd)):
            pro[i]+=spd[i]
        while True:
            if len(pro)==0:
                break
            if pro[0] >= 100:
                pro.popleft()
                spd.popleft()
                return_num+=1
            else:
                break
        if return_num !=0:
            answer.append(return_num)
    return answer
def solution(n, lost, reserve):
    student=[1 for i in range(n)]
    for lost_st in lost:
        student[lost_st-1]-=1
    for reserve_st in reserve:
        student[reserve_st-1]+=1
    lost_now=[]
    reserve_now=[]
    for i in range(len(student)):
        if student[i]==0:
            lost_now.append(i)
        elif student[i]==2:
            reserve_now.append(i)
    answer=n-len(lost_now)
    for j in lost_now:
        if j-1 in reserve_now:
            answer+=1
            reserve_now.remove(j-1)
        elif j+1 in reserve_now:
            answer+=1
            reserve_now.remove(j+1)
    return answer

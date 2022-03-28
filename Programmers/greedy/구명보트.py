from collections import deque
def solution(people, limit):
    people.sort()
    list_people=deque(people)
    answer=0
    while True:
        if len(list_people)==1:
            answer+=1
            break
        if len(list_people)==0:
            break
        else:
            on_boat=list_people.pop()
            if on_boat+list_people[0]<=limit:
                list_people.popleft()
            answer+=1
    return answer

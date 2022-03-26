from collections import deque
def solution(bridge_length, weight, truck_weights):
    queue=deque([0 for _ in range(bridge_length)])
    truck_weight=deque(truck_weights)
    answer=0
    while (truck_weight):
        time=0
        queue.popleft()
        if sum(queue)+truck_weight[0] <= weight:
            truck=truck_weight.popleft()
            queue.append(truck)
        else:
            for i in queue:
                if i !=0:
                    break
                else:
                    time+=1
            for _ in range(time):
                queue.popleft()
            answer+=time
            for _ in range(time+1):
                queue.append(0)
        answer+=1
    
    answer+=bridge_length
    return answer
   
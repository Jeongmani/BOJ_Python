import heapq
def solution(operations):
    heap = []
    for commands in operations:
        command=commands.split()
        if command[0]=="I":
            heapq.heappush(heap,int(command[1]))
        if command[0]=="D":
            if command[1] == "1":
                if len(heap)==0:
                    pass
                else:
                    max_num=max(heap)
                    heap.remove(max_num)
                    heapq.heapify(heap)
            if command[1] == "-1":
                if len(heap)==0:
                    pass
                else:
                    heapq.heappop(heap)
    answer=[0,0]
    if len(heap)==0:
        return answer
    else:
        min_num=min(heap)
        max_num=max(heap)
        answer=[max_num,min_num]
        return answer
        
    return answer
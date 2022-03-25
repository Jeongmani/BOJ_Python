import heapq

def solution(array, commands):
    answer = []
    test_case=len(commands)
    for test in range(test_case):
        processed=[]
        for process in range(commands[test][0]-1,commands[test][1]):
            processed.append(array[process])
        heapq.heapify(processed)
        processed_sort=[]
        while (processed):
            processed_sort.append(heapq.heappop(processed))
        answer.append(processed_sort[commands[test][2]-1])
    return answer
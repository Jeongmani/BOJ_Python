import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    time=0
    while True:
        first=heapq.heappop(scoville)
        if first>=K:
            return time
            break
        else:
            if len(scoville)==0:
                return -1
                break
        second=heapq.heappop(scoville)
        new=first+(second*2)
        heapq.heappush(scoville,new)
        time+=1
import heapq
def solution(jobs):
    sum_time=0
    now=0
    wait_list=[]
    len_jobs=len(jobs)
    jobs_check=[False for _ in range(len_jobs)]
    while True:
        for i in range(len_jobs):
            if jobs[i][0]<=now:
                if jobs_check[i]==False:
                    heapq.heappush(wait_list,(jobs[i][1],jobs[i][0]))
                    jobs_check[i]=True
        if len(wait_list)==0:
            if False not in jobs_check:
                return sum_time//len_jobs
                break
            else:
                now+=1
        else:
            time_spend=heapq.heappop(wait_list)
            request_time=time_spend[1]
            now+=time_spend[0]
            wait_time=now-request_time
            sum_time+=wait_time
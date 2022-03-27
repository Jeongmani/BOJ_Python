def solution(citations):
    citations.sort(reverse=True)
    for time, cit in enumerate(citations):
        if time >= cit:
            return time
    return len(citations)
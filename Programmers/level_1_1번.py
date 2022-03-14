def solution(d, budget):
    d.sort()
    while sum(d) > budget:
        d.pop()       
    answer = len(d)
    return answer

print(solution([1, 3, 2, 5, 4], 9))
print(solution( [2, 2, 3, 3], 10))
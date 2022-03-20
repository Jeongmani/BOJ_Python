def solution(numbers):
    result_arr=[]
    for i in range(10):
        if i not in numbers:
            result_arr.append(i)    
    answer = sum(result_arr)
    return answer
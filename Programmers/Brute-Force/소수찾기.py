from itertools import permutations
def solution(numbers):
    len_numbers=len(numbers)
    prime_list=[]
    for i in range(len_numbers):
        possible=list(permutations(numbers,(i+1)))
        for j in possible:
            prime_list.append(int(''.join(j)))
    
    prime_check=list(set(prime_list))
    answer=0
    for i in prime_check:
        if i==0:
            continue
        if i==1:
            continue
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                break
        else:
            answer+=1
    return answer
    
    

def solution(participant, completion):
    hash_data={}
    hash_sum=0
    
    for i in participant:
        hash_data[hash(i)]=i
        hash_sum+=hash(i)
        
    for i in completion:
        hash_sum-=hash(i)
        
    return hash_data[hash_sum]
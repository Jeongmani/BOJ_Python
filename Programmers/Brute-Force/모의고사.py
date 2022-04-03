def solution(answers):
    problem=len(answers)
    a=(problem//5)+1
    b=(problem//8)+1
    c=(problem//10)+1
    person_a=[1,2,3,4,5]*a
    person_b=[2,1,2,3,2,4,2,5]*b
    person_c=[3,3,1,1,2,2,4,4,5,5]*c
    count_a=0
    count_b=0
    count_c=0
    for i in range(problem):
        if person_a[i]==answers[i]:
            count_a+=1
        if person_b[i]==answers[i]:
            count_b+=1
        if person_c[i]==answers[i]:
            count_c+=1
    count=max(count_a,count_b,count_c)
    answer=[]
    if count_a==count:
        answer.append(1)
    if count_b==count:
        answer.append(2)
    if count_c==count:
        answer.append(3)
    
    return answer
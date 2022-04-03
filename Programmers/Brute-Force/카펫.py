def solution(brown, yellow):
    total=brown+yellow
    possible=[]
    for i in range(3,total):
        if total%i==0:
            possible.append((i,total//i))
    for row,col in possible:
        if (row-2)*(col-2)==yellow:
            return [col,row]
            
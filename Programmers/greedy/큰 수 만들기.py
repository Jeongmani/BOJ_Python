def solution(number, k):
    make_num=[]
    for i in number:
        while k>0 and make_num and make_num[-1]<i:
            make_num.pop()
            k-=1
        make_num.append(i)
    answer=''.join(make_num[:len(number)-k])
    return answer
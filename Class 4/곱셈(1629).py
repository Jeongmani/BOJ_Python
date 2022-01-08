import sys
input=sys.stdin.readline
A,B,C=map(int,input().split())                      #A,B,C를 입력받는다.
def squared(A,B):                                   #분할정복을 이용해 거듭제곱을 표현할 것이다.
    if B==1:    
        return A%C                                  #B가 1이라면 A를 C로 나눈값을 리턴한다.
    else:
        new_squared=squared(A,B//2)                 #그렇지 않다면 B를 2로 나누고 new_Squared함수를 실행한다.
        if B%2==0:
            return (new_squared*new_squared)%C      #이는 짝수인 경우 ex) 2**6은 (2**3)*(2**3)으로 표현 할 수 있음을 이용한다.
        else:
            return (new_squared*new_squared*A)%C    #이는 홀수인 경우 ex) 2**5는 (2**2)*(2**2)*2로 표현 할 수 있음을 이용한다.

print(squared(A,B))                                 
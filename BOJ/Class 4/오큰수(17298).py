import sys
input=sys.stdin.readline

N=int(input())
num_list=list(map(int,input().split()))                     #숫자의 배열을 리스트로 입력받는다.
NGE=[-1]*N                                                  #오큰수가 없는 경우는 -1로 출력함으로 -1로 배열의 크기만큼 초기화 해둔다.
stack=[]                                                    #인덱스를 저장할 스택을 만든다.
for i in range(N):
    while stack and num_list[stack[-1]] < num_list[i]:      #스택이 비어있지 않거나 스택의 가장 윗번째 수가 i번째 수보다 작다면 지금까지 스택에 있던 수들의 오큰수는 i번째 수이다.
        NGE[stack.pop()]=num_list[i]                        #스택에 있는 수들의 오큰수는 모두 i번째 수가 된다.
    stack.append(i)                                         #while문에 조건에 충족하지 않는다면 인덱스를 stack에 추가한다.
print(*NGE)                                                 #NGE를 출력한다. (*list_name)을 출력하면 리스트안에 있는 것들이 공백으로 구분되어 출력된다.

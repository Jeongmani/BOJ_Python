import sys
N=int(sys.stdin.readline().rstrip())
stack=[]            #스택을 구현하기 위해서 리스트를 이용했습니다. (스택은 선입후출 구조)
for _ in range(N):
    command=list(map(str,sys.stdin.readline().split()))  # 문제에서 5개의 명령을 입력받아서 리스트에 저장
    if command[0]=='push':              #명령이 'push'일 경우 'push x' 형태로 입력이 됨. 이때 x를 스택에 추가해준다.
        stack.append(int(command[1]))
    if command[0]=='pop':               #명령이 'pop'일 경우 스택에 top에서 빠지고 그 수를 출력, 스택에 아무것도 없을 경우에는 -1을 출력
        if len(stack)==0:
            print(-1)
        else:
            a=stack.pop()
            print(a)
    if command[0]=='size':              #명령이 'size'인 경우 스택의 사이즈를 출력함
        print(len(stack))
    if command[0]=='empty':             #명령이 'empty'인 경우 스택이 비어있다면 1(True)를 출력하고 아니라면 0(False)을 출력한다.
        if len(stack)==0:
            print(1)
        else:
            print(0)
    if command[0]=='top':               #명령이 'top'인 경우 스택의 top부분에 있는 정수를 출력하고 스택이 비어있다면 -1을 출력한다.
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])

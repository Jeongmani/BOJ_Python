def solution(s):
    stack=[]
    for i in s:
        if len(stack)==0:
            stack.append(i)
        else:
            if i==')':
                if stack[-1] == '(':
                    stack.pop()
            else:
                stack.append(i)
    if len(stack)==0:
        check=True
    else:
        check=False
    return check
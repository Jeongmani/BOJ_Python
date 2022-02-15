import sys
input=sys.stdin.readline
String=input().rstrip()                     #문자열을 입력받고
Key=input().rstrip()                        #폭발 문자열을 입력받는다.
Bomd=[]                                     #폭발 문자열이 들어오는지 확인하기 위해 스택 자료구조를 이용할 것이다.

for i in String:
    Bomd.append(i)                          #입력 받은 문자열을 스택에 넣는다.
    a=1                                     #밑에서 a==1인 경우만 pop을 진행하기 위해 임시 변수 선언
    if i == Key[-1]:
        if len(Bomd) < len(Key):            #스택의 길이보다 Key의 길이가 길면 폭발이 절대 진행되지 않기 때문에 continue함수로 다음 루프를 진행한다. 
            continue
        else:
            for j in range(len(Key)):
                if Bomd[-(j+1)]!=Key[-(j+1)]:   #스택의 끝과 Key의 끝이 같다면 스택의 끝부분에서 안쪽으로 들어가면서 Key와 같은 값인지 확인한다.
                    a=0                         #다르다면 a=0으로 바꾸며 아래서 pop이 진행되지 않도록 한다.
            if a==1:
                for _ in range(len(Key)):       #a=1이라면 스택의 끝부분이 Key와 동일하다는 의미임으로 pop을 Key의 길이 만큼 진행한다.
                    Bomd.pop()
                        
if len(Bomd)==0:                            #스택의 길이가 0dlfkaus FRULA를 출력한다.
    print('FRULA')
else:
    for i in Bomd:                          #스택에 남은 문자열이 있다면 순서대로 출력한다.
        print(i,end='')

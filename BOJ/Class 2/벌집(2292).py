n=int(input())                      #정수 N을 입력받는다

def room(x):                        #입력받은 정수N이 벌집에서 몇번째 층인지 구하는 함수를 구현한다.
    floor=1                         #층을 의미한다.
    multiply=6                      #6각형 벌집에서는 층*6의 개수만큼의 집을 만들 수 있다
    start=1                         #start는 strat층에서 처음 시작되는 방을 의미한다.
    while True:
        if n<=start:                #n이 start보다 작다면 그 바로 아래 층수인 floor를 출력하며 함수를 끝낸다.
            print(floor)
            break
        elif n>start:               #n이 start보다 크다면 start를 다음층으로 올리고 floor를 한층 증가시킨다.
            start+=floor*multiply
            floor+=1          

room(n)                             #room함수에 n을 넣어 시작한다.  
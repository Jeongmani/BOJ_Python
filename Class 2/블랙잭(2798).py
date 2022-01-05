N,M=map(int,input().split())                           #N,M을 입력받는다.
card=list(map(int,input().split()))                    #카드의 숫자들을 리스트 자료형으로 저장한다
sum_max=0                                              #M에 가장 가까우면서 M을 넘지 않을 수를 저장할 변수를 선언한다
for i in range(N):                                     #첫 카드를 선택 
    for j in range(i+1,N):                             #첫 카드 이후 i+1번째부터 끝까지 중 두번째 카드 선택
        for k in range(j+1,N):                         #두번째 카드 이후 j+1번째부터 끝까지 중 세번째 카드를 선택
            if (card[i]+card[j]+card[k]) <= M:         #카드의 수 합이 M보다 작거나 같은경우
                if sum_max< (card[i]+card[j]+card[k]): #sum_max보다 크다면
                    sum_max=(card[i]+card[j]+card[k])  #새로운 sum_max를 선언한다
print(sum_max)
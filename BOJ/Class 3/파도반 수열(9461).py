import sys
sequence=[0,1,1]                    #수열에서 초기 삼각형 변 길이인 1인 경우를 미리 리스트로 선언해둠 
for i in range(3,101):              #문제에서 주어진 입력값을 100까지 입력됨으로 100까지의 결괴를 리스트에 저장
    sequence.append(sequence[i-3]+sequence[i-2]) #수열의 점화식을 이용한 계산
T=int(sys.stdin.readline())
for _ in range(T):                  #테스트 케이스를 입력
    print(sequence[int(sys.stdin.readline())])   #테스트 케이스만큼 N번째 삼각형의 변의 길이를 출력한다

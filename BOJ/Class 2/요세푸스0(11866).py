import sys
N,K=map(int,sys.stdin.readline().split())           #N,K를 입력받아 공백으로 구분
number=[i+1 for i in range(N)]          #1~N까지의 숫자를 저장할 리스트(컴프리헨션 사용) 
check_list=[0]*(N+1)                    #check_list는 그 수를 방문했는지 확인하기 위해 만들고 편의를 위해 0번째는 이미 방문한 것으로 처리함                    
check_list[0]=1                         
result=[]                               #요세푸스 순열 순서대로 방문한 수를 저장하기 위한 리스트를 형성
pointer=0                               #pointer는 number리스트에 몇번째 숫자를 지나고 있는지 표시하면서 이동
i=0                                     #i는 이미 방문한 숫자라면 증가하지 않고 방문하지 않은경우 K의 배수가 됨을 확인하기 위해서 선언
while True:
    if pointer>=N:                      #pointer가 N을 초과한다면 pointer에서 N을 빼줌
        pointer=pointer-N
    else:
        pointer+=1                      #그것이 아니라면 pointer는 1씩 증가하며
    if check_list[pointer]==0:
        i+=1                            #방문하지 않은 곳에서는 i가 1씩 증가하고
        if i%K==0:                      #i가 K의 배수가 되었을때 pointer위치에 있는 수를 방문처리
            check_list[pointer]=1
            result.append(pointer)
    else:
        pass                            #i가 K의 배수가 아니라면 그냥 지나가고
    if 0 not in check_list:             #check_list에 방문하지 않은 리스트가 없다면 while문을 종료한다.
        break

print("<",end='')                       #문제 조건에 맞는 출력을 하기 위한 코드입니다.
for i in range(len(result)-1):
    print("%d, "%result[i], end='')
print(result[-1], end='')
print(">")

import sys                  #이 문제는 수를 정렬하는 문제이지만 메모리 제한이 8MB로 작은 편입니다.            
n = int(sys.stdin.readline().rstrip())
num_list = [0] * 10001      #문제에서 10000보다 작거나 같은 자연수만 주어진다고 했으므로 나오는 수를 저장할 리스트를 0으로 초기화

for _ in range(n):          #N개의 정수를 받아 리스트의 위치에 해당하는 수를 1증가 시킨다.
    temp = int(sys.stdin.readline().rstrip())
    num_list[temp]+=1

for i in range(10001):      #리스트에 i번째 요소가 0이 아니라면 그 수를 i를 i번째 요소만큼 출력한다.
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)

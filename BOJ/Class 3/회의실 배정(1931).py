import sys
input=sys.stdin.readline
N = int(input())
time = [[0]*2 for _ in range(N)]                #회의의 시작시간과 끝나는 시간을 저장할 리스트를 선언한다.
for i in range(N):
    start,end = map(int, input().split())       #회의의 시작시간과 끝나는 시간을 입력받아 i번째 인덱스로 지정한다.
    time[i][0] = start
    time[i][1] = end
time.sort(key = lambda x: (x[1], x[0]))         #회의를 빨리 끝나는 순서대로 정렬하고, 후에 시작시간 순서로 정렬한다. (이는 회의가 빨리 끝나면 뒤에 가능성있는 회의가 많기 때문)
count = 1
end_time = time[0][1]                           #끝나는 시간을 가장 첫번째 인덱스의 끝나는 시간으로 설정하고
for i in range(1, N):
    if time[i][0] >= end_time:                  #i번째 인덱스의 시작시간이 끝나는 시간보다 크다면 회의를 진행 할 수 있음으로 
        count+= 1                               #count를 1증가시키고
        end_time = time[i][1]                   #새로운 end_time으로 지정해준다.
print(count)
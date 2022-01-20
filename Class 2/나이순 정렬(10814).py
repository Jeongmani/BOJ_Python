N=int(input())
data=[]
for _ in range(N):
    A,B=input().split()
    data.append([int(A),B])                 #입력한 순서대로 저장이 되어있는 상태에서는 나이순으로만 정렬해 주면됨

data.sort(key=lambda x:(int(x[0])))         #lambda 함수를 이용해서 나이순으로 정렬
for i in range(N):
    print(data[i][0],data[i][1])
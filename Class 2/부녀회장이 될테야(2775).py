import sys
input=sys.stdin.readline

apt=[[0 for _ in range(15)]for _ in range(15)]          #14층 까지의 정보를 미리 저장할 2차원 리스트를 선언한다.
apt[0]=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]               #0층에 사는 사람들의 수
for i in range(1,15):                                   #i번째층
    for j in range(14):                                 #j번째호
        for k in range(j+1):                            #는 i-1층에 1~j호까지의 사람을 데려와야한다.
            apt[i][j]+=apt[i-1][k]

testcase=int(input())
for _ in range(testcase):
    floor=int(input())
    room=int(input())
    print(apt[floor][room-1])
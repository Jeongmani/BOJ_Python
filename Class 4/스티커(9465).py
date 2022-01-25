import sys
input=sys.stdin.readline

Testcase=int(input())
for _ in range(Testcase):
    len_sticker=int(input())                                    #2*N 즉 스트커의 길이 N을 len_sticker로 입력받는다.
    sticker=[]                                                  #스티커의 정보를 입력받을 리스트를 선언한다.
    for _ in range(2):
        sticker.append(list(map(int,input().split())))
    if len_sticker==1:
        print(max(sticker[0][0],sticker[1][0]))                 #스티커의 길이가 1인 경우에는 둘 중에 큰 수를 선택한다.
    else:
        dp=[[0 for _ in range(len_sticker)]for _ in range(2)]   #dp를 진행하기 위한 dp리스트를 선언한다.
        dp[0][0]=sticker[0][0]                                  #0번째 줄의 스티커가 선택될때 최대값은 자기 자신
        dp[1][0]=sticker[1][0]
        dp[0][1]=sticker[1][0]+sticker[0][1]                    #1번째 줄의 스티커가 선택될때 최대값은 자기 자신과 대각선에 0번째줄의 스티커
        dp[1][1]=sticker[0][0]+sticker[1][1]
        for i in range(2,len_sticker):
            dp[0][i]=max(dp[1][i-2],dp[1][i-1])+sticker[0][i]   #2번째 줄부터는 자신의 대각선 아래가 선택되거나 i-2번째의 대각선이 선택되는 경우 중 최대값을 선택하고 본인을 더한 값
            dp[1][i]=max(dp[0][i-2],dp[0][i-1])+sticker[1][i]
        print(max(dp[0][len_sticker-1],dp[1][len_sticker-1]))   #마지막 줄에서 위, 아래 중에서 최대값을 출력한다.

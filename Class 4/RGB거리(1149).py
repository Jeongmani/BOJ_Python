import sys
input=sys.stdin.readline


N=int(input())
RGB=[]                                              #DP를 사용할 예정
for i in range(N):
    RGB.append(list(map(int,input().split())))      #RGB리스트에 각각 집 색 비용을 저장한다.
for i in range(1,N):
    RGB[i][0]+=min(RGB[i-1][1],RGB[i-1][2])         #빨간집을 선택한경우 그 전 집에서는 초록집 파랑집중 가격이 저렴한것으로 선택
    RGB[i][1]+=min(RGB[i-1][0],RGB[i-1][2])         #초록집을 선택한경우 그 전 집에서는 빨간집 파랑집중 가격이 저렴한것으로 선택
    RGB[i][2]+=min(RGB[i-1][0],RGB[i-1][1])         #파랑집을 선택한경우 그 전 집에서는 빨간집 초록집중 가격이 저렴한것으로 선택

print(min(RGB[N-1]))

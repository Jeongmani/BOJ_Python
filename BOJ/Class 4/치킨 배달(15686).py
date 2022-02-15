import sys      
import itertools                                        #조합을 계산하기 위해서 itertools를 import
input=sys.stdin.readline

size,store=map(int,input().split())                     #map의 크기 size, 남길 치킨 집 store을 공백으로 구분하여 받는다.
chicken=[[] for _ in range(size)]                       #map을 저장할 2차원 리스트를 컴프리헨션을 이용해 초기화한다.
chicken_store=[]                                        #map에 2가 들어온 경우 치킨집의 위치를 저장하기 위한 리스트
combination=[]                                          #치킨집의 위치를 store개수 만큼 조합으로 뽑는 경우
customer=[]                                             #map에 1이 들어온 경우 손님의 위치를 저장하기 위한 리스트

for i in range(size):
    chicken[i]=list(map(int,input().split()))           #map을 입력받는다.
    for j in range(size):
        if chicken[i][j]==2:                            #2가 입력되면 치킨집 리스트에 위치를 추가한다.
            chicken_store.append((i,j)) 
        if chicken[i][j]==1:                            #1이 입력되면 손님의 리스테 위치를 추가한다.
            customer.append((i,j))



for i in itertools.combinations(chicken_store,store):   #조합함수를 사용해 치킨집을 store개 만큼 뽑는 조합을 저장한다. 
    combination.append(i)

distance_delivery=[]                                    #조합별로 거리를 저장할 리스트를 선언한다.

for i in range(len(combination)):
    total=0                                             #최소 거리를 저장할 변수를 선언한다.
    for j in range(len(customer)):
        distance=987654321                              #거리를 무제한으로 늘리고 이는 아래에서 최초에 min함수에서 선택되는것을 피하기 위해서이다.
        for k in range(store):   
            temp=abs(combination[i][k][0]-customer[j][0])+abs(combination[i][k][1]-customer[j][1])      #거리공식을 이용해 거리를 구하고
            distance=min(distance,temp)                 #조합에서 뽑힌 치킨집중 최소 거리인 것을 distance로 선언한다.
        total+=distance                                 #최소 거리들의 합을 구한다.
    distance_delivery.append(total)                     #최소 거리들의 합을 distance_delivery에 추가한다.
print(min(distance_delivery))                           #distance_delivery중 가장 최소값을 출력한다.

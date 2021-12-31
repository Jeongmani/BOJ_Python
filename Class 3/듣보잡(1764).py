import sys
N,M=map(int,sys.stdin.readline().split())
never_hear=set([])                      #듣도 못한 사람을 저장하는 집합을 선언한다
never_seen=set([])                      #보도 못한 사람을 저장하는 집합을 선업한다
for i in range(N):
    hear=sys.stdin.readline().rstrip()  #듣도 못한 사람을 집합에 추가한다
    never_hear.add(hear)
for j in range(M):
    seen=sys.stdin.readline().rstrip()  #보도 못한 사람을 집합에 추가한다
    never_seen.add(seen)
never_hear_seen=list(never_hear & never_seen)   #듣도 보도 못한 사람을 교집합을 이용하여 리스트의 형태로 저장한다 
never_hear_seen.sort()                          #처음에 리스트로 저장하여 교집합되는 부분을 찾는 방식을 이용했더니 시간초과가 나왔습니다.
print(len(never_hear_seen))
for h in never_hear_seen:
    print(h)

import sys                                                  #이중 for 문을 사용할 경우 N이 10000이고 M도 10000이기 때문에 너무 많이 시간이 걸려 풀 수 없다.

N,M=map(int,sys.stdin.readline().split())

data=dict()                                                 #딕셔너리 자료형을 이용하여 key값이 입력되면 value값을 출력하는 형태로 구현할 것이다
for _ in range(N):
    adress,password=map(str,sys.stdin.readline().split())
    data[adress]=password                                   #adress가 key값으로 주어지고 value값은 password가 되도록 한다.
for _ in range(M):
    quest=sys.stdin.readline().rstrip()                     #key값이 주어졌을때 value값을 출력한다.
    print(data[quest])

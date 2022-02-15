import sys
def gcd(a,b):                           #시간을 최대한 줄이기 위해서 최소공배수를 구하기 위해 유클리드 호제법을 사용한 함수 구현
    a,b=max(a,b),min(a,b)
    while b:
        a,b=b,a%b
    return a
T=int(sys.stdin.readline().rstrip())
for _ in range(T):
    M,N,x,y=map(int,sys.stdin.readline().split())
    end_number=((M*N)//gcd(M,N))       #종말의 날은 M과 N의 최소공배수 임을 이용한다. 
    check=False                        #while 문을 빠져나와도 check값이 변하는지 안변하는지에 따라서 True값고 False값을 부여
    while x<=end_number:
        if x%N == y%N:                 #x의 값을 고정으로 생각했을때 x(는 while문을 돌아갈때마다 M씩 증가)를 n으로 나눈 나머지와 y를 N으로 나눈 나머지가 같다면 
            print(x)
            check=True                 #찾고자하는 값임을 확인 할 수 있다.
            break
        x+=M
    if check==False:
        print(-1)

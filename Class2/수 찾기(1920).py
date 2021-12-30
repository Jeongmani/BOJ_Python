import sys 
N=int(sys.stdin.readline().rstrip())                        #N개의 정수의 개수를 입력받고
N_list=list(map(int,sys.stdin.readline().split()))          #정수 N개를 입력 받아 리스트에 넣는다
M=int(sys.stdin.readline().rstrip())
M_list=list(map(int,sys.stdin.readline().split()))           
for i in M_list:            #확인하고자하는 정수가 N리스트에 있으면 1을 없으면 0을 순서대로 출력한다.
    if i in N_list:
        print(1)
    else:
        print(0)

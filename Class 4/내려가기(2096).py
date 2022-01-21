import sys
input=sys.stdin.readline                                            #이 문제는 처음 리스트에 자료를 받고 max값과 min값을 리스트를 만들어 dp를 진행했지만 메모리 제한이 4mb이므로 실패했다.

N=int(input())                                      

min_dp=[0]*3                                                        #min값을 저장할 min_dp이다
max_dp=[0]*3                                                        #max값을 저장할 max_dp이다.

min_temp=[0]*3                                                      #임시적으로 min값을 저장할 임시 리스트
max_temp=[0]*3                                                      #임시적으로 max값을 저장할 임시 리스트이다.

for i in range(N):
    a,b,c=map(int,input().split())                                  #원래 i번째 수를 리스트에 추가했지만 a,b,c로 받는다.
    for j in range(3):
        if j==0:                                                    #j가 0일때 갈 수 있는 곳을 j와 j+1이다
            min_temp[j]=a+min(min_dp[j],min_dp[j+1])
            max_temp[j]=a+max(max_dp[j],max_dp[j+1])
        elif j==1:                                                  #j가 1일때 갈 수 있는 곳을 j-1,j,j+1이다
            min_temp[j]=b+min(min_dp[j-1],min_dp[j],min_dp[j+1])
            max_temp[j]=b+max(max_dp[j-1],max_dp[j],max_dp[j+1])
        elif j==2:                                                  #j가 2일때 갈 수 있는 곳을 j-1와 j이다
            min_temp[j]=c+min(min_dp[j-1],min_dp[j])
            max_temp[j]=c+max(max_dp[j-1],max_dp[j])
    for j in range(3):                                              #임시적으로 저장하던 값을 min,max dp리스트에 넣어준다. 
        max_dp[j]=max_temp[j]                           
        min_dp[j]=min_temp[j]
            
print(max(max_dp),min(min_dp))

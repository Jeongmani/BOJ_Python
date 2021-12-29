A,B=map(int,input().split())  #2개의 자연수 공백으로 구분하여 입력받는다.
A_list=[] #A의 약수를 저장할 리스트
B_list=[] #B의 약수를 저장할 리스트
division_A=1
division_B=1

while division_A <= A:             #A의 약수들을 구해 리스트에 추가
    if A%division_A==0:
        A_list.append(division_A)
    division_A+=1

while division_B<= B:              #B의 약수들을 구해 리스트에 추가
    if B%division_B==0:
        B_list.append(division_B)
    division_B+=1

for i in A_list:                        #GCD구하기 : A,B리스트에 공통된 수들 중 가장 큰 값
    if i in B_list:
        GCD=i
print(GCD)

LCM=(A//GCD)*(B//GCD)*GCD   #LCM의 성질을 이용한 식

print(LCM)

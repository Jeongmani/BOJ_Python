Number = int(input())
Num=[]
for _ in range(Number):
    num_1,num_2= map(int, input().split())
    Num.append(num_1+num_2)
for i in range(Number):
    print(f"Case #{i+1}: {Num[i]}")
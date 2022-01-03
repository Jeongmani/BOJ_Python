import math

N=int(input())
count=0

while True:
    key=math.sqrt(N)
    key_number=math.ceil(key)
    count+=1
    N-=(key_number**2)
    if N==0:
        print(count)
        break
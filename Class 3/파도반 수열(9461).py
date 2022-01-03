import sys
def sequence(x):
    if x==1 or x==2 or x==3:
        return 1
    else:
        return sequence(x-3)+sequence(x-2)

T=int(sys.stdin.readline())
for _ in range(T):
    sequence(int(sys.stdin.readline()))
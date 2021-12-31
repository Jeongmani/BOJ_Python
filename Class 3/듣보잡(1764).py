import sys
N,M=map(int,sys.stdin.readline().split())
never_hear=set([])
never_seen=set([])
for i in range(N):
    hear=sys.stdin.readline().rstrip()
    never_hear.add(hear)
for j in range(M):
    seen=sys.stdin.readline().rstrip()
    never_seen.add(seen)
never_hear_seen=list(never_hear & never_seen)
never_hear_seen.sort()
print(len(never_hear_seen))
for h in never_hear_seen:
    print(h)

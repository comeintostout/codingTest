from collections import deque
import sys
FILE_NAME = "5.txt"
sys.stdin = open("in"+FILE_NAME,"rt")

N,M = map(int,input().split())
Q = deque(map(int,input().split()))
maxPat = max(Q)
cnt = 0
while Q:
    pat = Q.popleft()
    M -= 1
    if pat < maxPat:
        Q.append(pat)
        if M == -1:
            M = N-1
    else:
        cnt += 1
        if M == -1:
            break
        maxPat = max(Q)
        N -= 1
print(cnt)
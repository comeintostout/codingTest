import sys
input = sys.stdin.readline

T = int(input())

MAX_NUMBER = 1000001
SosuList = [True] * (MAX_NUMBER)
for i in range(3,1001,2):
    if SosuList[i]:
        for k in range(i+i, MAX_NUMBER, i):
            SosuList[k] = False

for _ in range(T):
    cnt = 0
    N = int(input())
    if N == 4:
        cnt+=1
    for i in range(3,int(N/2)+1,2):
        if SosuList[i] and SosuList[N-i]:
            cnt+=1
    print(cnt)
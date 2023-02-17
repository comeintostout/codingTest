import sys
input = sys.stdin.readline

N = int(input())
PODO = [0]
DP =[]
for _ in range(N):
    PODO.append(int(input()))
    DP.append([0,0,0])
DP.append([0,0,0])

DP[1][1] = DP[1][2] = PODO[1]

if N > 1:
    for i in range(2,N+1):
        DP[i][0] = max(DP[i-1])
        DP[i][1] = DP[i-1][0] + PODO[i]
        DP[i][2] = DP[i-1][1] + PODO[i]
print(max(DP[N]))
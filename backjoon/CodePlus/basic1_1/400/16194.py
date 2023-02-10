import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int,input().rstrip().split()))
DP = [0] * N
DP[0] = P[0]

for i in range(1,N):
    tmp = []
    for j in range(0,i):
        tmp.append(P[j] + DP[i-j-1])
    tmp.append(P[i])
    DP[i] = min(tmp)
print(DP[N-1])
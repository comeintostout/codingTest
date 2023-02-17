import sys
input = sys.stdin.readline

N = int(input())
A = []
DP = []

for i in range(1,N+1):
    A.append(list(map(int,input().rstrip().split())))
    DP.append([0] * i)

DP[0][0] = A[0][0]
for i in range(1,N):
    DP[i][0] = A[i][0] + DP[i-1][0]
    for j in range(1,i):
        DP[i][j] = max(DP[i-1][j-1], DP[i-1][j]) + A[i][j]
    DP[i][i] = A[i][i] + DP[i-1][i-1] 
print(max(DP[N-1]))
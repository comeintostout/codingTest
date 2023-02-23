N = int(input())
A = list(map(int,input().rstrip().split()))

DP = [ [0,0] for i in range(N)]
DP[0][0] = A[0]

maxVal = A[0]
for i in range(1,N):
    DP[i][0] = max(DP[i-1][0]+A[i], A[i])
    DP[i][1] = max(DP[i-1][0], DP[i-1][1] + A[i])
    if maxVal < max(DP[i]):
        maxVal = max(DP[i])
print(maxVal)
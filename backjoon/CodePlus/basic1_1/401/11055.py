N = int(input())
A = list(map(int,input().rstrip().split()))

DP = [0] * N
DP[0] = A[0]

maxSum = DP[0]
for i in range(1,N):
    for j in range(i):
        if A[j] < A[i] and DP[j] > DP[i]:
            DP[i] = DP[j]
    DP[i] += A[i]
    if DP[i] > maxSum:
        maxSum = DP[i]
print(maxSum)
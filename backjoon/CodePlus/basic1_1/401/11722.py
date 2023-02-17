N = int(input())
A = list(map(int,input().rstrip().split()))
DP = [1]* N

maxLength = 1
for i in range(1,N):
    maxL = 0
    for j in range(i):
        if A[j] > A[i] and DP[j] > maxL:
            maxL = DP[j]
    DP[i] = maxL + 1
    if DP[i] > maxLength:
        maxLength= DP[i]

print(maxLength)
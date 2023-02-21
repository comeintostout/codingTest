N = int(input())
A = list(map(int,input().rstrip().split()))
B = A[::-1]

DP = [1] * N
reverDP = [1] * N

for i in range(1,N):
    Max = 0
    for j in range(i):
        if A[i] > A[j] and Max < DP[j]:
            Max = DP[j]
    DP[i] = Max + 1

for i in range(1,N):
    Max = 0
    for j in range(i):
        if B[i] > B[j] and Max < reverDP[j]:
            Max = reverDP[j]
    reverDP[i] = Max + 1

Max = 0
for i in range(N):
    if DP[i] + reverDP[N-i-1] - 1 >= Max:
        Max = DP[i] + reverDP[N-i-1] - 1
print(Max)
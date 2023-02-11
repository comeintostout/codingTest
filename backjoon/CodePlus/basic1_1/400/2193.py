N = int(input())

DP = [1] * (N+1)

for i in range(3, N+1):
    for j in range(1,i-1):
        DP[i] += DP[j]
print(DP[N])
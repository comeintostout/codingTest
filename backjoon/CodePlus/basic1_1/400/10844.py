N = int(input())

DP= [[0,0,0,0,0,0,0,0,0,0] for i in range(N+1)]
for k in range(1,10):
    DP[1][k] = 1

for i in range(2,N+1):
    DP[i][0] = DP[i-1][1] % 1000000000
    DP[i][9] = DP[i-1][8] % 1000000000
    for k in range(1,9):
        DP[i][k] = (DP[i-1][k-1] + DP[i-1][k+1]) % 1000000000
print(sum(DP[N])% 1000000000)
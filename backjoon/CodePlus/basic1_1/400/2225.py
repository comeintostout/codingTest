[N,K] = map(int,input().rstrip().split())

DP = [ [0 for j in range(K+1)] for i in range(N+1)]
for j in range(0,K+1):
    DP[0][j] = 1

for i in range(1,N+1):
    for j in range(1,K+1):
        for k in range(0,i+1):
            DP[i][j] += DP[i-k][j-1] % 1000000000
print(DP[N][K]% 1000000000)
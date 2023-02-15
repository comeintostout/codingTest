N = int(input())

DP = [ [0,0,0,0,0,0,0,0,0,0] for i in range(N+1)]
for i in range(10):
    DP[1][i] = 1

for i in range(2,N+1):
    for j in range(0,10):
        for k in range(j,10):
            DP[i][j]+= DP[i-1][k]% 10007
print(sum(DP[N]) % 10007 )
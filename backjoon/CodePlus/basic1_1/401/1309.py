N = int(input())

DP = [ [0,0] for i in range(N)]
DP[0][0] = 1
DP[0][1] = 2

for i in range(1,N):
    DP[i][0] = (DP[i-1][1] + DP[i-1][0]) % 9901
    DP[i][1] = ((DP[i-1][0] * 2) + (DP[i-1][1]))  % 9901

print(sum(DP[N-1]) % 9901)
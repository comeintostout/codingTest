import sys
n = int(sys.stdin.readline())

DP = [[-1,-1,-1] for i in range(n)]
Price = []
for i in range(n):
    Price.append(list(map(int,sys.stdin.readline().split())))

DP[0][0] = Price[0][0]
DP[0][1] = Price[0][1]
DP[0][2] = Price[0][2]

for house in range(1,n):
    DP[house][0] = Price[house][0] + min(DP[house-1][1], DP[house-1][2])
    DP[house][1] = Price[house][1] + min(DP[house-1][0], DP[house-1][2])
    DP[house][2] = Price[house][2] + min(DP[house-1][0], DP[house-1][1])

print(min(DP[n-1][0],DP[n-1][1],DP[n-1][2]))
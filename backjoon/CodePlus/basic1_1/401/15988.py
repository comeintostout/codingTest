import sys
input = sys.stdin.readline

DP = [0] * 1000001
DP[1] = 1
DP[2] = 2
DP[3] = 4
biggestN = 3

TC = int(input())
for _ in range(TC):
    N = int(input())
    if biggestN >= N:
        print(DP[N]% 1000000009)
    else:
        for i in range(biggestN+1, N+1):
            DP[i] = DP[i-1] % 1000000009 + DP[i-2]% 1000000009 + DP[i-3]% 1000000009
        biggestN = N
        print(DP[N]% 1000000009)

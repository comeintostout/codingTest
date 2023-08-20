import sys
sys.stdin = open("in5.txt", "rt")

N = int(input())
Stones = [list(map(int, input().split())) for _ in range(N)]
Stones.sort(key=lambda x: (x[0], x[2]), reverse=True)
DP = [0]*N

for i in range(N):
    height = 0
    for j in range(i):
        if Stones[i][2] < Stones[j][2]:
            height = max(height, DP[j])
    DP[i] = height + Stones[i][1]
print(max(DP))

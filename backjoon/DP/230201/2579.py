import sys

N = int(sys.stdin.readline())
Points = []
DP = [[-1,-1] for _ in range(N)]

for i in range(N):
    Points.append(int(sys.stdin.readline()))

if N <= 2:
    print(sum(Points))
else:
    DP[0][0] = 0
    DP[0][1] = Points[0]
    DP[1][0] = Points[0]
    DP[1][1] = Points[1] + Points[0]

    for stair in range(2,N):
        DP[stair][0] = DP[stair-1][1]
        DP[stair][1] = Points[stair] + max(DP[stair - 1][0], Points[stair-1] + DP[stair-2][0])

    print(DP[N-1][1])

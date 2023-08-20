import sys
sys.stdin= open("in5.txt",'rt')

N = int(input())
Maze= [list(map(int,input().split())) for _ in range(N)]
DP = [[0]*N for _ in range(N)]
DP[0][0]= Maze[0][0]

for i in range(1,N):
    DP[0][i] = DP[0][i-1] + Maze[0][i]
    DP[i][0] = DP[i-1][0] + Maze[i][0]

for r in range(1,N):
    for c in range(1,N):
        DP[r][c] = min(DP[r][c-1], DP[r-1][c]) + Maze[r][c]
print(DP[N-1][N-1])
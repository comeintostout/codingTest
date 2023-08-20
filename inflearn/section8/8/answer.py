import sys
sys.stdin = open("in5.txt","rt")

N = int(input())
Maze = [list(map(int,input().split())) for _ in range(N)]
DP = [[0]*N for _ in range(N)]

def dfs(r,c):
    global Maze, DP
    if DP[r][c] == 0:
        if r > 0 and c > 0:
            DP[r][c] = Maze[r][c] + min(dfs(r-1,c), dfs(r,c-1))
        elif r > 0 and c == 0:
            DP[r][c] = Maze[r][c] + dfs(r-1,c)
        elif r == 0 and c > 0:
            DP[r][c] = Maze[r][c] + dfs(r,c-1)
        else:
            DP[r][c] = Maze[r][c]
    return DP[r][c]

print(dfs(N-1,N-1))

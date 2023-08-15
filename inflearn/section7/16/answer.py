import sys
sys.stdin = open("in5.txt","rt")

def dfs(row,col):
    global N, ladders, visited,isFinished
    if isFinished:
        return 
    if row == 0:
        print(col)
        isFinished = True
        return

    for r,c in [(row,col-1),(row,col+1),(row-1,col)]:
        if 0<=r<N and 0<=c<N and ladders[r][c] and visited[r][c]==0:
            visited[r][c] = 1
            dfs(r,c)
            visited[r][c] = 0

if __name__ == "__main__":
    N = 10
    ladders = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    isFinished = False

    row = col = 0
    for c in range(N):
        if ladders[N-1][c] == 2:
            row = N-1
            col = c
            break
    dfs(row,col)
    
    


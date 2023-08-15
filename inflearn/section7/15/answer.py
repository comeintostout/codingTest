import sys
from collections import deque
sys.stdin = open("in4.txt","rt")

if __name__ == "__main__":
    M, N = map(int,input().split())
    Tomatoes = [list(map(int,input().split())) for _ in range(N)]
    Q = deque()
    dist = [[0]*M for _ in range(N)]

    for r in range(N):
        for c in range(M):
            if Tomatoes[r][c] == 1:
                Q.append((r,c))

    while Q:
        row,col = Q.popleft()
        for r,c in [(row-1,col), (row,col-1), (row+1,col), (row,col+1)]:
            if 0<=r<N and 0<=c<M and Tomatoes[r][c] == 0:
                Tomatoes[r][c] = 1
                dist[r][c] = dist[row][col]+1
                Q.append((r,c))
    
    isFinished = False
    maxDist = 0
    for r in range(N):
        if isFinished:
            break
        maxDist = max(maxDist, max(dist[r]))
        for c in range(M):
            if Tomatoes[r][c] == 0:
                maxDist = -1
                isFinished= True
                break
        
    print(maxDist)
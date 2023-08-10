import sys
from collections import deque
sys.stdin = open("in1.txt","rt")

if __name__ == "__main__":
    N = 7
    maze = [[1,1,1,1,1,1,1,1,1]]
    for _ in range(N):
        rows = list(map(int,input().split()))
        rows.insert(0,1)
        rows.append(1)
        maze.append(rows)     
    maze.append([1,1,1,1,1,1,1,1,1])  

    visitied = [[0 for _ in range(N+1)] for _ in range(N+1)]    
    distance = [[-1 for _ in range(N+1)] for _ in range(N+1)]    
    queue = deque()
    success = 0

    queue.append((1,1))
    visitied[1][1] = 1
    distance[1][1] = 0

    while queue:
        row, col = queue.popleft()
        if row == N and col == N:
            success = 1
            break
        for nextR,nextC in [(row+1,col),(row,col+1), (row-1,col), (row,col-1)]:
            if maze[nextR][nextC] == 0 and visitied[nextR][nextC] == 0:
                visitied[nextR][nextC] = 1
                distance[nextR][nextC] = distance[row][col]+1
                queue.append((nextR,nextC))


    print(distance[N][N])

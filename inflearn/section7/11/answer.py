import sys
from collections import deque
sys.stdin = open("in5.txt","rt")

if __name__ == "__main__":
    N = int(input())
    maze = [[0] * (N+1)]
    for _ in range(N):
        rows = list(map(int,input().split()))
        rows.insert(0,0)
        rows.append(0)
        maze.append(rows)     
    maze.append([0] * (N+1))  

    queue = deque()
    success = 0

    minValue = maze[1][1]+1
    minPoint = ()
    maxValue = maze[1][1]-1
    maxPoint = ()
    for i in range(1,N+1):
        for j in range(1,N+1):
            if maze[i][j] < minValue:
                minValue = maze[i][j]
                minPoint = (i,j)
            if maze[i][j] > maxValue:
                maxValue = maze[i][j]
                maxPoint = (i,j)
    queue.append(minPoint)
    count = 0

    while queue:
        row, col = queue.popleft()
        if row == maxPoint[0] and col == maxPoint[1]:
            count +=1
            continue
        for nextR,nextC in [(row+1,col),(row,col+1), (row-1,col), (row,col-1)]:
            if maze[nextR][nextC] > maze[row][col]:
                queue.append((nextR,nextC))

    print(count)

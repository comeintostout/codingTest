import sys
from collections import deque
sys.stdin = open("in5.txt","rt")

if __name__ == "__main__":
    N = int(input())
    Towns = [[0] * (N+2)]
    heightSet = set()
    for _ in range(N):
        rows = list(map(int,input().split()))
        heightSet = heightSet.union(set(rows))
        rows.insert(0,0)
        rows.append(0)
        Towns.append(rows)     
    Towns.append([0] * (N+2))  

    heightList = list(heightSet)
    heightList.sort()
    maxTowns = 0

    for Water in heightList:
        visited = [[0 for _ in range(N+2)] for _ in range(N+2)]
        queue = deque()
        numberOfIsland = 1

        for i in range(1,N+1):
            for j in range(1,N+1):
                if Towns[i][j] > Water and visited[i][j] == 0:
                    queue.append((i,j))
                    visited[i][j] = 1
                    while queue:
                        row, col = queue.popleft()
                        for nextR,nextC in [(row+1,col),(row,col+1), (row-1,col), (row,col-1)]:
                            if Towns[nextR][nextC] > Water and visited[nextR][nextC] == 0:
                                queue.append((nextR,nextC))
                                visited[nextR][nextC] = 1

                    numberOfIsland += 1
        maxTowns = max(maxTowns, numberOfIsland-1)
    print(maxTowns)
                    

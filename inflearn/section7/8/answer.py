import sys
from collections import deque
sys.stdin = open("in5.txt","rt")

if __name__ == "__main__":
    N = int(input())
    Apples = []

    for _ in range(N):
        Apples.append(list(map(int,input().split())))

    queue = deque()
    visited = [[0 for _ in range(N)] for _ in range(N)]
    dis = [[0 for _ in range(N)] for _ in range(N)]

    now = (N//2, N//2)
    count = 0
    queue.append(now)
    while queue:
        row, col = queue.popleft()
        if dis[row][col] < N//2:
            for nextR, nextC in [(row-1,col),(row+1,col),(row,col-1), (row,col+1)]:
                if visited[nextR][nextC] == 0:
                    dis[nextR][nextC] = dis[row][col]+1
                    visited[nextR][nextC] = 1
                    queue.append((nextR,nextC))
                    count += Apples[nextR][nextC]
        else:
            continue
    print(count)

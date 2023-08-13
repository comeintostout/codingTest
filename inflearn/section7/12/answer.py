import sys
from collections import deque
sys.stdin = open("in5.txt","rt")

if __name__ == "__main__":
    N = int(input())
    Apts = [[0] * (N+2)]
    for _ in range(N):
        rows = list(map(int,list(input())))
        rows.insert(0,0)
        rows.append(0)
        Apts.append(rows)     
    Apts.append([0] * (N+2))  

    visited = [[0 for _ in range(N+2)] for _ in range(N+2)]

    queue = deque()
    numberOfComplex = 1
    complexList = [0] * (N*N+2)

    for i in range(1,N+1):
        for j in range(1,N+1):
            if Apts[i][j] and visited[i][j] == 0:
                queue.append((i,j))
                visited[i][j] = 1
                while queue:
                    row, col = queue.popleft()
                    complexList[numberOfComplex] += 1

                    for nextR,nextC in [(row+1,col),(row,col+1), (row-1,col), (row,col-1)]:
                        if Apts[nextR][nextC] and visited[nextR][nextC] == 0:
                            queue.append((nextR,nextC))
                            visited[nextR][nextC] = 1

                numberOfComplex += 1
    result =complexList[1:numberOfComplex]
    result.sort()
    print(len(result))
    for r in result:
        print(r)
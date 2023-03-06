import sys
input = sys.stdin.readline

def getMaxScore(blocks,N,M):
    if N == 2 and M == 2:
        return sum(blocks[0]) + sum(blocks[1])
    elif N == 2 and M == 3:
        sum1 = sum(blocks[0])
        sum2 = sum(blocks[1])
        return max(sum1 + max(blocks[1]), sum2 + max(blocks[0]), sum1+sum2 - min(blocks[0][0] + blocks[1][2], blocks[0][2] + blocks[1][0]))
    else:
        return sum(blocks)

[N, M] = map(int,input().rstrip().split())
MAP = []

for row in range(N):
    MAP.append(list(map(int,input().rstrip().split())))

MAX = 0
for row in range(N):
    for col in range(M):
        if col < M - 1 and row < N - 1:
            MAX = max(MAX, getMaxScore([[MAP[row][col], MAP[row][col+1]], [MAP[row+1][col], MAP[row+1][col+1]]],2,2))
        if col < M - 2 and row < N - 1:
            MAX = max(MAX, getMaxScore( [ [MAP[row][col], MAP[row][col+1], MAP[row][col+2]], [MAP[row+1][col], MAP[row+1][col+1], MAP[row+1][col+2]]  ],2,3))
        if col < M - 1 and row < N - 2:
            MAX = max(MAX, getMaxScore([[MAP[row][col], MAP[row+1][col], MAP[row+2][col]], [MAP[row][col+1], MAP[row+1][col+1], MAP[row+2][col+1]]],2,3))
        if col < M - 3:
            MAX = max(MAX, getMaxScore([MAP[row][col],MAP[row][col+1],MAP[row][col+2],MAP[row][col+3]],1,4))
        if row < N - 3:
            MAX = max(MAX, getMaxScore([MAP[row][col],MAP[row+1][col],MAP[row+2][col],MAP[row+3][col]],1,4))

print(MAX)
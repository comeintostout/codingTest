import sys
sys.stdin = open("in1.txt","rt")

n, m = map(int,input().split())
adjMatrix = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    st,ed,weight = map(int,input().split())
    adjMatrix[st][ed] = weight


for i in range(1,n+1):
    for j in range(1,n+1):
        print(adjMatrix[i][j], end=" ")
    print()
import sys
sys.stdin = open("in5.txt","rt")

def DFS(route,start):
    global n, adjMatrix, cnt
    if start == n:
        cnt += 1
        return

    for ed, value in enumerate(adjMatrix[start]):
        if value and str(ed) not in route:
            tmp = route[:]
            tmp.append(str(ed))
            DFS(tmp,ed)


if __name__ == "__main__":
    n, m = map(int,input().split())
    adjMatrix = [[0]*(n+1) for _ in range(n+1)]
    cnt = 0
    for i in range(m):
        st,ed = map(int,input().split())
        adjMatrix[st][ed] = 1
        
    DFS(["1"],1)
    print(cnt)
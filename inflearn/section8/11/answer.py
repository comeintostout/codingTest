import sys
sys.stdin = open("in5.txt","rt")

N, M = map(int,input().split())
Problems = [list(map(int,input().split())) for _ in range(N)]
DP= [[0]*(M+1) for _ in range(N)]

def dfs(index, leftTime):
    global Problems, DP

    if leftTime == 0 or index < 0:
        return 0
    
    if DP[index][leftTime] == 0:
        if leftTime >= Problems[index][1]:
            DP[index][leftTime] = max(Problems[index][0] + dfs(index-1,leftTime-Problems[index][1]), dfs(index-1,leftTime))
        else:
            DP[index][leftTime] = dfs(index-1,leftTime)
    return DP[index][leftTime]

print(dfs(N-1,M))
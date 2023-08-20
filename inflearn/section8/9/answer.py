import sys
sys.stdin = open("in5.txt",'rt')

N, Limit= map(int,input().split())
Stones = [list(map(int,input().split())) for _ in range(N)]
DP = [[0]*(Limit+1) for _ in range(N)]

def dfs(index, weight):
    global N,Stones, DP
    if index < 0 or weight <= 0:
        return DP[0][0]
    
    if DP[index][weight] == 0:
        if weight >= Stones[index][0]:
            DP[index][weight] = max(Stones[index][1] + dfs(index,weight-Stones[index][0]), Stones[index][1] + dfs(index-1,weight-Stones[index][0]), dfs(index-1,weight))
        else:
            return dfs(index-1,weight)
    return DP[index][weight]

print(dfs(N-1,Limit))


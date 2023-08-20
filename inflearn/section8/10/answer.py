import sys
sys.stdin = open("in5.txt","rt")

N = int(input())
Coins = list(map(int,input().split()))
Change= int(input())
DP = [[0]*(Change+1) for _ in range(N)]

def dfs(index, left):
    global Coins, DP

    if left == 0:
        return 0
    elif index < 0:
        return 9999999
    
    if DP[index][left] == 0:
        if left >= Coins[index]:
            DP[index][left] = min(1+dfs(index,left-Coins[index]),1+dfs(index-1,left-Coins[index]),dfs(index-1,left))
        else:
            DP[index][left] = dfs(index-1,left)
    return DP[index][left]

print(dfs(N-1,Change))
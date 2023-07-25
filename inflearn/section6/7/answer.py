import sys

FILE_NAME = "5.txt"
sys.stdin = open("in"+FILE_NAME,"rt")

def DFS(total, pick):
    global goal, minCoin, Coins
    if pick > minCoin:
        return
    if total == goal:
        minCoin = min(pick,minCoin)
    elif total < goal:
        for coin in Coins:
            DFS(total+coin,pick+1)


if __name__ == "__main__":
    N = int(input())
    Coins = list(map(int,input().split()))
    goal = int(input())
    Coins.sort(reverse=True)

    minCoin = 9999
    DFS(0,0)
    print(minCoin)
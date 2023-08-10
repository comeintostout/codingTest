import sys
sys.stdin = open("in6.txt","rt")

def init():
    global T,K,coins
    T = int(input())
    K = int(input())
    for i in range(K):
        p,n = map(int,input().split())
        coins.append((p,n))

def DFS(index, price):
    global T, K, ways, coins
    
    if price == T:
        ways += 1
        return
    elif price > T:
        return 

    if index == K:
        return
    
    p, n = coins[index]
    for i in range(n+1):
        DFS(index+1,price + i*p)

if __name__ == "__main__":
    T = K = ways = 0
    coins = []
    init()

    DFS(0,0)
    print(ways)

    
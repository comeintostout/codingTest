N,K = map(int,input().split())
coins = []
for i in range(N):
    coin = int(input())
    if coin <= K:
        coins.append(coin)

i = len(coins)-1
answer = 0
while K > 0 and i>=0:
    coin = coins[i]
    answer += (K // coin)
    K = K % coin
    i -= 1

print(answer)
    
import math
N = int(input())
Root = math.floor(math.sqrt(N))

A = list(map(lambda x : x*x, range(1,Root+1)))

DP = [0]*(N+1)
DP[1] = 1

for i in range(2,N+1):
    tmp = []
    for k in A:
        if k > i:
            break
        tmp.append(DP[i-k])
    DP[i] = 1 + min(tmp)
print(DP[N])

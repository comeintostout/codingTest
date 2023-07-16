N = int(input())
P = list(map(int,input().split()))
P.sort()
answer = 0

times = N
for t in P:
    answer += (t*times)
    times-=1
print(answer)
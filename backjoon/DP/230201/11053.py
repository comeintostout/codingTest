import sys
length = int(sys.stdin.readline())
Numbers = list(map(int,sys.stdin.readline().split( )))

DP= [1 for _ in range(0,length)]

for i in range(1,length):
    for j in range(0,i):
        if Numbers[i] > Numbers[j]:
            DP[i] = max(DP[i], DP[j] + 1)

print(max(DP))
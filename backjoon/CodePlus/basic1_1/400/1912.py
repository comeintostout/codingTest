N = int(input())
A = list(map(int,input().rstrip().split()))

DP = [A[0]]
for i in range(N-1):
    DP.append(max(DP[i] + A[i+1], A[i+1]))
print(max(DP))
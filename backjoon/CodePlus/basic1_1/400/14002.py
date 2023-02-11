N = int(input())
A = list(map(int,input().rstrip().split()))

DP = [ [] for i in range(N)]
DP[0] = [A[0]]

maxIdxInArray = 0
for i in range(1,N):
    maxIdx = i
    flag = False
    for j in range(0,i):
        if A[j] < A[i] and len(DP[j]) > len(DP[maxIdx]):
            flag = True
            maxIdx = j
    if flag:
        for k in DP[maxIdx]:
            DP[i].append(k)
        DP[i].append(A[i])        
    else:
        DP[i] = [A[i]]
    if len(DP[i]) >= len(DP[maxIdxInArray]):
        maxIdxInArray = i

print(len(DP[maxIdxInArray]))
print(" ".join(map(str,DP[maxIdxInArray])))

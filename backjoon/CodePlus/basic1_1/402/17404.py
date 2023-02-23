import sys
input = sys.stdin.readline

def getFirstHouseInfo(A,B):
    if A[0] > B[0]:
        return B[1]
    elif A[0] < B[0]:
        return A[1]
    else:
        return list(set(A[1] + B[1]))

N = int(input())
DP = [ [ [0,[]],[0,[]],[0,[]] ] for i in range(N)]
DP2 = [ [ [0,[]],[0,[]],[0,[]] ] for i in range(N)]

A = []
for i in range(N):
    A.append(list(map(int,input().rstrip().split())))
A2 = A[::-1]

DP[0][0] = [A[0][0],[0]]
DP[0][1] = [A[0][1],[1]]
DP[0][2] = [A[0][2],[2]]
DP2[0][0] = [A2[0][0],[0]]
DP2[0][1] = [A2[0][1],[1]]
DP2[0][2] = [A2[0][2],[2]]

for i in range(1,N-1):
    DP[i][0][0] = A[i][0] + min(DP[i-1][1][0], DP[i-1][2][0])
    DP[i][0][1] = getFirstHouseInfo(DP[i-1][1], DP[i-1][2])

    DP[i][1][0] = A[i][1] + min(DP[i-1][0][0], DP[i-1][2][0])
    DP[i][1][1] = getFirstHouseInfo(DP[i-1][0], DP[i-1][2])

    DP[i][2][0] = A[i][2] + min(DP[i-1][0][0], DP[i-1][1][0])
    DP[i][2][1] = getFirstHouseInfo(DP[i-1][0], DP[i-1][1])

    DP2[i][0][0] = A2[i][0] + min(DP2[i-1][1][0], DP2[i-1][2][0])
    DP2[i][0][1] = getFirstHouseInfo(DP2[i-1][1], DP2[i-1][2])

    DP2[i][1][0] = A2[i][1] + min(DP2[i-1][0][0], DP2[i-1][2][0])
    DP2[i][1][1] = getFirstHouseInfo(DP2[i-1][0], DP2[i-1][2])

    DP2[i][2][0] = A2[i][2] + min(DP2[i-1][0][0], DP2[i-1][1][0])
    DP2[i][2][1] = getFirstHouseInfo(DP2[i-1][0], DP2[i-1][1])

Answer= []

for nth in range(3):
    a = 0 if nth > 0 else 1
    b = 1 if nth == 2 else 2

    if not (nth in DP[N-2][a][1] and len(DP[N-2][a][1]) == 1):
        Answer.append(A[N-1][nth] + DP[N-2][a][0])
    if not (nth in DP[N-2][b][1] and len(DP[N-2][b][1]) == 1):
        Answer.append(A[N-1][nth] + DP[N-2][b][0])

    if not (nth in DP2[N-2][a][1] and len(DP2[N-2][a][1]) == 1):
        Answer.append(A2[N-1][nth] + DP2[N-2][a][0])
    if not (nth in DP2[N-2][b][1] and len(DP2[N-2][b][1]) == 1):
        Answer.append(A2[N-1][nth] + DP2[N-2][b][0])

print(min(Answer))


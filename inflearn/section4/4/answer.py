from concurrent.futures import process
import sys
sys.stdin = open("in5.txt","rt")

[N, C] = list(map(int,input().strip().split(' ')))
X = []
for n in range(0,N):
    x = int(input().strip())
    X.append(x)

X.sort()

left = 1
right = (X[-1] - X[0])//(C - 1)

def isValid(mid):
    pick = []
    pick.append(X[0])
    for i in range(1,len(X)):
        if X[i] - pick[-1] >= mid:
            pick.append(X[i])
            if len(pick) == C:
                return True
    return False

answer = 0
while left <= right:
    mid = (left + right) // 2
    if isValid(mid):
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)
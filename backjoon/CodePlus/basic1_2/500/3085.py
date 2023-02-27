import sys
input = sys.stdin.readline

def getLineScore(line):
    maxLength = 1
    length = 1
    before = ""
    for c in line:
        if c == before:
            length += 1
        else:
            maxLength = max(maxLength, length)
            length = 1
            before = c
    return max(maxLength, length)

def getVerticalLine(candies, idx):
    ret = []
    for i in range(len(candies)):
        ret.append(candies[i][idx])
    return ret

def getRowCol(N,a):
    return [int(a / N), int(a % N)]

def swapCandies(candies, N, a,b):
    [rowA, colA] = getRowCol(N,a)
    [rowB, colB] = getRowCol(N,b)

    c = candies[rowA][colA]
    candies[rowA][colA] = candies[rowB][colB]
    candies[rowB][colB] = c

N = int(input())
candies = []
for i in range(N):
    candies.append(list(input().rstrip()))

maxScore = 1
for i in range(N):
    maxScore = max(maxScore, getLineScore(candies[i]), getLineScore(getVerticalLine(candies,i)))

isBreak = False
for a in range(N*N):
    for b in range(a+1,N*N):
        if maxScore == N:
            isBreak = True
            break
        [rowA, colA] = getRowCol(N,a)
        [rowB, colB] = getRowCol(N,b)
        if abs(rowA-rowB) + abs(colA-colB) == 1:
            swapCandies(candies, N, a,b)
            if rowA == rowB:
                maxScore = max(maxScore, getLineScore(candies[rowA]), getLineScore(getVerticalLine(candies,colA)),getLineScore(getVerticalLine(candies,colB)))
            else:
                maxScore = max(maxScore, getLineScore(candies[rowA]),getLineScore(candies[rowB]), getLineScore(getVerticalLine(candies,colA)))
            swapCandies(candies, N, a,b)
    if isBreak:
        break
print(maxScore)
import sys
input = sys.stdin.readline

A = []
for _ in range(9):
    A.append(int(input()))

A.sort()
sumA = sum(A)

isBreak = False
for i in range(8):
    for j in range(i+1,9):
        if (sumA - A[i] - A[j]) == 100:
            for k in range(len(A)):
                if k != i and k != j:
                    print(A[k])
            isBreak = True
            break
    if isBreak:
        break
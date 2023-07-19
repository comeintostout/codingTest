from collections import deque
import sys
FILE_NAME = "5.txt"
sys.stdin = open("in"+FILE_NAME,"rt")

vaildOrder = input()
N = int(input())
result = []

def isValidOrder(vaildOrder, inputOrder):
    i = 0
    for st in inputOrder:
        if i == len(vaildOrder):
            return "YES"
        if st in vaildOrder[i+1:]:
            return "NO"
        if st == vaildOrder[i]:
            i += 1

    if i == len(vaildOrder):
        return "YES"
    else:
        return "NO"

for i in range(N):
    result.append(isValidOrder(vaildOrder, input()))
print("\n".join(result))
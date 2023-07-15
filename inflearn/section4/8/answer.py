import sys
sys.stdin = open("in5.txt","rt")
from collections import deque

N,M = map(int,input().split())
weights = list(map(int,input().split()))
weights.sort()
weights = deque(weights)

boats = 0
while len(weights) >= 2:
    bigger = weights.pop()
    if bigger + weights[0] <= M:
        weights.popleft()
    boats+=1
if weights:
    boats+=1
print(boats)
import sys
sys.stdin = open("in5.txt","rt")
from collections import deque

L = int(input())
boxes = list(map(int,input().split()))
boxes.sort()
M = int(input())
length = len(boxes)

for i in range(M):
    boxes[-1] -= 1
    boxes[0] += 1
    
    i = 1
    while i < length and boxes[-i] < boxes[-i-1]:
        tmp = boxes[-i]
        boxes[-i] = boxes[-i-1]
        boxes[-i-1] = tmp
        i += 1
    
    i = 0
    while i < length-1 and boxes[i] > boxes[i+1]:
        tmp = boxes[i]
        boxes[i] = boxes[i+1]
        boxes[i+1] = tmp
        i += 1
print(boxes[-1]- boxes[0])



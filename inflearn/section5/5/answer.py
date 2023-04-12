import sys
from collections import deque

FILE_NAME = "3.txt"
sys.stdin = open("in"+FILE_NAME,"rt")

p, k = map(int,input().split())

sys.stdin = open("out"+FILE_NAME,"rt")
realAnswer = int(input())

queue = deque(list(range(1,p+1)))

i = 1
while len(queue) > 1:
    if i != k:
        queue.append(queue.popleft())
        i += 1
    else:
        i = 1
        queue.popleft()

myAnswer = queue[0]
print(myAnswer == realAnswer,myAnswer)
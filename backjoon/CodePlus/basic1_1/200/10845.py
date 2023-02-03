import sys

input = sys.stdin.readline

N = int(input())

queue = []
front =0
rear = 0

for _ in range(N):
    query = input().split()
    if query[0] == "push":
        queue.append(query[1])
        rear += 1
    elif query[0] == "pop":
        if front >= rear:
            print(-1)
        else:
            print(queue[front])
            front += 1
    elif query[0] == 'size':
        print(rear - front)
    elif query[0] == "empty":
        print(0 if rear > front else 1)
    elif query[0] == "front":
        if rear > front:
            print(queue[front])
        else:
            print(-1)
    else:
        if rear > front:
            print(queue[rear-1])
        else:
            print(-1)
    

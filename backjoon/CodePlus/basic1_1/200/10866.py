import sys

input = sys.stdin.readline

N = int(input())

Deque = dict()
front = 0
back = -1

for _ in range(N):
    query = input().split()
    if query[0] == "push_front":
        front -= 1
        Deque[str(front)] = query[1]
    elif query[0] == "push_back":
        back += 1
        Deque[str(back)] = query[1]
    elif query[0] == "pop_front":
        if front <= back:
            print(Deque[str(front)])
            front += 1
        else:
            print(-1)
    elif query[0] == "pop_back":
        if front <= back:        
            print(Deque[str(back)])
            back -= 1
        else:
            print(-1)
    elif query[0] == "size":
        print(back - front + 1)
    elif query[0] == "empty":
        print(0 if back >= front else 1)
    elif query[0] == "front":
        if front <= back:
            print(Deque[str(front)])
        else:
            print(-1)
    else:
        if front <= back:      
            print(Deque[str(back)])
        else:
            print(-1)

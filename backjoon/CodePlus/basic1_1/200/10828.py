import sys

N = int(sys.stdin.readline())

stack = []
for _ in range(N):
    query = sys.stdin.readline().split()
    if query[0] == "push":
        stack.append(query[1])
    elif query[0] == "pop":
        pop = -1 if len(stack) == 0 else stack.pop()
        print(pop)
    elif query[0] == "size":
        print(len(stack))
    elif query[0] == "empty":
        print(1 if len(stack) == 0 else 0)
    else:
        print(-1 if len(stack) == 0 else stack[-1])
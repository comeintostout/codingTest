import sys

input = sys.stdin.readline
N = int(input())

output = []
stack = []
last = 0
for _ in range(N):
    num = int(input())
    if num > last:
        while last < num:
            stack.append(last + 1)
            output.append('+')
            last += 1
        stack.pop()
        output.append('-')
    elif num != stack[-1]:
        output = "NO"
        break
    else:
        stack.pop()
        output.append('-')

if output == "NO":
    print("NO")
else:
    print("\n".join(output))
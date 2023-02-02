import sys

input = sys.stdin.readline
N = int(input())

for _ in range(N):
    stack = []
    answer = 'YES'
    for letter in list(input()):
        if letter == '(':
            stack.append(letter)
        elif letter == ")":
            if len(stack) > 0:
                stack.pop()
            else:
                answer = 'NO'  
                break
    if len(stack) > 0:
        answer = 'NO'
    print(answer)
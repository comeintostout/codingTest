import sys
input = sys.stdin.readline

Alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
N = int(input())
F = list(input().rstrip())
Data = dict()

for i in range(N):
    Data[Alphabet[i]] = int(input())

F = list(map(lambda f : Data[f] if f in Alphabet else f,F))

stack = []
for a in F:
    if a == "+":
        num2 = stack.pop()
        num1 = stack.pop()
        stack.append(num1 + num2)
    elif a == "-":
        num2 = stack.pop()
        num1 = stack.pop()
        stack.append(num1 - num2)
    elif a == "*":
        num2 = stack.pop()
        num1 = stack.pop()
        stack.append(num1 * num2)
    elif a == "/":
        num2 = stack.pop()
        num1 = stack.pop()
        stack.append(num1 / float(num2))
    else:
        stack.append(a)
print("{0:.2f}".format(stack.pop()))
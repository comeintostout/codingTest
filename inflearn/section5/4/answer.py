import sys
FILE_NAME = "5.txt"
sys.stdin = open("in"+FILE_NAME,"rt")

inputString = input()
stack = []

for st in inputString:
    if st.isdecimal():
        stack.append(int(st))
    else:
        right = stack.pop()
        left = stack.pop()
        if st == "+":
            stack.append(left+right)
        elif st == '-':
            stack.append(left-right)
        elif st == "*":
            stack.append(left*right)
        elif st == '/':
            stack.append(int(left/right))
print(stack[0])
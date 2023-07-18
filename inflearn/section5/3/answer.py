import sys
FILE_NAME = "5.txt"
sys.stdin = open("in"+FILE_NAME,"rt")

inputString = input()
stack = []
answer= ""

for st in inputString:
    if st.isdecimal():
        answer += st
    elif st=="(":
        stack.append(st)
    elif st=="*" or st=="/":
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            answer += stack.pop()
        stack.append(st)
    elif st=="+" or st=="-":
        while stack and stack[-1] != '(':
            answer += stack.pop()
        stack.append(st)
    elif st==')':
        while stack and stack[-1] != '(':
            answer += stack.pop()
        stack.pop()

while stack:
    answer+=stack.pop()

print(answer)

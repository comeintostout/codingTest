import sys
input = sys.stdin.readline

Operator = ['+', '-', '*', '/', '(', ')']
F = input().rstrip()

stack = []
ans = ''
for letter in F:
    if letter.isalpha():
        ans += letter
    else:
        if letter == '(': 
            stack.append(letter)
        elif letter == '*' or letter == '/': # 먼저 들어오고 같은 우선순위에 있는 */는 ans에 넣어줌
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                ans += stack.pop()
            stack.append(letter)
        elif letter == '+' or letter == '-': #이보다 낮은 우선 순위가 없어서 연산자이면 전부 ans에 넣어줌
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.append(letter)
        elif letter == ')': # 닫음 괄호와 열음 괄호 사이에 있는 연산자들 전부 반환
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.pop()

while stack:
    ans += stack.pop()
print(ans)
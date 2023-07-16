from collections import deque

formula = deque(input().split('-'))

answer = 0
fmla = formula.popleft()
answer = sum(map(int,fmla.split('+')))

while formula:
    fmla = formula.popleft()
    answer -= sum(map(int,fmla.split('+')))

print(answer)
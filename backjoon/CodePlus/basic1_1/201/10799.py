import sys
input = sys.stdin.readline

S = input()

output = 0
sticks = 0 
before = ""
for s in S:
    if s == "(":
        sticks += 1
        before = s
    else:
        sticks -= 1
        if before == "(":
            output += sticks
        else:
            output += 1
        before = s
        
print(output - 1)
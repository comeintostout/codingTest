import sys
FILE_NAME = "5.txt"
sys.stdin = open("in"+FILE_NAME,"rt")

inputString = input()

cnt = 0
pipes= 0
lastSt = ""
for st in inputString:
    if st == "(":
        pipes += 1
    elif st == ")" and lastSt == "(":
        pipes -= 1
        cnt += pipes
    else:
        pipes -= 1
        cnt += 1
    lastSt = st
print(cnt)
    
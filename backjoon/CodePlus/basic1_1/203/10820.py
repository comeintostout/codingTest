import sys
input = sys.stdin.readline

while True:
    number = 0
    alpabet = 0
    capital = 0
    space = 0   
    S = input()
    if S == "" or S == "\n":
        break
    for l in S:
        if ord(l) == ord(" "):
            space += 1
        elif ord(l) >= ord('a') and ord(l) <= ord('z'):
            alpabet += 1
        elif ord(l) >= ord('A') and ord(l) <= ord('Z'):
            capital += 1
        elif ord(l) >= ord('0') and ord(l) <= ord('9'):
            number += 1
    print(alpabet,capital,number,space)
        

moum = ['a','A','e','E','i','I','o','O','u','U']

while True:
    inputString = input()
    if inputString == "#":
        break
    cnt = 0
    for ch in inputString:
        if ch in moum:
            cnt += 1
    print(cnt)
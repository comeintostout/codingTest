S = input().rstrip()
output = ""

for l in S:
    if ord(l) >= ord('a') and ord(l) <= ord('z'):
        if ord(l) + 13 > ord('z'):
            output += chr(ord(l) - 13)
        else:
            output += chr(ord(l) + 13)
    elif ord(l) >= ord('A') and ord(l) <= ord('Z'):
        if ord(l) + 13 > ord('Z'):
            output += chr(ord(l) - 13)
        else:
            output += chr(ord(l) + 13)
    else:
        output += l
print(output)

import sys
input = sys.stdin.readline

S = list(map(lambda s:s.split('>')  ,input().strip().split('<')))

output = ""
for words in S:
    if len(words) > 1:
        output += "<" + words[0] + ">"
        tmp = list(map(lambda s: s[::-1],words[1].split()))
        tmpOutput = ""
        for wds in tmp:
            tmpOutput += wds + " "
        output += tmpOutput.strip()
    else:
        tmp = list(map(lambda s: s[::-1],words[0].split()))
        tmpOutput = ""
        for wds in tmp:
            tmpOutput += wds + " "
        output += tmpOutput.strip()

print(output)
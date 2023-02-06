S = input().rstrip()
ans = [0] * 26

for l in S:
    ans[ord(l) - 97] += 1

print(*ans)
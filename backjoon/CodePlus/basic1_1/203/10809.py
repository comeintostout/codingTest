S = input().rstrip()
ans = [-1] * 26

for i in range(len(S)):
    if ans[ord(S[i]) - 97] == -1:
        ans[ord(S[i]) - 97] = i

print(*ans)
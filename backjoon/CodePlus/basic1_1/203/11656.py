
S = input().rstrip()
ans = []

for i in range(len(S)):
    ans.append(S[i:])
ans.sort()
for j in ans:
    print(j)
N = int(input())
target = list(map(int,input().split()))

isChanged = 0
for j in range(N-1,0,-1):
    i = j-1
    if target[i] < target[j]:
        for k in range(N-1,i,-1):
            if target[k] > target[i]:
                tmp = target[i]
                target[i] = target[k]
                target[k] = tmp
                isChanged= 1
                break
        if isChanged:
            tmp = target[j:N]
            tmp.sort()
            for k in range(j,N):
                target[k] = tmp[k-j]
            break
if isChanged:
    target= list(map(str,target))
    print(" ".join(target))
else:
    print(-1)
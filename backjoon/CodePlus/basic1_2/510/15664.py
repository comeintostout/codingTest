N, M = map(int,input().split())
numbers= list(map(int,input().split()))
numbers.sort()

def dfs(pick,index):
    global numbers, M

    if len(pick) == M:
        print(" ".join(pick))
        return

    lastNumber= -1
    for idx in range(index, len(numbers)):
        if numbers[idx] == lastNumber:
            continue
        tmp = pick[:]
        tmp.append(str(numbers[idx]))
        dfs(tmp, idx+1)
        lastNumber=numbers[idx]

dfs([],0)
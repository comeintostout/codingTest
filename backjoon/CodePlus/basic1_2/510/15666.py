N, M = map(int,input().split())
numbers= list(set(list(map(int,input().split()))))
numbers.sort()

def dfs(pick):
    global numbers, M

    if len(pick) == M:
        print(" ".join(pick))
        return

    lastPick = int(pick[-1]) if pick else -1
    for num in numbers:
        if num >= lastPick:
            tmp = pick[:]
            tmp.append(str(num))
            dfs(tmp)

dfs([])
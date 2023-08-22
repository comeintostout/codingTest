N, M = map(int,input().split())
numbers= list(set(list(map(int,input().split()))))
numbers.sort()

def dfs(pick):
    global numbers, M
    if len(pick) == M:
        print(" ".join(pick))
        return

    for num in numbers:
        tmp = pick[:]
        tmp.append(str(num))
        dfs(tmp)        

dfs([])
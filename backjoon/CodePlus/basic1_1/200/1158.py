[N,K] = list(map(int,input().split()))

Yose = [i for i in range(1,N+1)]
deleted = []

idx = -1
while len(Yose) > 0:
    idx = (idx + (K % len(Yose))) % len(Yose)
    deleted.append(str(Yose.pop(idx)))
    idx = idx - 1 if idx > 0 else len(Yose) - 1

    
print("<" + ', '.join(deleted) + ">")

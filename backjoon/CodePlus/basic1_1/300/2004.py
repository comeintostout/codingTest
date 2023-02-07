[N,A] = map(int,input().rstrip().split())
B = N - A

def get5count(N,A, B):
    count5 = 0
    count2 = 0
    i = 5
    while i <= N:
        count5 += int(N/i)
        count5 -= int(A/i)
        count5 -= int(B/i)
        i *= 5
    j = 2
    while j <= N:
        count2 += int(N/j)
        count2 -= int(A/j)
        count2 -= int(B/j)
        j *= 2
        
    return min(count5,count2)

print(get5count(N,A,B))

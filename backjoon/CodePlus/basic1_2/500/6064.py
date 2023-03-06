import sys
input = sys.stdin.readline

TC = int(input())

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)
    
def lcm(a,b):
    return int(a * b / gcd(a,b))

for _ in range(TC):
    [M,N,X,Y] = map(int,input().rstrip().split())
    day = X
    endDay = lcm(M,N)

    while day <= endDay:
        if (day - 1)%N + 1 == Y:
            break
        day += M
    if day <= endDay:
        print(day)
    else:
        print(-1)

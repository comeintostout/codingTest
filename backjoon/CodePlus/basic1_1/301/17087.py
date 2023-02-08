import sys
input = sys.stdin.readline

[N,S] = map(int,input().rstrip().split())
deltaA = list(map(lambda a: abs(S- int(a)),input().rstrip().split()))

def gcd(a,b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)

while len(deltaA) > 1:
    tmp = []
    while len(deltaA) > 0:
        a = deltaA.pop()
        if len(deltaA) > 0:
            b = deltaA.pop()
            tmp.append(gcd(a,b))
        else:
            tmp.append(a)

    deltaA = tmp

print(deltaA[0])
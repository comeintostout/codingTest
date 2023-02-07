import sys
input = sys.stdin.readline

T = int(input().rstrip())

def gcd(num1, num2):
    if num1 % num2 == 0:
        return num2
    else:
        return gcd(num2, num1 % num2)

for _ in range(T):
    [A,B] = map(int, input().rstrip().split())
    gcdValue = gcd(A,B)
    print(round((A*B)/gcdValue))
    
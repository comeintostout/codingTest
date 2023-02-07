[A, B] = map(int,input().rstrip().split())

def gcd(num1, num2):
    if num1 % num2 == 0:
        return num2
    else:
        return gcd(num2, num1 % num2)

gcdValue = gcd(A,B)
lcmValue = round((A * B) / gcdValue)

print(gcdValue)
print(lcmValue)

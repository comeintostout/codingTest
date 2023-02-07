
[A,B,C] = list(map(int,input().rstrip().split()))

print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A * B)%C)
print(((A%C) * (B%C))%C)
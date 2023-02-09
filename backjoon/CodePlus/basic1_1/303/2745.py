[N,B] = input().rstrip().split()
B = int(B)

Value = dict()
for i in range(0,10):
    Value[str(i)] = i
for i in range(10,36):
    Value[chr(ord('A') + (i - 10))] = i

result = 0
jinsu = 1
for letter in N[::-1]:
    result += jinsu * Value[letter]
    jinsu *= B
print(result)
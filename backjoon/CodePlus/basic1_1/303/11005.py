[N,B] = map(int,input().rstrip().split())

Value = dict()
for i in range(0,10):
    Value[i] = str(i)
for i in range(10,36):
    Value[i] = chr(ord('A') + (i - 10))
    
output = ""
while N > 0:
    output += Value[N%B]
    N = int(N/B)
print(output[::-1])
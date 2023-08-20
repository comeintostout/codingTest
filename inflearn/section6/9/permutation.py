import sys
import itertools as it
sys.stdin = open("in1.txt","rt")

if __name__ == "__main__":
    N, F = map(int,input().split())
    b = [1]*N
    for i in range(1,N):
        b[i] = b[i-1]*(N-1)/i
    a = list(range(1,N+1))
    
    for tmp in it.permutations(a,3):
        print(tmp)
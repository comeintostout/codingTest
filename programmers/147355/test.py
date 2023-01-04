
def solution(t, p):
    answer = 0
    numP = int(p)
    for i in range(0,len(t)-len(p)+1):
        num = int(t[i:i+len(p)])
        if(numP >= num):
            answer += 1

    return answer

t = "10203"
p = "15"
print(solution(t,p))
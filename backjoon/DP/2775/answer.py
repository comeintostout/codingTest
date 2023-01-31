tc = int(input())
for i in range(tc):
    k = int(input())
    n = int(input())
    apart = [list(range(1,n+1))]
    for floor in range(1,k+1):
        peopleOnTheFloor = []
        for ho in range(1,n+1):
            peopleOnTheFloor.append(sum(apart[floor-1][:ho]))
        apart.append(peopleOnTheFloor)
    print(apart[k][n-1])





# 1 4 10
# 1 3 6
# 1 2 3 4 5 6 7 8

# k층의 n호
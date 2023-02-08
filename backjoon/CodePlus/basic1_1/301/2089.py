origin = int(input())

if origin == 0:
    print(0)
else:
    result = ""
    while origin != 1:
        if origin < 0:
            if origin % 2 == 1:
                origin = int(origin/-2) + 1
                result += "1"
            else:
                origin = int(origin/-2)
                result += "0"
        else:
            if origin % 2 == 1:
                result += "1"
            else:
                result += "0"
            origin = int(origin / -2)

    result += "1"
    print(result[::-1])
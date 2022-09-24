def solution():
    n = int(input())
    directions = list(input().split(" "))

    x = 1; y = 1

    for direction in directions:
        if direction == "R": x+=1
        elif direction == "L": x-=1
        elif direction == "U": y-=1
        elif direction == "D": y+=1

        if x > n: x = n
        if x < 1: x = 1
        if y > n: y = n
        if y < 1: y = 1

    return f'{y} {x}'

print(solution())
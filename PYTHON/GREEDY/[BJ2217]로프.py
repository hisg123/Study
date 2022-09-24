def solution():
    n = int(input())
    lopes = []

    for i in range(n):
        lopes.append(int(input()))
    lopes.sort()

    max_weight = 0
    for lope in lopes:
        if (max_weight < lope*n):
            max_weight = lope*n
        n -= 1

    return max_weight
print(solution())




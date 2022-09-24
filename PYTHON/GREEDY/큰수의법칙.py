def solution():
    sum = 0
    index = 0
    n, m, k = map(int, input().split(' '))
    numbers = list(map(int, input().split(' ')))
    numbers.sort(reverse=True)

    temp_k = k
    while m > 0:
        m-=1
        temp_k-=1
        if temp_k == 0:
            temp_k = k
            sum += numbers[index+1]
        else: sum += numbers[index]

    return sum

print(solution())
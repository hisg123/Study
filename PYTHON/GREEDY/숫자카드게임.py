def solution():
    m, n = map(int, input().split())
    numbers = []
    for i in range(m):
        numbers.append(min(list(map(int, input().split(" ")))))
    return max(numbers)

print(solution())
def solution():
    t = int(input())

    for i in range(t):
        n = int(input())
        cnt = 0
        scores = []
        for j in range(n):
            scores.append(list(map(int, input().split(" "))))
        print(scores)

    return cnt

print(solution())
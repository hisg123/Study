def solution(n, m, numbers):
    maxSum = 0
    numbers.sort(reverse=True)

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                numberSum = numbers[i]+ numbers[j] + numbers[k]
                if numberSum == m:
                    return numberSum
                elif maxSum < numberSum and numberSum < m:
                    maxSum = numberSum

    return maxSum

if __name__ == "__main__":
    n, m = map(int, input().split(" "))
    numbers = list(map(int, input().split(" ")))

    print(solution(n, m, numbers))
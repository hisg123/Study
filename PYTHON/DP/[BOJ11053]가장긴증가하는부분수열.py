def solution():
    n = int(input())
    array = list(set(list(map(int, input().split(" ")))))
    array.sort()
    return len(array)

if __name__ == "__main__":
    print(solution())
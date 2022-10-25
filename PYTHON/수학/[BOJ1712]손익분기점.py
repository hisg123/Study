def solution():
    a, b, c = map(int, input().split((" ")))
    if b >= c: n = -1
    else: n = a // (c-b) + 1
    return n

if __name__ == "__main__":
    print(solution())
def solution():
    n = int(input())
    i = 0
    index = 1
    while True:
        if "666" in str(i):
            if index == n:
                result = i
                break
            index += 1
        i+=1

    return result

if __name__ == "__main__":
    print(solution())
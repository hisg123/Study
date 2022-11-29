def solution():
    n = 1
    visited = list(range(1, 10002))

    while n <= 10000:
        created_number = n
        for i in str(n): created_number += int(i)
        if created_number in visited: visited.remove(created_number)
        n += 1

    return "\n".join(map(str, visited))

if __name__ == "__main__":
    print(solution())
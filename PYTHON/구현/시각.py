def solution():
    cnt = 0
    n = int(input())
    for hour in range(n+1):
        for min in range(60):
            for sec in range(60):
                if "3" in f"{hour}{min}{sec}":
                    cnt+=1

    return cnt

print(solution())
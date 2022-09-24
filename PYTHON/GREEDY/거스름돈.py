def solution(n):
    cnt = 0
    coins = [500, 100, 50, 10]

    for coin in coins:
        cur_cnt = n//coin
        cnt += cur_cnt
        n -= cur_cnt*coin
        if n == 0: break

    return cnt

print(solution(1260))
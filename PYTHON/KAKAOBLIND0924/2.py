def solution(cap, n, deliveries, pickups):
    answer = 0
    deliver_sum = 0
    pickup_sum = 0

    p = [ i for i in range(n)].sort(reverse=True)
    visited = []
    index = n-1

    while len(visited) < n:
        if index not in visited:
            deliver_sum += deliveries[index]
            pickup_sum += pickups[index]

        if deliver_sum > cap or pickup_sum > cap:
            deliver_sum -= deliveries[index]
            pickup_sum -= pickups[index]
        else:
            visited.append(index)

        index -= 1
        if index == 0:
            for i in p:

        print(deliver_sum, pickup_sum)

    return answer

cap = 4
n = 5
deliveries = [1, 0, 3, 1, 2]
pickups = [0, 3, 0, 4, 0]

print(solution(cap, n, deliveries, pickups))
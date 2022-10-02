def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


def solution(x, y, direction, map_info, d):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    count = 1
    turn_time = 0

    while True:
        turn_left()
        nx = x + dx[direction]
        ny = y + dy[direction]

        if d[nx][ny] == 0 and map_info[nx][ny] == 0:
            d[nx][ny] = 1
            x = nx
            y = ny
            count += 1
            turn_time = 0
            continue
        else:
            turn_time += 1

        if turn_time == 4:
            nx = x + dx[direction]
            ny = y - dy[direction]

            if map_info[nx][ny] == 0:
                x = nx
                y = ny
            else:
                break
            turn_time = 0

    return count

if __name__ == "__main__":
    n, m = map(int, input().split(" "))
    x, y, direction = map(int, input().split(" "))
    map_info = []
    d = [[0] * m for i in range(n)]

    for i in range(n):
        map_info.append(list(map(int, input().split(" "))))

    print(solution(x, y, direction, map_info, d))

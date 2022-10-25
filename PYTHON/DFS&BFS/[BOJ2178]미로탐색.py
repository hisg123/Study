n, m = map(int, input().split(" "))
miro = []
for i in range(n):
    miro.append(list(map(int, list(input()))))

visited = [[False for __ in range(m)] for _ in range(n)]

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if miro[x][y] == 1:
        visited[x][y] = True
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

def solution():
    for i in range(n):
        for j in range(m):
    return miro

if __name__ == "__main__":
    print(solution())
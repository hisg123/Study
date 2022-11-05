from collections import deque

def bfs(start, graph, visited):
    queue = deque([start])
    visited.append(start)

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if i not in visited:
                queue.append(i)
                visited.append(i)

    return visited


def solution():
    n, m = map(int, input().split(" "))
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b = map(int, input().split(" "))
        graph[a].append(b)
        graph[b].append(a)

    # print(graph)

    cnt = 0
    visited = []
    for v in range(1, n+1):
        if v in visited: continue
        visited = bfs(v, graph, visited)
        cnt += 1

    return cnt

if __name__ == "__main__":
    print(solution())
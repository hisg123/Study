from collections import deque
def bfs(graph, start, visited=[]):
    visited.append(start)
    queue = deque([start])

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if i not in visited:
                queue.append(i)
                visited.append(i)

    return visited

def dfs(graph, v, visited = []):
    visited.append(v)

    for i in graph[v]:
        if i not in visited:
            visited = dfs(graph, i, visited)
    return visited

def solution():
    n, m, v = map(int, input().split(" "))
    graph = [[] for _ in range(n+1)]
    for i in range(m):
        n1, n2 = map(int, input().split(" "))
        if n2 not in graph[n1]: graph[n1].append(n2)
        if n1 not in graph[n2]: graph[n2].append(n1)

    for i in range(len(graph)):
        graph[i].sort()

    print(" ".join([str(int) for int in dfs(graph, v)]))
    print(" ".join(str(int) for int in bfs(graph, v)))

solution()
from collections import deque
def bfs(graph, start, visited=[]):
    visited.append(start)
    queue = deque([start])
    cnt = 0

    while queue:
        v = queue.popleft()
        cnt += 1
        for i in graph[v]:
            if i not in visited:
                queue.append(i)
                visited.append(i)
    return cnt-1

def solution():
    n = int(input())
    link = int(input())
    graph = [[] for _ in range(n+1)]
    for i in range(1, link+1):
        a, b = map(int, input().split(" "))
        graph[a].append(b)
        graph[b].append(a)

    return bfs(graph, 1)

print(solution())
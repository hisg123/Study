from collections import deque

def myBFS(graph: list, root: int) -> list:
    queue = deque([root])
    visited = [root]

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not i in visited:
                visited.append(i)
                queue.append(i)

    return visited

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,4],
    [1,7]
]

print(myBFS(graph, 1))
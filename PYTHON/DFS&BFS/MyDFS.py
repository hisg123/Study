def MyDFS(graph, root):
    stack = [root]
    visited = [root]

    while stack:
        v = stack.pop()
        if v not in visited: visited.append(v)
        for i in graph[v]:
            if not i in visited:
                stack.append(i)
    return visited

n, m, v = map(int, input().split(" "))
graph = [[] for _ in range(n+1)]
for i in range(m):
    n1, n2 = map(int, input().split(" "))
    if n2 not in graph[n1]: graph[n1].append(n2)
    if n1 not in graph[n2]: graph[n2].append(n1)

for i in range(len(graph)):
    graph[i].sort(reverse=True)

print(graph)
print("".join(str(int) for int in MyDFS(graph, v)))
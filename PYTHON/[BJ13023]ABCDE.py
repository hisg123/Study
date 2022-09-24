from collections import defaultdict

def solution():
    graph, root = MakeGraph()
    return DFS(graph, root)

def MakeGraph():
    graph = defaultdict(set)
    M, N = input().split(" ")
    for i in range(int(N)):
        a, b = input().split(" ")
        if i == 0: root = a
        graph[a].add(b)
    return graph, root

def DFS(graph, root):

    for i in graph:

        visited = []
        stack = [i]

        while stack:
            if len(visited) == 5:
                return 1

            n = stack.pop()
            if n not in visited:
                visited.append(n)
                stack += graph[n] - set(visited)
                print(n, visited, stack, graph[n])
                if graph[n] == {}:
                    visited = [n]
    return 0

print(solution())

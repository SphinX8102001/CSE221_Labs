
import sys
sys.setrecursionlimit(200000)
N, M = map(int, input().split())
l_1 = list(map(int, input().split()))
l_2 = list(map(int, input().split()))

graph = [[] for _ in range(N + 1)]
for i in range(M):
    u, v = l_1[i], l_2[i]
    graph[u].append(v)
    graph[v].append(u)

checked = [False] * (N + 1)
order = []

def dfs(graph, node):
    checked[node] = True
    order.append(node)
    for neighbor in sorted(graph[node]):
        if not checked[neighbor]:
            dfs(graph, neighbor)
dfs(graph, 1)
print(*order)
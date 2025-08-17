
from collections import deque

N, M, S, D = map(int, input().split())
l_1 = list(map(int, input().split()))
l_2 = list(map(int, input().split()))

graph = [[] for _ in range(N + 1)]
for i in range(M):
    u, v = l_1[i], l_2[i]
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N + 1):
    graph[i].sort()

def bfs(graph, start_node, num_nodes):
    dist = [-1] * (num_nodes + 1)
    prev = [-1] * (num_nodes + 1)
    queue = deque([start_node])
    dist[start_node] = 0

    while queue:
        u = queue.popleft()

        for v in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                prev[v] = u
                queue.append(v)

    return dist, prev
dist, prev = bfs(graph, S, N)
if dist[D] == -1:
    print(-1)
if dist[D] != -1:
    path = []
    current_node = D
    while current_node != -1:
        path.append(current_node)
        current_node = prev[current_node]
    path.reverse()
    print(dist[D])
    print(*path)
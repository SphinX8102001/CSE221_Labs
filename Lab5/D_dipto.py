#D
from collections import deque

n, m, s, d, k = map(int, input().split())
a_list = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    a_list[u].append(v)

def bfs(a_list, start_node, num_nodes):
    dist = [-1] * (num_nodes + 1)
    pred = [-1] * (num_nodes + 1)
    queue = deque([start_node])
    dist[start_node] = 0

    while queue:
        u = queue.popleft()

        for v in a_list[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                pred[v] = u
                queue.append(v)

    return dist, pred
dist_s, pred_s = bfs(a_list, s, n)

if dist_s[k] == -1:
    print(-1)
else:
    dist_k, pred_k = bfs(a_list, k, n)
    if dist_k[d] == -1:
        print(-1)
    else:
        path_s_to_k = []
        current = k
        while current != -1:
            path_s_to_k.append(current)
            current = pred_s[current]
        path_s_to_k.reverse()

        path_k_to_d = []
        current = d
        while current != -1:
            path_k_to_d.append(current)
            current = pred_k[current]
        path_k_to_d.reverse()

        combined_path = path_s_to_k[:-1] + path_k_to_d
        total_length = dist_s[k] + dist_k[d]

        print(total_length)
        print(*combined_path)
from collections import deque
first_line = input().split()
n = int(first_line[0])
m = int(first_line[1])
S = int(first_line[2])
D = int(first_line[3])


adj = []
for i in range(n + 1):
    adj.append([])

if m > 0:
    u_line = input().split()
    v_line = input().split()
    for i in range(m):
        u = int(u_line[i])
        v = int(v_line[i])
        adj[u].append(v)
        adj[v].append(u)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result
for i in range(1, n + 1):
    if len(adj[i]) > 1:
        adj[i] = merge_sort(adj[i])

def bfs(start, end):
    dist = []
    parent = []
    for i in range(n + 1):
        dist.append(-1)
        parent.append(-1)

    q = deque()
    dist[start] = 0
    q.append(start)

    while len(q) > 0:
        u = q.popleft()
        if u == end:
            break
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                parent[v] = u
                q.append(v)

    return dist, parent

dist, parent = bfs(S, D)

if dist[D] == -1:
    print(-1)
else:
    print(dist[D])
    path = []
    cur = D
    length = 0
    while cur != -1:
        length += 1
        path.append(cur)
        cur = parent[cur]

    for i in range(length - 1, -1, -1):
        if i == 0:
            print(path[i])
        else:
            print(path[i], end=" ")
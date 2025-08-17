#gotta change variables before submitting
first_line = input().split()
n = int(first_line[0])
r = int(first_line[1])

adj = []
for i in range(n + 1):
    adj.append([])


for i in range(n - 1):
    edge = input().split()
    u = int(edge[0])
    v = int(edge[1])
    adj[u].append(v)
    adj[v].append(u)


subtree_size = [0] * (n + 1)


stack = [(r, -1, 0)]  
while stack:
    u, parent, state = stack.pop()
    if state == 0:
        stack.append((u, parent, 1)) 
        for v in adj[u]:
            if v != parent:
                stack.append((v, u, 0))
    else:
        size = 1
        for v in adj[u]:
            if v != parent:
                size += subtree_size[v]
        subtree_size[u] = size
q = int(input())
for i in range(q):
    x = int(input())
    print(subtree_size[x])
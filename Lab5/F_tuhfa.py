#gotta change variables before submitting 
from collections import deque
line1= input().split()
n = int(line1[0])
m = int(line1[1])
adj = []
for i in range(n + 1):
    adj.append([])
indegree=[0] * (n + 1)
for i in range(m):
    line2 = input().split()
    u = int(line2[0])
    v = int(line2[1])
    adj[u].append(v)
    indegree[v] += 1
q = deque()
for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)
count=0
while q:
    u = q.popleft()
    count += 1
    for v in adj[u]:
        indegree[v] -= 1
        if indegree[v] == 0:
            q.append(v)
if count == n:
    print("No")
else:
    print("Yes")

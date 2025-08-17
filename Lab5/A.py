import sys
def CreateNullAdjList(no_of_vertices,no_of_edges):
    null_adj_list = {}
    for i in range(no_of_vertices+1):
        null_adj_list[i] = []    
    return null_adj_list

def AddEdge(adj_list,v1,v2): 
    adj_list[v1].append(v2)
    adj_list[v2].append(v1)

def bfs(adj_list,source=1):
    n =len(adj_list)
    q = []
    visited = [False] * n
    visited[source] = True
    q.append(source)
    while len(q) != 0:
        curr = q.pop(0)
        print(curr, end=' ')
        for node in adj_list[(curr)]:
            if not visited[node]:
                visited[node] = True
                q.append(node)

def main():
    no_of_cities,no_of_roads = map(int, sys.stdin.readline().strip().split())
    adj_list = CreateNullAdjList(no_of_cities,no_of_roads)
    for i in range(no_of_roads):
        v1,v2 = map(int, sys.stdin.readline().strip().split())
        AddEdge(adj_list,v1,v2)
    bfs(adj_list, 1)
main()        
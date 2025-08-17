import sys
sys.setrecursionlimit(2*100000+5)

l_1 = []
l_2 = []
graph = []


def BuildGraph(l_1,l_2,no_of_edges):
    global graph
    for i in range(no_of_edges):
        v1 = l_1[i]
        v2 = l_2[i]
        graph[v1][v2] = 1
        graph[v2][v1] = 1

def dfs(adj_matrix, source = 1):
    n = len(adj_matrix)
    stack = []
    visited = [False] * n
    visited[source] = True
    stack.append(source)

    while len(stack)!=0:
        curr = stack.pop()
        print(curr, end=' ')
        for neighbor in range(n):
            if adj_matrix[curr][neighbor] == 1 and not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)
                

def main():
    N,M = map(int, sys.stdin.readline().strip().split()) 
    global graph,l_1, l_2
    graph = [[0]*(N+1) for _ in range(N+1)] 
    l_1 = list(map(int, sys.stdin.readline().strip().split()))
    l_2 = list(map(int, sys.stdin.readline().strip().split()))
    BuildGraph(l_1, l_2,M)
    dfs(graph)

main()    



    
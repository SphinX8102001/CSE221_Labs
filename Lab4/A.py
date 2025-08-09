import sys
def addEdge(graph,u ,v,weight): #Directed Weighted Edge(using adjancency matrix)
    graph[u][v] = weight

def createAdjMatrix(V): #NULL
    graph = [[0]*(V+1) for _ in range(V+1)]
    return graph

def printAdjMatrix(graph): #Prints the adjacency matrix
    for r in range(1,len(graph)):
        for c in range(1,len(graph)):
            print(graph[r][c], end=" ")
        print()

def main():
    v,e = map(int, sys.stdin.readline().strip().split())
    graph = createAdjMatrix(v)
    for i in range(e):
        u,v,weight = map(int, sys.stdin.readline().strip().split())
        addEdge(graph,u,v,weight)
    printAdjMatrix(graph)

main()
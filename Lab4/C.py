import sys
def create_null_adjacency_list(no_of_vertices):
    adj_list = {}
    for i in range(no_of_vertices):
        adj_list[i] = []
    return adj_list

def create_adjacency_list(no_of_vertices):
    null_adj_list = create_null_adjacency_list(no_of_vertices)
    for node in range(no_of_vertices):
        neighbors = sys.stdin.readline().strip().split()
        neighbors = list(map(int, neighbors))
        neighbors = neighbors[1:]
        for neighbor in neighbors:
            if neighbor not in null_adj_list[node]:
                null_adj_list[node].append(neighbor)
    adj_list = null_adj_list
    return adj_list
def createNullAdjMatrix(no_of_vertices):
    null_Adj_matrix = [[0]*no_of_vertices for _ in range(no_of_vertices)]
    return null_Adj_matrix
def AdjListToAdjMatrix(adj_list):
    no_of_vertices = len(adj_list)
    adj_matrix = createNullAdjMatrix(no_of_vertices)
    for i in range(no_of_vertices):
        for neighbor in adj_list[i]:
            adj_matrix[i][neighbor] = 1
    return adj_matrix
def printMatrix(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if c < len(matrix[r]) - 1:
                print(matrix[r][c], end=" ")
            else:
                print(matrix[r][c])
def main():        
    no_of_nodes = int(sys.stdin.readline().strip())
    adj_list = create_adjacency_list(no_of_nodes)
    adj_matrix = AdjListToAdjMatrix(adj_list)
    printMatrix(adj_matrix)

main()
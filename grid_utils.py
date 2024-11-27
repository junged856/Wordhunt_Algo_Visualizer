from Graph import Graph
from Trie import Trie

def generate_grid(grid):
    G = Graph()
    n = len(grid)
    
    # make nodes
    for i in range(n * n):
        row = i // n
        col = i % n
        G.add_node(i, grid[row][col])
            
    # create all edges
    for i in range(n * n):
        end_nodes = []
        row = i // n
        col = i % n
        
        if col != 0 and row != 3:
            end_nodes.append(i + n - 1)
        if col != 3:
            end_nodes.append(i + 1)
        if row != 3:
            end_nodes.append(i + n)
        if row != 3 and col != 3:
            end_nodes.append(i + n + 1)
            
        G.add_edges(i, end_nodes)
    
    G.set_dimensions((n, n))
    
    return G
        
def draw_grid(n, G):
    for i in range(n * n):
        row = i // n
        col = i % n
        node_val = G.get_node_val(i)
        print(node_val + " ", end='')
        if col == 3: 
            print("")
        
class Graph:
    def __init__(self):
        self.adj_list = {}
        self.node_vals = {}
    
    def add_node(self, id, val):
        if self.adj_list.get(id, None) != None:
            print('node already exists')
            return
        self.adj_list[id] = list()
        self.node_vals[id] = val
        return 
        
    def add_edge(self, node1, node2):
        if not (self.node_exists(node1) and self.node_exists(node2) and not self.is_neighbour(node1, node2)):
            return False
        
        self.adj_list[node1].append(node2)
        self.adj_list[node2].append(node1)
        
    def add_edges(self, start, nodes):
        for end in nodes:
            self.add_edge(start, end)
        return
            
    def get_node_val(self, node):
        return self.node_vals[node]
        
    def get_neighbours(self, node):
        return self.adj_list.get(node, False)
    
    def is_neighbour(self, node1, node2):
        if node2 in self.adj_list[node1] or node1 in self.adj_list[node2]:
            return True
        return False
    
    def node_exists(self, node):
        return self.adj_list.get(node, None) != None
    
    def print_graph(self):
        print(self.adj_list)
        print(self.node_vals)
        return
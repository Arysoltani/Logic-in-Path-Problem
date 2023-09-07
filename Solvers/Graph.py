class Graph:


    def __init__(self, number_nodes):
        self.number_nodes = number_nodes
        self.edge_list = []
    
    def add_edge(self, node1, node2):
        self.edge_list.append((node1, node2))
    
    def read_adj_matrix(self):
        for i in range(self.number_nodes):
            row = list(map(int, input().split()))
            for j in range(len(row)):
                if(row[j]):
                    self.add_edge(i, j)
    def __str__(self):
        print(f"number of nodes in graph is {self.number_nodes}")
        print(f"edges:")
        for edge in self.edge_list:
            print(edge)
        return ""
        
class Graph:
    def __init__(self, graph={}):
        self.graph = graph

    def show_vertices(self):
        return list(self.graph.keys())

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def show_edges(self):
        edges = []
        for first_vertex in self.graph:
            for second_vertex in self.graph[first_vertex]:
                if {second_vertex, first_vertex} not in edges:
                    edges.append({first_vertex, second_vertex})
        return edges

    def add_edge(self, edge):
        edge = set(edge)
        (first_vertex, second_vertex) = tuple(edge)
        if first_vertex in self.graph:
            self.graph[first_vertex].append(second_vertex)
        else:
            self.graph[first_vertex] = [second_vertex]

if __name__ == '__main__':

    graph1 = {
        'a': ['b', 'c'],
        'b': ['a', 'd'],
        'c': ['a', 'd'],
        'd': ['e'],
        'e': ['d']
    }

    graph = Graph(graph1)

    graph.add_edge(['g', 'a'])
    graph.add_vertex('f')
    print(graph.show_vertices())
    print(graph.show_edges())

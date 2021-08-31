from queue import Queue


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

def bfs_search(n, m, edges, s):

    adj_list = {}

    graph = Graph(adj_list)

    for i in edges:
        for j in i:
            if j not in adj_list:
                graph.add_vertex(j)

    all_nodes = list(range(1,n+1))
    for node in all_nodes:
        if node not in adj_list.keys():
            adj_list[node] = []

    for edge in edges:
        graph.add_edge(edge)

    visited = {}
    level = {}
    parent = {}
    bfs_output_list = []
    queue = Queue()

    for node in adj_list.keys():
        visited[node] = False
        parent[node] = None
        level[node] = -1

    visited[s] = True
    level[s] = 0
    queue.put(s)

    while not queue.empty():
        first_node = queue.get()
        bfs_output_list.append(first_node)
        for vertex in adj_list[first_node]:
            if not visited[vertex]:
                visited[vertex] = True
                parent[vertex] = first_node
                level[vertex] = level[first_node] + 6
                queue.put(vertex)

    output = []
    for node in sorted(adj_list.keys()):
        if node != s:
            output.append(level[node])
    print(output)
    print(adj_list)


if __name__ == '__main__':

    edges = [[1, 2], [1, 3], [3, 4]]

    bfs = bfs_search(n=5, m=3, edges=edges, s=1)

    bfs

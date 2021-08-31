from queue import Queue

class Vertex:
    def __init__(self, name=None, neighbours=[], isVisited=False, distance=9999):
        self.name = name
        self.neighbours = neighbours
        self.isVisited = isVisited
        self.distance = distance

    def add_neighbour(self, vertex):
        if vertex not in self.neighbours:
            self.neighbours.append(vertex)
            self.neighbours.sort()

class Graph:
    def __init__(self, graph={}):
        self.graph = graph

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, edge):
        edge = set(edge)
        (first_vertex, second_vertex) = tuple(edge)

        if first_vertex in self.graph:
            self.graph[first_vertex].append(second_vertex)
        else:
            self.graph[first_vertex] = [second_vertex]



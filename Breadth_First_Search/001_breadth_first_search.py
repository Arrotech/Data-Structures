from queue import Queue


def bfs_search(source_node, final_node, adj_list={}):
    visited = {}
    level = {}
    parent = {}
    bfs_output_list = []
    queue = Queue()

    for node in adj_list.keys():
        visited[node] = False
        parent[node] = None
        level[node] = -1

    visited[source_node] = True
    level[source_node] = 0
    queue.put(source_node)

    while not queue.empty():
        first_node = queue.get()
        bfs_output_list.append(first_node)
        for vertex in adj_list[first_node]:
            if not visited[vertex]:
                visited[vertex] = True
                parent[vertex] = first_node
                level[vertex] = level[first_node] + 1
                queue.put(vertex)

    print(bfs_output_list)
    print(level['g'])

    path = []
    while final_node is not None:
        path.append(final_node)
        final_node = parent[final_node]
    path.reverse()
    print(path)


if __name__ == '__main__':
    source_node = 'a'
    final_node = 'h'
    adj_list = {
        'a': ['b', 'd'],
        'b': ['a', 'c'],
        'c': ['b'],
        'd': ['a', 'e', 'f'],
        'e': ['d', 'f', 'g'],
        'f': ['d', 'e', 'h'],
        'g': ['e', 'h'],
        'h': ['g', 'f']
    }
    bfs = bfs_search(source_node, final_node, adj_list)

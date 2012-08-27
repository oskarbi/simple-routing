import sys

def min_node(nodes):
    """Return the node with the minimun weight from the list."""
    min_weight = sys.maxint
    min_weight_node = None
    for node in nodes:
        if node[1] < min_weight:
            min_weight = node[1]
            min_weight_node = node[0]
    return min_weight_node, min_weight

def dijkstra(graph, s, d):
    """Return the shortest path between two nodes in a graph and
    the distance between them.
    """
    distance = {}
    previous = {}
    for node in graph.get_stops():
        distance[node] = sys.maxint
        previous[node] = None

    distance[s] = 0
    queue = [(s, distance[s])]

    while queue:
        u, u_distance = min_node(queue) # Priorize the shortest paths found
        if u == d:
            break # We've reached the destination

        queue.remove((u, u_distance))

        for v in graph.get_stop(u).get_neighbors():
            if distance[v] > u_distance + graph.get_stop(u).get_distance(graph.get_stop(v)):
                distance[v] = u_distance + graph.get_stop(u).get_distance(graph.get_stop(v))
                previous[v] = u
                queue.append((v, distance[v]))

    # Build the list of nodes composing the path
    node = d
    path = []
    while node != s:
        path.append(node)
        node = previous[node]
    path.append(node)
    path.reverse()

    return path, distance[d]

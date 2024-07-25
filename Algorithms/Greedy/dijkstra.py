import sys


def dijkstra(graph, src):
    n = len(graph)  # Initialize the number of vertices in the graph.
    dist = [sys.maxsize] * n  # Initialize distances from src to all other vertices as INFINITE.
    dist[src] = 0
    visited = [False] * n

    # Loop through all vertices.
    for _ in range(n):
        # Select the minimum distance vertex from the set of vertices not yet processed.
        # u is always equal to src in the first iteration.
        u = min(range(n), key=lambda k: sys.maxsize if visited[k] else dist[k])
        # Mark the picked vertex as processed.
        visited[u] = True
        # Update dist value of the adjacent vertices of the picked vertex.
        for v, weight in enumerate(graph[u]):
            # Update dist[v] only if it is not in visited, there is an edge from u to v,
            # and total weight of path from src to v through u is smaller than current value of dist[v].
            if weight and not visited[v] and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight

    # Print the constructed distance array.
    print("Vertex\t\tdist from source vertex")
    for i in range(n):
        print(chr(65 + i), "\t\t\t", dist[i])


# Define a graph as a 2D array.
graph = [
    [0, 1, 2, 0, 0, 0],
    [1, 0, 0, 5, 1, 0],
    [2, 0, 0, 2, 3, 0],
    [0, 5, 2, 0, 2, 2],
    [0, 1, 3, 2, 0, 1],
    [0, 0, 0, 2, 1, 0]
]
# Call the dijkstra function with the graph and source vertex.
dijkstra(graph, 0)

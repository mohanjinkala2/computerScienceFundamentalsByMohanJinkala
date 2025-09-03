# Bellman-Ford Algorithm
    # 📝 Idea
        # Like Dijkstra, it finds shortest paths from a single source.
        # But unlike Dijkstra, it works even if the graph has negative edge weights.
        # Can also detect negative weight cycles.
    # 🔹 Steps
        # Initialize distances: dist[source] = 0, all others = ∞.
        # Repeat (V-1) times (where V = number of vertices):
        # For every edge (u, v, w) → if dist[u] + w < dist[v], update dist[v].
        # Run one more pass: if any distance can still be updated → there is a negative cycle.
def bellman_ford(nodes,edges,source):
    distance={node:float('inf') for node in nodes}
    distance[source]=0
    for _ in range(len(nodes)-1):
        for u,v,weight in edges:
            if distance[u]+weight<distance[v]:
                distance[v]=distance[u]+weight
                
    #Check for negative cycles
    for u, v, weight in edges:
        if distance[u] + weight < distance[v]:
            print("Graph contains a negative weight cycle!")
            return None
    return distance


vertices = ['A', 'B', 'C', 'D', 'E']
edges = [
    ('A', 'B', -1),
    ('A', 'C', 4),
    ('B', 'C', 3),
    ('B', 'D', 2),
    ('B', 'E', 2),
    ('D', 'B', 1),
    ('D', 'C', 5),
    ('E', 'D', -3)
]
print(bellman_ford(vertices, edges, 'A'))

                    
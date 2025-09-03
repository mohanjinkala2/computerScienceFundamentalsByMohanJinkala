# Floyd–Warshall Algorithm
    # 📝 What it does
        # A Dynamic Programming algorithm.->because we store length of path, when required we use them.
        # Finds the shortest path between every pair of vertices in a graph.
        # Works for directed / undirected, positive / negative edges.
        # ⚠️ But does not work if there’s a negative cycle (like Bellman-Ford).
    # 🔹 Idea
        # We keep a distance matrix dist where:
        # dist[i][j] = shortest distance from i to j.
        # Initially:
            # dist[i][j] = weight(i, j) if edge exists,
            # dist[i][j] = 0, if i==j,
            # otherwise ∞.
            # Then for each vertex k, check:
            # dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
            # Meaning:
            # “Is it shorter to go from i → j directly, or i → k → j?”
    #Summary:
        # Dijkstra → one source, positive edges.
        # Bellman-Ford → one source, negative edges allowed.
        # Floyd-Warshall → all pairs shortest paths.
from collections import defaultdict
def DistancesMatrix(edges,vertices):
    distances=[[0 if i==j else float('inf') for j in range(vertices)] for i in range(vertices)]
    for u,v,weight in edges:
        distances[u][v]=weight
    return distances
def  Floyd_Warshall_Algorithm(distances,vertices):
    for k in range(vertices):
        for i in range(vertices):
            for j in range(vertices):
                if distances[i][k]+distances[k][j]<distances[i][j]:#here try to move find path length from i->k->j and i-j campare them which is small.
                    distances[i][j]=distances[i][k]+distances[k][j]
    #for finding negative cycle present in graph or not.
    isCyclePresent=False
    for i in range(vertices):
        if distances[i][i]<0:
            isCyclePresent=True
    return distances,isCyclePresent
     
Matrix=DistancesMatrix([[0,1,3],[1,0,2],[0,3,5],[1,3,4],[3,2,2],[2,1,1]],4)
print(Floyd_Warshall_Algorithm(Matrix,4))
    
    
    
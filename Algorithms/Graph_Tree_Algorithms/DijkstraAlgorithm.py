# Dijkstra’s Algorithm (Shortest Path)
# 📝 Idea
    # Find the shortest path from a starting node to all other nodes in a weighted graph (with non-negative weights).
    # Uses a priority queue (min-heap) to always expand the nearest node first.
# 🔹 Steps
    # Start with a source node → distance = 0.
    # Set all other distances = ∞ (infinity).
    # Use a min-heap / priority queue to pick the node with the smallest distance.
    # Update distances to its neighbors if a shorter path is found.
    # Repeat until all nodes are visited.
import heapq
def buildGraph(edgesArray):
        graph={}
        for edge in edgesArray:
            if edge[0] not in graph:
                graph[edge[0]]=[[edge[1],edge[2]]]
            else:
                graph[edge[0]].append([edge[1],edge[2]])
            if edge[1] not in graph:
                graph[edge[1]]=[[edge[0],edge[2]]]
            else:
                graph[edge[1]].append([edge[0],edge[2]])
        return graph
def Dijkstra(edges,start):
    Graph=buildGraph(edges)
    Distances={}
    for node in Graph:
        Distances[node]=float('inf')
    array=[(0,start)]
    Distances[start]=0
    while array:
            currentDistance,node=heapq.heappop(array)
            if currentDistance>Distances[node]:
                continue
            for neighboor,weight in Graph[node]:
                Distance=currentDistance+weight
                if Distance<Distances[neighboor]:
                    Distances[neighboor]=Distance
                    heapq.heappush(array,(Distance,neighboor))
    print(Distances)           
Dijkstra([[0,1,2],[0,2,10],[1,3,11],[2,4,5],[1,4,6],[2,3,6],[3,5,7],[4,5,8]],0)
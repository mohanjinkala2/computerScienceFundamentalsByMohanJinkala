# Prim’s Algorithm is a greedy algorithm used to find the Minimum Spanning Tree (MST) of a connected, weighted, undirected graph.
# An MST is a subset of edges that connects all vertices with minimum total edge weight and contains no cycles.
# Steps of Prim’s Algorithm
    # Start from any arbitrary node.
    # Maintain two sets:
        # MST set (vertices already included).
        # Remaining vertices.
    # At each step:
        # Pick the edge with the minimum weight that connects a vertex in the MST set to a vertex outside it.
        # Add that edge and the new vertex to the MST set.
    # Repeat until all vertices are included.
import heapq
def Prims_Algorithm(vertices,graph):
    visit=[0]*vertices
    arr=[[0,0,-1]]#[weight,currentNode,currentNodeParent]
    costOfMinimumSpanningTree=0
    minimumSpanningTree=[]
    while arr:
        current=heapq.heappop(arr)
        if visit[current[1]]!=0:
            continue
        if current[2]!=-1:
            minimumSpanningTree.append([current[1],current[2]])
            costOfMinimumSpanningTree+=current[0]
        visit[current[1]]=1
        for neighboor,weight in graph[current[1]]:
            if visit[neighboor]==0:
                heapq.heappush(arr,[weight,neighboor,current[1]])
    print(minimumSpanningTree,costOfMinimumSpanningTree)
        
graph={0:[(1,2),(2,1)],1:[(0,2),(2,1)],2:[(1,1),(0,1),(4,2),(3,2)],4:[(2,2),(3,1)],3:[(2,2),(4,1)]}      
Prims_Algorithm(5,graph)
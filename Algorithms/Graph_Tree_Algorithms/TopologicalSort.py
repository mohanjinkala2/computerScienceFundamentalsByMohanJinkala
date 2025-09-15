# 🔹 Topological Sort
    # 📝 What it is
    # A linear ordering of vertices in a Directed Acyclic Graph (DAG)
    # Such that for every directed edge u → v, u comes before v in the ordering.
    # Example use cases:
    # Task scheduling (if task A must be done before task B).
    # Course prerequisites.
# ⚠️ Works only for DAGs (no cycles and also should not be unDirected).
# 🔹 Two Ways to Do It
    # DFS Method
        # Do DFS.
        # After visiting all neighbors, add the node to a stack.
        # Reverse the stack at the end → topological order.
    # Kahn’s Algorithm (BFS + Indegree)
        # Count in-degree (number of incoming edges) for each node.
        # Start with nodes having 0 in-degree.
        # Remove them and reduce in-degrees of their neighbors.
        # Keep picking nodes with in-degree = 0.
from collections import defaultdict,deque
def buildGraph(edgesArray):
        graph=defaultdict(list)
        for edge in edgesArray:
                graph[edge[0]].append(edge[1])
        return graph
def TopologicalSortByDfs(Graph,vertices):
        stack=[]
        has_cycle=[False]
        visit=[0 for i in range(vertices)]
        def dfs(vertice):
            if has_cycle[0]:
                return 
            visit[vertice]=1
            for neighboor in Graph[vertice]:
                if visit[neighboor]==0:
                    dfs(neighboor)
                elif visited[neighbor] == 1:# Found a back edge → Cycle detected
                    has_cycle[0] = True
                    return
            stack.append(vertice)
        for i in range(vertices):
            if visit[i]==0:
                dfs(i)
        return stack[::-1]
    
    
def TopologicalSortByBfs(Graph,vertices):
    indegree={i:0 for i in range(vertices)}
    for u in Graph:
        for v in Graph[u]:
            indegree[v]+=1
    queue=deque([vertice for vertice in indegree if indegree[vertice]==0])
    topoSort=[]
    while queue:
        u=queue.popleft()
        topoSort.append(u)
        for v in Graph[u]:
            indegree[v]-=1
            if indegree[v]==0:
                queue.append(v)
    if len(topoSort)!=vertices:# check for cycle
        print("Graph has a cycle, topological sort not possible!")
        return None
    return topoSort
Graph=buildGraph([[5,2],[5,0],[4,0],[4,1],[2,3],[3,1],[1,2]])
vertices=6
print(TopologicalSortByDfs(Graph,vertices),"*")
print(TopologicalSortByBfs(Graph,vertices),"**")

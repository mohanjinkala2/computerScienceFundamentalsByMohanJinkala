# What is DFS?->uses stack
# DFS = Depth First Search.
# It is used to traverse (visit) or search in graphs and trees.
# It goes deep into one path before trying other paths.
# 🔹 How it Works
    # Start from a node.
    # Visit it and mark as visited.
    # Go to one of its neighbors (unvisited).
    # Keep going deeper until no more new nodes.
    # Backtrack and try another path.
from collections import deque
def dfsOnGraph():
    visit=set()
    edges=[[1,2],[0,1],[2,3],[1,3]]
    def buildGraph(edgesArray):
        graph={}
        for edge in edgesArray:
            if edge[0] not in graph:
                graph[edge[0]]=[edge[1]]
            else:
                graph[edge[0]].append(edge[1])
            if edge[1] not in graph:
                graph[edge[1]]=[edge[0]]
            else:
                graph[edge[1]].append(edge[0])
        return graph
    Graph=buildGraph(edges)
    def dfs(node,Graph):
        visit.add(node)
        print(node,end=" ")
        for neighboor in Graph[node]:
            if neighboor not in visit:
                dfs(neighboor,Graph)
    dfs(0,Graph)
def dfsOnTree():
    def buildTree(nodeNeighboors):
            class Node():
                def __init__(self,val):
                    self.val=val
                    self.left=None
                    self.right=None
            pos=0
            root=Node(nodeNeighboors[pos])
            queue=deque([root])
            while queue:
                node=queue.popleft()
                pos+=1
                if nodeNeighboors[pos]!=None:
                    temp=Node(nodeNeighboors[pos])
                    node.left=temp
                    queue.append(temp)
                pos+=1
                if nodeNeighboors[pos]!=None:
                    temp=Node(nodeNeighboors[pos])
                    node.right=temp
                    queue.append(temp)
            return root
    root=buildTree([0,1,2,3,None,4,5,None,None,7,None,None,None,None,None])
    def dfs(temp):#This is preOrder like this we have Postoder and inOrder
        if temp==None:
            return
        print(temp.val,end=" ")
        dfs(temp.left)
        dfs(temp.right)
    dfs(root)
dfsOnTree()
        
        
    
            
        
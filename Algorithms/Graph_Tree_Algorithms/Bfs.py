# What is BFS?->uses queue
# BFS = Breadth First Search.
# It is used to traverse or search in graphs and trees.
# It goes level by level (or breadth-wise) instead of going deep.
# 🔹 How it Works
    # Start from a node.
    # Visit it and mark as visited.
    # Put it in a queue.
    # Take the front node from the queue. Visit all its unvisited neighbors and add them to the queue.
    # Repeat until queue is empty.
from collections import deque
def BfsOnGraph():
    visit=set()
    edges=[[1,2],[0,1],[2,3],[2,0]]
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
    def Bsf(temp):
        queue=deque([temp])
        visit.add(temp)
        BsfArray=[]
        while queue:
            levelNodes=[]
            for i in range(len(queue)):
                val=queue.popleft()
                levelNodes.append(val)
                for neighboor in Graph[val]:
                    if neighboor not in visit:
                        queue.append(neighboor)
                        visit.add(neighboor)
            BsfArray.append(levelNodes+[])
        print(BsfArray)
    Bsf(0)
    
def BfsOnTree():
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
    def bfs(temp):
        queue=deque([temp])
        bfsArray=[]
        while queue:
            levelNodes=[]
            for i in range(len(queue)):
                node=queue.popleft()
                levelNodes.append(node.val)
                if node.left!=None:
                    queue.append(node.left)
                if node.right!=None:
                    queue.append(node.right)
            bfsArray.append(levelNodes+[])
        print(bfsArray)
    bfs(root)
BfsOnGraph()
                
            

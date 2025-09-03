# let’s now cover Kruskal’s Algorithm, another classic greedy method for building a Minimum Spanning Tree (MST).
# It is quite different from Prim’s Algorithm: instead of growing the MST from one node, Kruskal’s sorts all edges and adds them one by one (if they don’t form a cycle).
# Steps of Kruskal’s Algorithm
    # Sort all edges of the graph in non-decreasing order of weight.
    # Initialize MST as empty.
    # Use a Disjoint Set Union (DSU / Union-Find) to detect cycles:
        # If adding an edge connects two previously disconnected components → add it to MST.
        # Otherwise, skip it (to avoid cycles).
    # Repeat until MST contains (V-1) edges.
class DisjointSetUnion():
    def __init__(self,vertices):
        self.rank=[0]*vertices
        self.size=[1]*vertices
        self.parent=[i for i in range(vertices)]
    def pathCompression(self,node):
        if self.parent[node]==node:
            return node
        self.parent[node]=self.pathCompression(self.parent[node])
        return  self.parent[node]
    def unionByRank(self,u,v):
        ultimateParentOfU=self.pathCompression(u)
        ultimateParentOfV=self.pathCompression(v)
        if ultimateParentOfU==ultimateParentOfV:
            return "This edge leads to cycle"
        if self.rank[ultimateParentOfU]==self.rank[ultimateParentOfV]:
            self.rank[ultimateParentOfV]+=1
            self.parent[ultimateParentOfU]=ultimateParentOfV
        elif self.rank[ultimateParentOfU]<self.rank[ultimateParentOfV]:
            self.parent[ultimateParentOfU]=ultimateParentOfV
        else:
            self.parent[ultimateParentOfV]=ultimateParentOfU
    def unionBySize(self,u,v):
        ultimateParentOfU=self.pathCompression(u)
        ultimateParentOfV=self.pathCompression(v)
        if ultimateParentOfU==ultimateParentOfV:
            return "This edge leads to cycle"
        elif self.size[ultimateParentOfU]<=self.size[ultimateParentOfV]:
            self.parent[ultimateParentOfU]=ultimateParentOfV
            self.size[ultimateParentOfV]+=self.size[ultimateParentOfU]
        else:
            self.parent[ultimateParentOfV]=ultimateParentOfU
            self.size[ultimateParentOfU]+=self.size[ultimateParentOfV]
    def find(self,u,v):
        ultimateParentOfU=self.pathCompression(u)
        ultimateParentOfV=self.pathCompression(v)
        if ultimateParentOfU==ultimateParentOfV:
            return False
        return True
def minimumSpanningTree(edges):
        edges.sort()
        minimumSpanningtree=[]
        costOfSpanningTree=0
        vertices=6
        start=0
        unionSet=DisjointSetUnion(vertices+1)#we added 1 because our graph is 1 based not 0 based
        while len(minimumSpanningtree)<vertices-1:
            weight,u,v=edges[start]
            if unionSet.find(u,v):#used to find if u,v are present in same component are not ,if they present we will not add,has it leads to cylce formation.
                unionSet.unionByRank(u,v)
                minimumSpanningtree.append([u,v])
                costOfSpanningTree+=weight
            start+=1
        print(minimumSpanningtree,costOfSpanningTree)
edges=[[1,1,4],[2,1,2],[9,5,4],[4,5,1],[5,4,3],[3,4,2],[3,3,2],[8,3,6],[7,6,2]]#[weight,u,v]        
minimumSpanningTree(edges)
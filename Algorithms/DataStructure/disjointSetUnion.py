# Union (Attach Two Sets)
# When we want to join two nodes u and v:
 # Find ultimate parents:
    # rootU = find(u)
    # rootV = find(v)
 # If rootU == rootV → already in the same set (no union needed).
 # Otherwise:
    # Compare rank/size of rootU and rootV.
    # Union by Rank:
        # Attach smaller rank tree under bigger rank tree.
        # If ranks are equal → choose one arbitrarily, and increase its rank by +1.
    # Union by Size (alternative):
        # Attach smaller size tree under bigger size tree.
        # Update size of new root.

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
            return True
        return False
vertices=6
edges=[[0,1],[0,5],[2,3],[5,1]]
unionSet=DisjointSetUnion(vertices)
for u,v in edges:
    unionSet.unionBySize(u,v)
print(unionSet.find(0,5),unionSet.size)            
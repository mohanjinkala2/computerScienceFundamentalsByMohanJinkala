#BIT is a 1 index based.
#it is used in sum in given range, frequency(Inversion Count in Array)etc
class FenwickTree:
    def __init__(self,bitArrayLength):
        self.bitArray=[0]*bitArrayLength
        
    def update(self,id,val):
        while id<len(self.bitArray):
            self.bitArray[id]+=val
            id+=(id&-id)
            
    def makeTree(self,arr):
        for i in range(1,len(arr)):
            self.update(i,arr[i])
            
    def findRangeSum(self,id):
        ans=0
        while id>0:
            ans+=self.bitArray[id]
            id-=(id&-id)
        return ans
arr=[1, 2, 1, 2, 1, 3]
tree=FenwickTree(len(arr)+1)
tree.makeTree([0]+arr)
print(tree.findRangeSum(4))
        
    
    
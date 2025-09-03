#we need to find number of elements on its right side greater then present element
#arr=[5,2,3,1]->[3,1,1,0]
#like this we can also find min, max on both sides
class FenwickTree:
    def __init__(self,bitArrayLength):
        self.bitArray=[0]*bitArrayLength
        
    def update(self,id,val):
        while id<len(self.bitArray):
            self.bitArray[id]+=val
            id+=(id&-id)
            
    def makeTree(self,arr):
        ans=[0]*len(arr)
        for element,elementIndex in arr:#arr=[[element,elementIndex]]
            if elementIndex==0:
                continue
            self.update(elementIndex,1)
            ans[elementIndex]=self.findRangeSum(len(arr)-1)-self.findRangeSum(elementIndex)
        return ans[1:]
                 
    def findRangeSum(self,id):
        ans=0
        while id>0:
            ans+=self.bitArray[id]
            id-=(id&-id)
        return ans
    
arr=[0,5,2,1,1,0] #Because Fenwick tree  is one based index
arr=[[arr[i],i] for i in range(len(arr))]
arr.sort()
print(arr)
tree=FenwickTree(len(arr))
print(tree.makeTree(arr))



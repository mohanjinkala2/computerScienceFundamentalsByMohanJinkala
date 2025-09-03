def normalSegmentTree():
        inputArray=[1,2,3,4,5,6,7,8]
        arr=[0]*(4*len(inputArray))
        def DfsSegmentTreeBuild(indexOfSegmentTree,left,right):
            if left==right:
                arr[indexOfSegmentTree]=inputArray[left]
                return 
            mid=(left+right)//2
            DfsSegmentTreeBuild(indexOfSegmentTree*2,left,mid)
            DfsSegmentTreeBuild(indexOfSegmentTree*2+1,mid+1,right)
            arr[indexOfSegmentTree]=arr[indexOfSegmentTree*2]+arr[indexOfSegmentTree*2+1] #or we can use max,min,xor and other  
            return arr[indexOfSegmentTree]
        def query(v,left,right,requiredleft,requiredright):
            if right<requiredleft or left>requiredright:
                return 0 #if it is max then return float('-inf'), if minimum then return float('inf'), for multiplication return 1
            if left>=requiredleft and right<=requiredright:
                return arr[v]
            mid=(left+right)//2
            x=query(2*v,left,mid,requiredleft,requiredright)
            y=query(2*v+1,mid+1,right,requiredleft,requiredright)
            return x+y
        def update(v,left,right,updateIndex,updateValue):
            if left>updateIndex or right<updateIndex:
                return 
            elif left==right==updateIndex:
                arr[v]=updateValue
                return
            mid=(left+right)//2
            update(2*v,left,mid,updateIndex,updateValue)
            update(2*v+1,mid+1,right,updateIndex,updateValue)
            arr[v]=arr[2*v]+arr[2*v+1] #if it maximum we use max(arr[2*v],arr[2*v+1]), foe minimum we use min(arr[2*v],arr[2*v+1]) 
        DfsSegmentTreeBuild(1,0,len(inputArray)-1)
        print(query(1,0,len(inputArray)-1,1,4))
        update(1,0,len(inputArray)-1,2,10)
        print(query(1,0,len(inputArray)-1,1,4))

def lazyPropogationSegmentTree():#it is used when we to update a range of elements with certain element example:[1,2,3,4,5]->from [1,4] add 10->[1,12,13,14,15]
    inputArray=[1,2,3,4,5,6,7,8]
    arr=[0]*(4*len(inputArray))
    checkForLazy=[False]*len(arr)
    lazyValue=[0]*len(arr)
    def DfsSegmentTreeBuild(indexOfSegmentTree,left,right):
            if left==right:
                arr[indexOfSegmentTree]=inputArray[left]
                return 
            mid=(left+right)//2
            DfsSegmentTreeBuild(indexOfSegmentTree*2,left,mid)
            DfsSegmentTreeBuild(indexOfSegmentTree*2+1,mid+1,right)
            arr[indexOfSegmentTree]=arr[indexOfSegmentTree*2]+arr[indexOfSegmentTree*2+1] #or we can use max,min,xor and other  
            return arr[indexOfSegmentTree]
    def apply(v,left,right,value):
        if left!=right:
            checkForLazy[v]=True 
            lazyValue[v]+=value
        arr[v]+=(right-left+1)*value
    def pushDown(v,left,right):
        if checkForLazy[v]==False:
            return 
        checkForLazy[v]=False
        apply(2*v,left,(left+right)//2,lazyValue[v])
        apply(2*v+1,(left+right)//2+1,right,lazyValue[v])
        lazyValue[v]=0
    def query(v,left,right,requiredleft,requiredright):
            if right<requiredleft or left>requiredright:
                return 0 #if it is max then return float('-inf'), if minimum then return float('inf'), for multiplication return 1
            if left>=requiredleft and right<=requiredright:
                return arr[v]
            pushDown(v,left,right)
            mid=(left+right)//2
            x=query(2*v,left,mid,requiredleft,requiredright)
            y=query(2*v+1,mid+1,right,requiredleft,requiredright)
            return x+y
    def update(v,left,right,updateIndexLeft,updateIndexRight,updateValue):
            if left>updateIndexRight or right<updateIndexLeft:
                return 
            elif left>=updateIndexLeft and right<=updateIndexRight:
                apply(v,left,right,updateValue)
                return
            pushDown(v,left,right)#if any lazy is present in this node it will be pushDown to child Node
            mid=(left+right)//2
            update(2*v,left,mid,updateIndexLeft,updateIndexRight,updateValue)
            update(2*v+1,mid+1,right,updateIndexLeft,updateIndexRight,updateValue)
            arr[v]=arr[2*v]+arr[2*v+1] #if it maximum we use max(arr[2*v],arr[2*v+1]), foe minimum we use min(arr[2*v],arr[2*v+1])
    DfsSegmentTreeBuild(1,0,len(inputArray)-1)
    print(arr)
    update(1,0,len(inputArray)-1,1,6,10)
    print(query(1,0,len(inputArray)-1,1,4))
    print(arr)
lazyPropogationSegmentTree()
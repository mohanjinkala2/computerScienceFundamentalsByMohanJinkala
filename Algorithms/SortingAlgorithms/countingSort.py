# Counting Sort in Simple Words
# Counting Sort is good when numbers are not too big (like marks out of 100, or ages).
# Instead of comparing numbers (like Quick/Merge), it counts how many times each number appears.
# Then it uses that count to build the sorted array.
arr=[2,1,1,5,3,4,8,7]
maxElement=max(arr)
countArray=[0]*(maxElement+1)
for i in arr:
    countArray[i]+=1
sortedArray=[]
for i in range(len(countArray)):
    sortedArray.extend([i]*countArray[i])
print(sortedArray)
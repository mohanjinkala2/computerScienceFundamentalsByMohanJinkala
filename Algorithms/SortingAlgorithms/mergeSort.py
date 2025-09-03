# Merge Sort Overview
# Merge Sort is a divide and conquer algorithm:
# Divide: Split the array into two halves until each subarray has only one element.
# Conquer: Recursively sort the subarrays.
# Combine (Merge): Merge the two sorted halves into a single sorted array.
arr=[2,1,4,8,3]
def MergeSort(a):
    if len(a)<=1:
        return a
    mid=len(a)//2
    leftArray=MergeSort(a[:mid])
    rightArray=MergeSort(a[mid:])
    
    #merge two sorted array's
    newArray=[]
    i=0
    j=0
    while i<len(leftArray) and j<len(rightArray):
        if leftArray[i]<rightArray[j]:
            newArray.append(leftArray[i])
            i+=1
        else:
            newArray.append(rightArray[j])
            j+=1
    while i<len(leftArray):
        newArray.append(leftArray[i])
        i+=1
    while j<len(rightArray):
        newArray.append(rightArray[j])
        j+=1
    return newArray
print(MergeSort(arr))
    
    
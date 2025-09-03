# Quick Sort Overview
# Quick Sort works by:
# Choosing a pivot element.
# Partitioning the array so that:
# All elements smaller than pivot go to the left.
# All elements greater than pivot go to the right.
# Recursively applying the same process to the left and right subarrays.
arr=[2,1,5,4,8,7]
def QuickSort(a):
    if len(a)<=1:
        return a
    pivotElement=a[0] #Take any element has pivot
    leftArray=[i for i in a[1:] if i<=pivotElement]
    rightArray=[i for i in a[1:] if i>pivotElement]
    return QuickSort(leftArray)+[pivotElement]+QuickSort(rightArray)
print(QuickSort(arr))
    
    
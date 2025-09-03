# Steps of Selection Sort
# Start with the first element (index i = 0).
# Find the minimum element in the remaining array (from i to n-1).
# Swap the found minimum element with the element at position i.
# Move i to the next index and repeat until the array is sorted.
arr=[3,5,2,8,6]
for i in range(len(arr)-1):
    min_index=i
    for j in range(i+1,len(arr)):
        if arr[j]<arr[min_index]:
            min_index=j
    arr[i],arr[min_index]=arr[min_index],arr[i]
print(arr)
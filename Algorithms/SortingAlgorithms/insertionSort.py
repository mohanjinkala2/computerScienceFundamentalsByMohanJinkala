# Insertion Sort Overview
# Insertion Sort works the way we often sort playing cards in our hands:
# Start with the second card (index 1).
# Compare it with the cards before it.
# Insert it into the correct position among the already sorted cards.
# Repeat for all cards.
arr=[2,1,4,3,8,5]
for i in range(1,len(arr)):
    key=arr[i]
    j=i-1
    while j>=0 and arr[j]>key:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=key
print(arr)
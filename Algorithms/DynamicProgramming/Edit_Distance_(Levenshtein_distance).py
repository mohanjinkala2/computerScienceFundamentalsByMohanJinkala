# 🔹 Problem
    # Given two strings word1 and word2, find the minimum number of operations required to convert word1 into word2.
    # Allowed operations are:
        # Insert a character
        # Delete a character
        # Replace a character
s1,s2= "intention", "execution"
dp=[[-1 for _ in range(len(s2))] for _ in range(len(s1))]
def editDistance(i,j):
    if i>=len(s1) and j>=len(s2):
        return 0
    if i>=len(s1) and j<len(s2):
        return len(s2)-j
    if i<len(s1) and j>=len(s2):
        return len(s1)-i
    if dp[i][j]!=-1:
        return dp[i][j]
    if s1[i]==s2[j]:
        dp[i][j]=editDistance(i+1,j+1)
    else:  
        x=1+editDistance(i,j+1) #insert      
        y=1+editDistance(i+1,j+1) #replace
        z=1+editDistance(i+1,j) #delect
        dp[i][j]=min(x,y,z)
    return dp[i][j]      
print(editDistance(0,0)) 
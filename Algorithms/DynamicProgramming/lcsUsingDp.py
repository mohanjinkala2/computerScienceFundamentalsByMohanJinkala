# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.
# Example 1:
    # Input: text1 = "abcde", text2 = "ace" 
    # Output: 3  
    # Explanation: The longest common subsequence is "ace" and its length is 3.
text1='abcde'
text2='ace'
dp=[[-1 for j in range(len(text2))] for i in range(len(text1))] #we can also use hashmap like dp={}
def lcsUsingMemoization(leftStringIndex,rightStringIndex):
    if leftStringIndex>=len(text1) or rightStringIndex>=len(text2):
        return 0
    if dp[leftStringIndex][rightStringIndex]!=-1:
        return dp[leftStringIndex][rightStringIndex]
    x,y,z=0,0,0
    if text1[leftStringIndex]==text2[rightStringIndex]:
        x=1+lcsUsingMemoization(leftStringIndex+1,rightStringIndex+1)
    y=lcsUsingMemoization(leftStringIndex,rightStringIndex+1)
    z=lcsUsingMemoization(leftStringIndex+1,rightStringIndex)
    dp[leftStringIndex][rightStringIndex]=max(x,y,z)
    return dp[leftStringIndex][rightStringIndex]
print(lcsUsingMemoization(0,0))
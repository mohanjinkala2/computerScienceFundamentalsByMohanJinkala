# 🔹 What is Partition DP?
    # It’s a DP technique used when:
    # We want to divide a sequence (array/string/matrix chain) into parts.
    # For each possible "cut" (partition), we recursively solve the subproblems and combine results.
    # We try all possible partitions and take the minimum/maximum.
# 🔹 Standard Partition DP Form
    # For a range [i…j]:
        # dp[i][j] = min( dp[i][k] + dp[k+1][j] + cost(i,k,j) )   for i ≤ k < j
    # dp[i][j] = best answer for subproblem from i to j
    # We loop through all cut points k to partition.
# 🔹 Classic Examples of Partition DP
    # Matrix Chain Multiplication (MCM)
    # (You just saw this — choose best split point k to minimize cost).
    # Palindrome Partitioning (minimum cuts to make string into palindromes).
    # Burst Balloons (Leetcode 312).
    # Boolean Parenthesization (count ways to parenthesize expression to make it true).
# When to Use Partition DP?
    # You should think of Partition DP if:
        #if there is many ways(pattern) of solving problem but we need to choice min or max.ex:mupltiply matrix's 1->a*(b*c) or 2->(a*b)*c here 1,2 are ways(patterns)
        # The problem asks for the best way to split a string/array into pieces.
        # The answer depends on trying all possible cuts.
        # Overlapping subproblems exist (same (i,j) will be recomputed many times if done naïvely).
        # Either:
        # You want the minimum/maximum value among partitions, OR
        # You want to generate all possible partitions.
# First we discuss MCM
MatrixArray=[10,20,30,40,50] #here there is len(MatrixArray)-1 number of matrix are there, Dimensions of this len(MatrixArray)-1 number of matrixs:[10,20], [20,30], [30,40], [40,50]
#we need to find the minimum number of multiplications required to multiply all this matrix. eg: [10,20]*[20,30] requires 10*20*30 multiplications
dp=[[float('inf') for _ in range(len(MatrixArray))] for _ in range(len(MatrixArray))]
def MCM(i,j):
    if i==j:
        return 0
    if dp[i][j]!=float('inf'):
        return dp[i][j]
    for k in range(i,j):
        dp[i][j]=min(dp[i][j],MCM(i,k)+MCM(k+1,j)+MatrixArray[i-1]*MatrixArray[k]*MatrixArray[j])
    return dp[i][j]
print(MCM(1,len(MatrixArray)-1))
    
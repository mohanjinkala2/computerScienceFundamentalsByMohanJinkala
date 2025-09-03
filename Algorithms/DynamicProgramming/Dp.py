# What is DP?
    # Dynamic Programming (DP) is a method to solve problems by breaking them into overlapping subproblems and storing their results to avoid recomputation.
    # It is usually applied when the problem has:
    # Overlapping subproblems (same subproblems solved multiple times).
    # Optimal substructure (optimal solution can be built from optimal solutions of subproblems).
# 🔹 Two Approaches in DP
    # Top-Down (Memoization)
        # Solve problem recursively.
        # Store results in a dictionary/array to reuse later.
    # Bottom-Up (Tabulation)
        # Build a table iteratively from smaller subproblems up to the final solution.
    
#Let's understand dp through Fibonacci numbers
def recursion(n):
    if n<=1:
        return n
    return recursion(n-1)+recursion(n-2)
dp={}
def Memoization(n):
    if n<=1:
        return n
    if n in dp:
        return dp[n]
    dp[n]=Memoization(n-1)+Memoization(n-2)
    return dp[n]
def Tabulation(n):
    dp=[0]*(n+1)
    dp[1]=1
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]
print(recursion(10))
print(Memoization(400))
print(Tabulation(4))
    
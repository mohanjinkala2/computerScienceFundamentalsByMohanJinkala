# 🎯 Problem: 0/1 Knapsack, we cannot solve 0/1 using greedy, it can only be solved by dp.
    # You are given:
        # n items where each item has a weight and a value.
        # A knapsack with capacity W.
# 👉 Find the maximum total value you can put in the knapsack without exceeding its capacity.
# Each item can either be taken (1) or not taken (0) — hence 0/1 Knapsack.
# Example
# Input:
#solving using pick and not pick
n = 3
W=50
weights = [10, 20, 30]
values  = [60, 100, 120]
dp=[[-1 for _ in range(W+1)] for _ in range(n)]
def dfs(i,w):
    if i>=n:
        return 0
    if dp[i][w]!=-1:
        return dp[i][w]
    x=0
    if w+weights[i]<=W:
       x=values[i]+dfs(i+1,w+weights[i])
    y=dfs(i+1,w)
    dp[i][w]=max(x,y)
    return dp[i][w]
print(dfs(0,0))
    
    
        
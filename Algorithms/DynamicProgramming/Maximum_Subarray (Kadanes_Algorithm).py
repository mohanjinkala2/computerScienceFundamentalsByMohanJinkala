def kadanes_Algorithm(arr):
    subArraySum=0
    max_sum=float('-inf')
    for i in range(len(arr)):
        subArraySum+=arr[i]
        max_sum=max(subArraySum,max_sum)
        if subArraySum<0:
            subArraySum=0
    return max_sum
def maxSubArray(nums):
        dp=[-1 for _ in range(len(nums))]
        def dfs(i):
            if i == 0:
                dp[i]=nums[i]
                return dp[i]
            if dp[i]!=-1:
                return dp[i]
            dp[i]=max(nums[i], nums[i] + dfs(i-1))
            return dp[i]
        return max(dfs(i) for i in range(len(nums)))
print(maxSubArray([-2,-3,4,-1,-2,1,5,-3]))
print(kadanes_Algorithm([-2,-3,4,-1,-2,1,5,-3]))
            
        
    
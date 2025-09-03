# Given an integer array nums, return the length of the longest strictly increasing subsequence.
# Example 1:
    # Input: nums = [10,9,2,5,3,7,101,18]
    # Output: 4
    # Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
nums=[10,9,2,5,3,7,101,18]
nums=[float('-inf')]+nums
dp=[[-1 for _ in range(len(nums))] for _ in range(len(nums))]
def lis(presentIndex,previousIndex):
    if presentIndex>=len(nums):
        return 0
    if dp[presentIndex][previousIndex]!=-1:
        return dp[presentIndex][previousIndex]
    x,y=0,0
    if nums[presentIndex]>nums[previousIndex]:
        x=1+lis(presentIndex+1,presentIndex)
    y=lis(presentIndex+1,previousIndex)
    dp[presentIndex][previousIndex]=max(x,y)
    return dp[presentIndex][previousIndex]
print(lis(1,0))
print(dp)
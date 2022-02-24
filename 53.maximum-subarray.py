#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [] # dp = the biggest answer 'include me'
        for i in range(len(nums)):
            if i == 0:
                dp.append(nums[i])
            else:
                bigger = max(nums[i], nums[i]+dp[i-1])
                dp.append(bigger)

        return max(dp)
        
# @lc code=end


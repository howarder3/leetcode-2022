#
# @lc app=leetcode id=217 lang=python
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # print(list(set(nums)))
        # print(len(set(nums)))
        return (len(set(nums)) != len(nums))

        
# @lc code=end


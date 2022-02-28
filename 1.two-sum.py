#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mydict = {}
        for idx in range(len(nums)):     
            # print(mydict.keys())       
            if nums[idx] in mydict.keys():
                return [mydict[nums[idx]], idx]
            else:
                mydict[target - nums[idx]] = idx
                
# @lc code=end


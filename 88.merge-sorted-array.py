#
# @lc app=leetcode id=88 lang=python
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        while (m > 0 and n > 0): 
            if(nums1[m-1] >= nums2[n-1]):
                nums1[m+n-1] = nums1[m-1] # put nums1[m] in to the last place of nums1
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        else:
            while n > 0: # m = 0
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            # else m > 0, already in nums1


       


        
# @lc code=end


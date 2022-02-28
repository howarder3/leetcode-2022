#
# @lc app=leetcode id=350 lang=python
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # print(set(nums1) & set(nums2))
        nums1, nums2 = sorted(nums1), sorted(nums2)
        res = []
        pt1, pt2 = 0, 0
        while(pt1 < len(nums1) and pt2 < len(nums2)):
            if nums1[pt1] > nums2[pt2]:
                pt2 += 1
            elif nums1[pt1] < nums2[pt2]:
                pt1 += 1
            else: # nums1[pt1] == nums2[pt2]
                res.append(nums1[pt1])
                pt1 += 1
                pt2 += 1
                
        return res


        
# @lc code=end


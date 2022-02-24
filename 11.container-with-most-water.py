#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l = 0 # index
        r = len(height)-1 # index
        width = len(height)-1
        while(width > 0 and l < r): # normal case
            area = width * min(height[r], height[l])
            # print(f"area = {area}, r = {r}, l = {l}") # debug
            max_area = max(max_area, area)
            

            # update
            if height[r] > height[l]: # l smaller
                l += 1
                width -= 1
            else:
                r -= 1
                width -= 1

        return max_area
        



        
# @lc code=end


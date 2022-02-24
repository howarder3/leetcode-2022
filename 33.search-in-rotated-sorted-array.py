#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l_idx , r_idx = 0, len(nums)-1
        
        while l_idx <= r_idx:
            mid_idx = (l_idx + r_idx)//2
            
            if nums[mid_idx] == target:
                return mid_idx
            
            # search left
            if nums[l_idx] <= nums[mid_idx]:
                if nums[l_idx] <= target and target < nums[mid_idx]: # ascending side
                    r_idx = mid_idx - 1
                else:
                    l_idx = mid_idx + 1

            # search right
            else: 
                if nums[mid_idx] < target and target <= nums[r_idx]: # ascending side
                    l_idx = mid_idx + 1
                else:
                    r_idx = mid_idx - 1


        return -1
        
# @lc code=end


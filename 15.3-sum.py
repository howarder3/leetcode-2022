#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        
        # decide target
        for i in range(len(nums)):
            if(i > 0 and nums[i-1] == nums[i]): # when same target, only calculate first 
                continue # go to next loop
            target = -nums[i]
            # print(f"i = {i}, target = {target}") # debug

            l = i+1
            r = len(nums)-1

            while(l < r and l < len(nums) and r >= 0): # normal condition
                # print(f"l = {l}, r = {r}") # debug
                if nums[l] + nums[r] == target:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]: # when same value, only calculate first
                        l += 1 
                elif nums[l] + nums[r] > target: # need smaller, r - 1
                    r -= 1                  
                else: # nums[l] + nums[r] < target: need bigger, l + 1
                    l += 1        

        return ans


# @lc code=end


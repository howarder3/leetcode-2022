#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            ans = 0
        else:
            ans = 0
            queue_list = []
            l = 0 # left pointer

            for r in range(len(s)): # s[r], get one new word
                # found duplicate in sliding window, remove until duplicate not found
                while s[r] in queue_list: 
                    queue_list.pop(0)
                    l += 1
                # not found or all duplicate removed, push new word s[r]
                queue_list.append(s[r]) 
                # update answer
                ans = max(ans, r-l+1)     
        return ans
        
# @lc code=end


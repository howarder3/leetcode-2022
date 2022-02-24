#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mylist = [word for word in s]
        # print(mylist)

        idx = 0
        if len(s) != len(t):
            return False

        while(mylist):
            if t[idx] not in mylist:
                return False

            if t[idx] in mylist:
                mylist.remove(t[idx])
                idx += 1
           

        return True

        
# @lc code=end


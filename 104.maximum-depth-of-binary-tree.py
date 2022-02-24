#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        depth = 0
        if root:
            level = [root]
        else:
            level = []

        while(level):
            depth += 1
            next_level = []
            for ele in level:
                if ele.left:
                    next_level.append(ele.left)
                if ele.right:
                    next_level.append(ele.right)
            
            level = next_level 
        
        return depth
        
# @lc code=end


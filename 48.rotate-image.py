#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix) # one side

        # transpose
        for i in range(N):
            for j in range(i+1, N):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp
        # print(f"{matrix}") #dubug

        # right and left reverse
        for i in range(N):
            for j in range(N//2):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[i][-j+(N-1)]
                matrix[i][-j+(N-1)] = tmp
        
# @lc code=end


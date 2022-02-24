/*
 * @lc app=leetcode id=217 lang=cpp
 *
 * [217] Contains Duplicate
 */

// @lc code=start
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        // unordered_set set
        // Hash table | RB-tree
        // | (ordered)
        // insert and search fast O(1) | search fast only when data less
        // memory use more | memory use less
        // set: ordered, print as ascend, need know n-1...
        // unordered: no-sort needed, single lookup, only insert, delete, search
        set<int> s(nums.begin(), nums.end());
        // for(auto it = s.begin(); it != s.end(); it++)
        //     cout << *it << endl;
        return nums.size() != s.size();
    }
};
// @lc code=end


/*
 * @lc app=leetcode id=53 lang=cpp
 *
 * [53] Maximum Subarray
 */

// @lc code=start
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        vector<int> dp;
        for(int i=0; i< nums.size(); i++){
            if(i == 0){
                dp.push_back(nums[i]); // record 'include me' biggest
            }
            else{
                dp.push_back((nums[i] > nums[i]+dp[i-1]) ? nums[i] : nums[i]+dp[i-1]); // record 'include me' biggest
            }
        }      
        auto it = std::max_element(dp.begin(), dp.end());  
        // std::vector<int>::iterator it;
        // cout << *it << endl;

        // int max_value = *std::max_element(dp.begin(), dp.end());
        // cout << max_value << endl;

        return *it;
    }
};
// @lc code=end


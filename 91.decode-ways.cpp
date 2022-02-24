/*
 * @lc app=leetcode id=91 lang=cpp
 *
 * [91] Decode Ways
 */

// @lc code=start
class Solution {
public:
    int numDecodings(string s) {
        // dp
        int n = s.size();
        if(n <= 0){
            return 0;
        }
        vector<int> dp(n+1);
        dp[n] = 1; // ..... 1
        for(int i=n-1; i>=0 ; i--){
            if(s[i] == '0'){ // invalid case
                dp[i] = 0;
                continue;
            }  
            // default
            dp[i] = dp[i+1];
            
            // if special case
            int num = stoi(s.substr(i, 2)); // count 2
            // cout << num << endl;
            if( 10 <= num && num <= 26 ){
                dp[i] = dp[i+1] + dp[i+2];
            }
        }

        // for(int i=0; i<n+1; i++)
        //     cout << dp[i] << " ";
        return dp[0];
    }
            // cout << s.length() << endl;
    //     int len = s.length();
    //     if(len <= 0){
    //         return 0;
    //     }
    //     if(s[0] == '0') // invalid start "0"=int, '0'=string
    //         return 0;
    //     if(len == 1){
    //         cout << stoi(s) << endl;
    //         return 1;
    //     }
    //     else{
    //         string sub_str = s.substr(0, 2);
    //         cout << "stoi = "<< stoi(sub_str) << endl;

    //         if(10 <= stoi(sub_str) && stoi(sub_str) <= 26){
    //             // go 1, 2 step next 
    //             // cout << "stoi pass" << endl;
    //             if(numDecodings(s.substr(2, s.length())) <= 0)
    //                 return numDecodings(s.substr(1, s.length())) + 1; 
    //             else
    //                 return numDecodings(s.substr(1, s.length())) + numDecodings(s.substr(2, s.length())); 
    //         }
    //         else{
    //             // cout << "stoi failed" << endl;
    //             // go 1 step next
    //             return numDecodings(s.substr(1, s.length())); 
    //         }
    //     }
    // }
};
// @lc code=end


/*
 * @lc app=leetcode id=2 lang=cpp
 *
 * [2] Add Two Numbers
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *res = new ListNode(0); // 0 -> 
        ListNode *p = res; // res 'pointer value', think &res if move simultaneously
        int carry = 0, value;

        while(1){
            if(l1 && l2){ // both remain
                value = l1->val + l2->val + carry;
                if(value >= 10){
                    carry = 1;
                    value = value - 10;
                }
                else{
                    carry = 0;
                }
                cout << value << endl;
                p->next = new ListNode(value);
                p = p->next;
                l1 = l1-> next;
                l2 = l2-> next;
            } 
            else if(l1){ // remain l1
                value = l1->val + carry;
                if(value >= 10){
                    carry = 1;
                    value = value - 10;
                }
                else{
                    carry = 0;
                }
                cout << value << endl;
                p->next = new ListNode(value);
                p = p->next;
                l1 = l1-> next;
            }
            else if(l2){ // remain l2
                value = l2->val + carry;
                if(value >= 10){
                    carry = 1;
                    value = value - 10;
                }
                else{
                    carry = 0;
                }
                cout << value << endl;
                p->next = new ListNode(value);
                p = p->next;
                l2 = l2-> next;
            }
            else{ // no remain
                if(carry == 1){
                    p->next = new ListNode(1);
                    p = p->next;
                }
                break;
            }
        }
        return res->next;
    }
};
// @lc code=end


#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        back = front = head
        for _ in range(n):
            front = front.next

        if not front:
            return head.next

        while(front.next):
            front, back = front.next, back.next

        # print(back.val)
        back.next = back.next.next
        return head

        
# @lc code=end


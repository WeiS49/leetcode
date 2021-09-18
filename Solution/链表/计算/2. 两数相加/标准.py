#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        listx = ListNode(0)
        guard = listx
        tmp = 0
        while l1 or l2 or tmp:
            if l1:
                tmp += l1.val
                l1 = l1.next
            if l2:
                tmp += l2.val
                l2 = l2.next
            listx.next = ListNode(tmp % 10)
            listx = listx.next
            tmp //= 10

        return guard.next

# @lc code=end


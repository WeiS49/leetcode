#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # dicx = {}
        listx = []
        while head:
            if head in listx:
            # if dicx.get(head):
                return True
            # dicx[head] = 1
            listx.append(head)
            head = head.next
        return False
# @lc code=end


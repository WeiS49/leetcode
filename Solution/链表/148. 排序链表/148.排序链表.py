#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        left_end = self.findMid(head)
        mid = left_end.next
        left_end.next= None
        left, right = self.sortList(head), self.sortList(mid)
        return self.merge(left, right)

    def findMid(self, node):
        if not node or not node.next: return node
        slow, fast = node, node.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge(self, left, right):
        guard = ListNode(0)
        pre = guard
        while left and right:
            if left.val < right.val:
                pre.next = left
                left = left.next
            else:
                pre.next = right
                right = right.next
            pre = pre.next
        pre.next = left if left else right
        return guard.next



# @lc code=end


#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# [21] 合并两个有序链表
# Time: O(n) Space: O(1)
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        guard = ListNode(0)
        pre = guard
        # 这里的关系应该是 && 而不是 || 
        # 因为当其中一方为空时, 直接连接另一方即可'
        # 如果用 || , 可能会对NoneType使用.val, 产生错误
        while l1 and l2:
            v1, v2 = l1.val, l2.val
            if v1 < v2:
                pre.next = l1
                l1 = l1.next
            elif v1 >= v2:
                pre.next = l2
                l2 = l2.next

            pre = pre.next
        pre.next = l1 if not l2 else l2
        return guard.next





# @lc code=end


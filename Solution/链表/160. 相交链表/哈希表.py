#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        hashMap = {}
        while headA:
            hashMap[headA] = True
            headA = headA.next
        while headB:
            if headB in hashMap.keys():
                return headB
            headB = headB.next
        return
# @lc code=end


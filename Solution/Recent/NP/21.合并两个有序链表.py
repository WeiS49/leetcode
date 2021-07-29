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
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        prehead = ListNode(0)
        pre = prehead
        while l1 and l2:
            if l1.val > l2.val:
                pre.next = l2
                l2 = l2.next

            else:
                pre.next = l1
                l1 = l1.next
            pre = pre.next # 需要更新'临时节点'的位置, 始终指向链表中最后一个节点

        pre.next = l1 if l1 is not None else l2 # 如果某一链表为空, 则直接指向剩下的内容即可
        return prehead.next

        # prehead = None
        # while l1 and l2:
        #     if l1.val > l2.val:
        #         temp = l2.next
        #         l2.next = prehead
        #         prehead = l2
        #         l2 = temp
        #     else:
        #         temp = l1.next
        #         l1.next = prehead
        #         prehead = l1
        #         l1 = temp
        # while l1:
        #     temp = l1.next
        #     l1.next = prehead
        #     prehead = l1
        #     l1 = temp
        # while l2:
        #     temp = l2.next
        #     l2.next = prehead
        #     prehead = l2
        #     l2 = temp
        # return prehead

# @lc code=end


#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 直接一次性移动到末尾

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        prehead = ListNode(0)
        prehead.next = head
        prev = prehead # 头结点的前一个结点
        cur = head # 当前节点

        while True:
            if not cur or not cur.next: # 确定当前节点和下一节点为非空
                break

            # 因为是循环, 所以需要做额外判定 - 判断下一节点为非空
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            
            if prev.next != cur:
                prev.next = cur.next
            else:
                prev = prev.next
            cur = cur.next

        return prehead.next


        # prehead = ListNode(0)
        # prehead.next = head
        # prev = prehead
        # # prev = head # 当前节点的上一个节点
        # cur = head # 当前节点

        # while True:
        #     if not cur or not cur.next:
        #         break

        #     while cur.next and cur.val == cur.next.val:
        #         cur = cur.next

        #     if prev.next == cur:
        #         prev = prev.next
        #     else:
        #         prev.next = cur.next

        #     cur = cur.next

        # return prehead.next


# @lc code=end


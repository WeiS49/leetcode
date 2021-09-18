#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# [86] 分隔链表
# 创建额外链表, 分别保存更大的值和更小的值
# 最后将链表进行拼接

# Time: O(n) Space: O(n)

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # 创建两个链表, 分别保存比x小的值和比x大的值
        less, more = ListNode(0), ListNode(0)
        # 创建哨兵节点, 保存新链表的初始状态
        q, p = less, more 
        while head:
            if head.val < x:
                less.next = head
                less = less.next
            else:
                more.next = head
                more = more.next
            head = head.next # 注意head指针
        # 合并两个链表
        more.next = None 
        less.next = p.next
        return q.next


# @lc code=end


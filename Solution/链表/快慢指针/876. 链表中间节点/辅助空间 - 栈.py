#
# @lc app=leetcode.cn id=876 lang=python3
#
# [876] 链表的中间结点

# 用一个栈保存链表中的节点, 
# 似乎还可以用快慢指针: 当快指针到终点, 慢指针(附近)正好就是目标节点
# Time: O(n)
# Space: O(n)

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time:
# Space:

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        listx = []
        while head:
            listx.append(head)
            head = head.next

        length = len(listx)
        return listx[length//2]

# @lc code=end


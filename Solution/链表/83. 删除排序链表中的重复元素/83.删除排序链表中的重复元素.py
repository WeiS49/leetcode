#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 基本解法: 单次循环, 遇到如果下个节点与当前节点一致, 跳过它
# 时间复杂度: 单次循环, O(n)
# 空间复杂度: 使用空间为常量, O(1)


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: # 排除特殊情况
            return
        cur = head # 最重要返回head值(整个链表), 所以单独声明临时变量并进行操作
        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return head




# @lc code=end


#
# @lc app=leetcode.cn id=445 lang=python3
#
# [445] 两数相加 II
# 时间复杂度: 单层循环, O(n)
# 空间复杂度: 两个列表, 每个列表的数据是n个, O(2n) -> O(n)

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val) # 变量写错了
            l2 = l2.next
        ans = None
        carry = 0
        while s1 or s2 or carry: # carry位的条件
            a = 0 if not s1 else s1.pop()
            b = 0 if not s2 else s2.pop()
            cur = a + b + carry  # 不要忘了加进位
            carry = cur // 10
            cur %= 10
            current_node = ListNode(cur)
            current_node.next = ans
            ans = current_node

        return ans

# @lc code=end


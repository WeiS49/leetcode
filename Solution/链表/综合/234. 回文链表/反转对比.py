#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表



# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 追求空间复杂度O(1)的解法, 多了一些代码, 但多出来的都属于模板, 应该记住
# 时间复杂度: 单层循环, O(n);  时间复杂度: 只是用常量空间, O(1)
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        first_half = self.halfNode(head)
        second_half = self.reverseNode(first_half.next)

        first = head
        second = second_half
        result = True
        while True:
            if not result or not second:
                break
            if first.val != second.val:
                result = False
            first = first.next
            second = second.next
        return result

    def reverseNode(self, head):
        prev = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev

    def halfNode(self, head):
        slow, fast = head, head

        while True:
            if not fast or not fast.next or not fast.next.next:
                break
            fast = fast.next.next
            slow = slow.next

        return slow
























    #     if head is None: # 排除特殊情况
    #         return True 
        
    #     first_half_end = self.half_node(head)
    #     second_half_start = self.reverse_node(first_half_end.next)
    #     result = True
    #     first = head
    #     second = second_half_start

    #     while result and second is not None: # 总是后半段先结束
    #         if first.val != second.val:
    #             result = False
    #         first = first.next
    #         second = second.next
    #     return result

    # def half_node(self, head): # 这是寻找链表中间位置的模板, 写熟练
    #     slow = head
    #     fast = head
    #     while fast.next and fast.next.next: # 快指针总是先到终点, 所以条件不需要写slow.next
    #         fast = fast.next.next
    #         slow = slow.next
    #     return slow

    # # 如果是输入长度是奇数 - 二者一样长, 偶数 - 后半段短
    # def reverse_node(self, head): # 这是反转链表的模板, 写熟练
    #     previous = None
    #     cur = head
    #     while cur:
    #         next_node = cur.next
    #         cur.next = previous
    #         previous = cur
    #         cur = next_node
    #     return previous
# @lc code=end

    # def reverse_node(self, start):
    #     previous = None
    #     cur = start
    #     return cur
    #     while start:
    #         temp = start
    #         # temp = start.next
    #         start.next = previous
    #         previous = start
    #         start = temp.next
    #         # start = temp
    #     # return start
    #     # return previous

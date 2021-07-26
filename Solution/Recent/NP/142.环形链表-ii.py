#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II

# 双指针解法, 后续需要增补哈希表解法
# 时间复杂度: 单次循环(不涉及嵌套), O(n)
# 空间复杂度: 维护了两个指针, 没有额外的辅助空间, O(1)

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while True:
            if not fast or not fast.next: return    # 直接在这里写快指针的终止条件(二者中有任意一个不存在)
            # if not (fast and fast.next): return    # 两种写法等效
            slow, fast = slow.next, fast.next.next
            # if fast or fast.next == None: return None
            if fast == slow: break
        fast = head # 直接将快指针置回原点
        while fast != slow: # 若二者再次相遇, 此时的位置即为环的入口(需要走的步数一致)
            slow = slow.next
            fast = fast.next
        return fast

# @lc code=end


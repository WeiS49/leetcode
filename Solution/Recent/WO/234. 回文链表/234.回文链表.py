#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表

# 先想办法将链表值添加进数组中, 对数组使用双指针操作
# 时间复杂度: 单层循环, 不涉及嵌套, O(n)
# 空间复杂度: 涉及在循环中添加链表元素, O(n)


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        nums = []
        cur = head
        while cur:
            nums.append(cur.val) # 将链表值添加进数组中
            cur = cur.next

        start = 0
        end = len(nums) - 1
        while start <= end: # 使用双指针, 分别指向首尾, 对比是否相等
            if nums[start] != nums[end]: # 在if语句中处理简单情况, 剩下的用else解决
                return False
            else: # 指针移动
                start += 1
                end -= 1
        return True
        # return nums == nums[::-1] # 利用Python语言特性的解法, 免去了第二个while循环

        
# @lc code=end


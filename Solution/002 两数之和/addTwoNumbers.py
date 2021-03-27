class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        listx = ListNode()
        guard = listx
        tmp = 0

        while l1 or l2 or tmp:
            v1 = v2 = 0
            if l1:
                v1 += l1.val
                l1 = l1.next

            if l2:
                v2 += l2.val
                l2 = l2.next
            
            tmp, val = divmod(v1 + v2 + tmp, 10)
            listx.next = ListNode(val)
            listx = listx.next

        return guard.next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 根据题意, 首先要创建新链表
        listx = ListNode()
        # 创建烧饼节点(返回值)
        guard = listx
        # 设置进位值
        tmp = 0
        while l1 or l2 or tmp:
            if l1:
                tmp += l1.val
                l1 = l1.next # 指向下一位

            if l2:
                tmp += l2.val
                l2 = l2.next

            listx.next = ListNode(tmp % 10)
            tmp = tmp // 10
            listx = listx.next

        return guard.next
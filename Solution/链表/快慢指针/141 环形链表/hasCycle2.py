
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        if head == None:        # 解决空链表的情况
            return False

        slow = head
        fast = head.next

        # 分别解决: 链表中两个值的情况, 三个值的情况
        while fast != None and fast.next != None:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next

        return False

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True

        except:
            return False





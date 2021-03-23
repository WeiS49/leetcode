
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        if not head:
            return False
        
        if head.val == 0:
            return True

        head.val = 0
        return self.hasCycle(head.next)




class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        s = set()   # 声明一个集合(不允许重复)

        while head:
            
            if head in s:   # 若出现重复项
                return True # 说明存在环
            
            s.add(head) # 每次循环都将当前节点存入集合
            head = head.next    # 指针后移

        return False

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        hashmap = {}

        while head:
            if hashmap.get(head, 0) != 0:   # 找不到, 默认返回0
                return True
            else:
                hashmap[head] = 1
            head = head.next

        return False




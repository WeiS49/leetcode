# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        Node = ListNode(None)
        result = Node # 变量result指向实例Node的地址(所以是动态的)
        lx = l1
        # print(lx.val)
        # print(lx) # 此时的lx的值是整个l1链表
        # print(result.next)
        # print('------')
        # print(l1)
        while l1 and l2:
            if l1.val < l2.val:
                print(l1)
                Node.next = l1  # 考虑链表的结构, 每次下一位地址都会变(包括l1和Node), (全部赋值)
                print(l1)
                l1 = l1.next  
                print(l1)
            else:
                # print(lx)
                Node.next = l2 
                l2 = l2.next
                # print(l2)
            # print(lx)
            # print(result.next)
            print('--')
            Node = Node.next
        
        if l1:
            Node.next = l1
        if l2:
            Node.next = l2
        
        Nodex = ListNode(9)
        Node.next = Nodex
        
        # print(l2)
        # print(lx)
        # print(result.next)
        
        return result.next
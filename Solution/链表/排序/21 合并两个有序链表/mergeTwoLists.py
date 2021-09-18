
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        Node = ListNode(None)
        result = Node # 这里保存的是当前状态, 是动态变化的值
        print(result)
        while l1 and l2:
            if l1.val < l2.val:
                Node.next = l1  # 每次都把剩下的所有内容作为地址赋给Node, 思考链表的构成(所以每次next值都会变, 包括lx)
                l1 = l1.next    # l1也会被影响, 但每次都会被重新赋值
            else:
                Node.next = l2
                l2 = l2.next
            Node = Node.next
            #print(result.val)

        if l1:
            Node.next = l1
        if l2:
            Node.next = l2
        #print(type(result))
        Node2 = ListNode(6)
        Node.next = Node2
        print(result)
        return result

l1 = [1, 3, 4]
l2 = [1, 2, 4]
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

nodex = ListNode(1)
nodex.next = node2
nodex.next.next = node4
print(type(nodex))

solution = Solution()

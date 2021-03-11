
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 解法1 快慢指针

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    Node = ListNode(0) # 声明哨兵节点
    Node.next = head # 哨兵节点指向给定链表(该节点本身就是一个链表)
    slow, fast = Node, Node
    count = 0   # count越大, 慢指针移动的越早

    while fast.next != None: # 当快指针到末尾(循环次数一定)
        if count >= n:  # 慢指针开始移动的条件
            slow = slow.next # 慢指针开始移动
        fast = fast.next    # 快指针移动
        count += 1  # 向慢指针移动条件趋近

    # 关键在于把握好快慢指针的距离
    
    x = slow.next
    slow.next = slow.next.next
    # print(head)
    return Node.next

# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         Node = ListNode(None)
#         Node.next = head
#         first,slow = Node, Node
#         for i in range(n):
#             first = first.next
#         while first.next != None:
#             first = first.next
#             slow = slow.next
#         slow.next = slow.next.next
#         return Node.next


node1 = ListNode([1,2,3,4,5])
# solution = Solution()
removeNthFromEnd(node1, 2)


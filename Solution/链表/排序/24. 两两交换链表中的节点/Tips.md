## 题干

* 题目的描述及输入输出案例(图片?)



## 相似

* LC147. 对链表进行插入排序

  * 重点去看pre.next的赋值, 该题事先没有对pre.next进行操作, 所以可以用
  * 但这道题LC24 就涉及了对pre.next进行操作, 所以不能直接赋值
  
```
  相似代码
  ```
  
  

## 心得

* 涉及到**对原链表进行修改**、而且**要求返回该链表中节点**的题目, 需要用到**哨兵节点**

* 链表的交换顺序 —— 先前再后

  * 让最靠前的节点指向后面(如果有多个节点就执行多次), 操作完毕后让后面的节点指向前面的节点

  ```
  # pre为最前面的节点, node1 node2是pre后面的两个节点, 目的是要交换它们
  node1 = pre.next
  node2 = pre.next.next
  
  pre = node2 # 因为不涉及多个节点, 所以可以写成pre = node1.next
  node1.next = node2.next 
  node2.next = node1 # 在这道题中可以写成node1, 如果node1、node2中有多个节点, 则需要写成pre.next
  pre = node1
  
  ```



* 对于链表题来说, 关键在于理清此时究竟应该**对哪个节点进行操作**, **用哪个节点赋值**

  * 如果某个节点之前已经进行过操作, 
  * 所以没有标准答案, 具体根据题目而定

  



## 参考资料

[官方题解](https://leetcode-cn.com/problems/swap-nodes-in-pairs/solution/liang-liang-jiao-huan-lian-biao-zhong-de-jie-di-91/)
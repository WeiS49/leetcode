## 题干

* 题目的描述及输入输出案例(图片?)



## 相似

* 同 LC206. 反转链表 相似

  ```
  tmp = cur.next
  cur.next = pre
pre = cur
  cur = tmp
  ```
  
  

## 心得

* 头插法

  * 将一个元素插入到头节点的下一个节点

  ```
  # L表示链表, p表示待插入节点
  p.next = L.next
  L.next = p
  ```

  * 上面这是头插法的标准代码, 可以看到对于链表节点的插入, **先处理**的是**后半部分的节点**, 后处理前半部分的节点

* 思路

  ```
  # pre: left节点的前一个节点
  ```

  * 将left节点后的每一个节点插入到pre和left之间, 使用头插法进行操作

  

* 需要注意的是, 在链表题中, 操作的每个元素都是**链表**(包含节点关系), 而不是单独的数字
  * 每次对节点n/n.next进行赋值操作, 都可能会改变整个链表的值(节点关系被修改)
  * 这就导致很多看上去对于单个数字成立的情况, 在链表赋值中可能会失败

```
1 cur = pre.next
2 for i in range(right - left - 1):
3	next = cur.next
4	cur.next = next.next
5	next.next = pre.next # 这里的pre.next看似等于cur, 但由于上一行代码对cur进行的操作, 导致不能这样赋值
6	pre.next = next
```

* 可以看到, 在第4行代码中, 对cur进行了操作, 此时cur != pre.next, 一定要注意这一点
  * 所以此时如果想要表示"pre的下一个节点", 不能使用cur, 而应该用pre.next
  * 在这里, 第5、6行代码等同于头插法的标准代码, 第4行是因为插入的节点本身就在链表中, 而不是一个独立的节点, 所以需要额外的一点操作, 但大体思路就是头插法的思路

## 参考资料

[官方题解](https://leetcode-cn.com/problems/reverse-linked-list-ii/solution/fan-zhuan-lian-biao-ii-by-leetcode-solut-teyq/)

[头插法讲解](https://blog.csdn.net/cainiaofu/article/details/108434499)
## 题干

* 题目的描述及输入输出案例(图片?)



## 相似

* LC92. 链表排序Ⅱ

  ```
  # 对链表中节点使用头插法
  next = cur.next
cur.next = next.next
  next.next = pre.next
  pre.next = next
  ```
  
  

## 心得

* 代码中的判断语句

  ```
  val = cur.next.val
  if p.next.val > val:
  	p = dummy # 将p置回原点
  ```

  * 为什么要写这句?

    * 因为p指向的是"头"节点, 而"头"节点是比cur.next节点小的**前一个节点**, 如果此时p.next.val > val, 则无法确定p是不是前一个结点, 所以需要置回原点重新查找
    * 这样做的原因是, 每轮"头插法"进行后, p节点的值都会被修改, 所以需要重新赋值, 而加上那句判断只是为了减少一些执行次数

    

* 对于链表结点排序这样的题目, 尤其是链表中的节点的重新排序, 有一部分代码是固定的, 就是**链表中节点的头插法**
  * 头插法的前提, 找到"**头**"
    * 对于92题来讲, "头"就是left节点的前一个节点
    * 而对于本题(147题), "头"就是最后一个比cur.next.val小的节点的**前一个节点**(因为涉及到从小到大排序)

​	



## 参考资料

[头插法](https://leetcode.com/problems/insertion-sort-list/discuss/46432/AC-Python-192ms-solution)
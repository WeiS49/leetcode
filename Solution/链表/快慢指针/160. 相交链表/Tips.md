## 题干

* 题目的描述及输入输出案例(图片?)



## 相似

* 和以前做过的题有什么相似之处

  ```
  相似代码
  ```

  

## 心得

* 两个思路:
  * 哈希表
    * 遍历其中一条链表headA, 将节点保存下来, 遍历另一条, 如果发现存在, 则找到, 否则没找到
    * 关键点: headA中节点作为key还是value? 这决定了之后遍历的内容
  * 双指针
    * 一条链表的节点值:
      * [1, 2, 3, 4, 5], 注意 5.next == null
      * 也就是说链表的末尾是null
    * 设定两个指针, 分别指向两个链表, 当一条指针指向链表末尾null时(判断此时指针指向null), 重新将它指向另一条链表
      * null == null -> 无交点
      * [x, y, z] == [x, y, z] -> 有交点
    * 分析
      * 无交点时, 两个指针分别走了两条链表总和(m+n)次
      * 有交点时, 分别走m + n(不重合), n + m(不重合) 次.



## 参考资料

[官方题解](https://leetcode-cn.com/problems/intersection-of-two-linked-lists/solution/xiang-jiao-lian-biao-by-leetcode-solutio-a8jn/)

[相交链表](https://leetcode-cn.com/problems/intersection-of-two-linked-lists/solution/intersection-of-two-linked-lists-shuang-zhi-zhen-l/)
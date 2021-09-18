## 题干

* 题目的描述及输入输出案例(图片?)



## 相似

* 和以前做过的题有什么相似之处

  ```
  相似代码
  ```

  

## 心得

* 在链表题中, 一定要注意**循环内指针的移动**

  * 一般来讲, 循环的条件是链表中还有节点

    ```
    while head:
    ```

  * 因此, 为了防止死循环, 在每次循环中, 链表的指针都要**向后移动**(根据题目, 移动步数可能不同)

    ```
    while head:
    	pass
    	head = head.next # 链表指针向后移动
    ```

    

​	



## 参考资料

[标准写法](https://leetcode-cn.com/problems/partition-list/solution/si-lu-jian-dan-yi-kan-jiu-dong-xing-neng-uf9p/)
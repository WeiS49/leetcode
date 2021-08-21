## 题干

* 题目的描述及输入输出案例(图片?)



## 相似

* 和以前做过的题有什么相似之处

  ```
  相似代码
  ```

  

## 心得

* 题目也有两种解法 —— 递归和模拟递归(用栈/队列来实现)

* 这种题一般都带有**回溯**的操作
  * 当遍历完某一条路径后, "弹出"操作列表中的最后一个值, 以此来遍历另一侧的节点

* 递归解法

  * 不符合条件的情况
    * 当前节点root为空
  * 符合条件的情况
    * root没有左 && 右节点
      * 加入结果
    * 有左 || 右节点
      * 递归进行

  

* 模拟递归解法, 通过值的传递来简介达到这种效果.
  * 在静态语言中, 这些操作可以通过指针操作进行处理
  * 层序遍历使用**队列**进行处理.
  * 使用列表paths存储**所有**可能的路线, 分别遍历左右节点(BFS), 将符合条件的值存储到paths中
  * ![](https://raw.githubusercontent.com/WeiS49/Bilder/main/img/leetcode/257_pic.png)	

```
input: [1, 2, 3, null, 5]
效果: 
paths = 
[1]
[3, 1->2]
[1->2, 1->3]
[1->3, 1->2->5]
end
```











## 参考资料

[题目分析](https://mp.weixin.qq.com/s/Osw4LQD2xVUnCJ-9jrYxJA)

[官方题解](https://leetcode-cn.com/problems/binary-tree-paths/solution/er-cha-shu-de-suo-you-lu-jing-by-leetcode-solution/)
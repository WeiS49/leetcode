## 题干

* 题目的描述及输入输出案例(图片?)



## 相似

* LC104. 二叉树的最大深度

  ```
  相似代码
  ```

  

## 心得

* 涉及套路
  * LC104. 二叉树的最大深度 —— 查找最大深度才能找到直径



* 这道题需要用到中间值来保存当前的最大值,  或者说这道题用中间值是一个更省力的做法, 否则就无从比较最大值了
  * 总要有之前的值和现在去比较才能体现出大小
* 与之相对的, LC104、LC111也可以用到中间值, 但没有必要, 因为最大、最小值总是要经过遍历才能找到的



* 涉及到左右边的最大路径, 算是LC104. 最大深度的二维版本了, 基本可以算是medium难度, 但由于实际操作步骤不算多, 所以被分到了easy.

* 主要的区别在于本题中增加了一个**比较大小**的步骤 —— 在搜索最大深度的同时, 使用一个变量保存当前最大的节点数

* 思路(depth函数)

  1. 递归左右节点, 获取它们的深度

  2. 使用中间值保存当前最大直径
     * 做比较 —— 当前最大直径 与 左右深度+当前节点

  3. 使用"罐头"递归查找二叉树的最大深度(只有获取了最大深度才能找到最大直径)



* 问题:

  * 为什么代码中有两次 "+1"

  ![](https://raw.githubusercontent.com/WeiS49/Bilder/main/img/leetcode/part/543_plusOne.png)

  * "+1"是为了存储当前节点(注意是在最后才存储)
  * 第一次"+1"是为了做比较, 第二次才是为了返回值, 功能不同, 不可混淆

​	



## 参考资料

[官方题解](https://leetcode-cn.com/problems/diameter-of-binary-tree/solution/er-cha-shu-de-zhi-jing-by-leetcode-solution/)

[官方题解的补充](https://leetcode-cn.com/problems/diameter-of-binary-tree/solution/shi-pin-jie-shi-di-gui-dai-ma-de-yun-xing-guo-chen/)
# [二叉树的最小深度](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/description/)

|  Category  |  Difficulty   | Likes | Dislikes |
| :--------: | :-----------: | :---: | :------: |
| algorithms | Easy (48.08%) |  549  |    -     |



给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

**说明：**叶子节点是指没有子节点的节点。

 

**示例 1：**

![img](https://assets.leetcode.com/uploads/2020/10/12/ex_depth.jpg)

```
输入：root = [3,9,20,null,null,15,7]
输出：2
```

**示例 2：**

```
输入：root = [2,null,3,null,4,null,5,null,6]
输出：5
```

## 相似

* 104. 二叉树的最大路径

  ![](https://raw.githubusercontent.com/WeiS49/Bilder/main/img/leetcode/solutions/104_recursion.png)

* 这道题因为是找最大路径, 可以省略掉有子节点的情况, 直接通到叶子节点去比较



## 心得

* 判断路径的题目(104、111), 参与判断的一定是到**根子节点**的情况

  * **特殊**: (想象特殊的二叉树: 链表, 在这种情况下, 最小路径不是1而是链表的长度)
  * 对于这道题来讲, 一定要判断所有的情况, 因为总是会出现**特殊情况**

  * 与之相对的, 104题, 可以不用判断(下面的第三种情况可以不写), 因为判断最大深度的时候会自动忽略深度较小的情况
  * **总结**: 找最大, 可以忽略小的; 找最小, 不能忽略所有情况, 因为小是比较出来的

* 对于二叉树的节点, 一共要考虑三种情况(完整的流程)

  1. 没有节点(not root): return 0

  2. 没有子节点(not root.left and not root.right): return 1

  3. 有子节点(可以用root.left or root.right做简化操作)

     * 有左子节点

       * 左子节点操作

     * 有右子节点

       * 右子节点操作

       

​	



## 参考资料

[递归解法](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/solution/li-jie-zhe-dao-ti-de-jie-shu-tiao-jian-by-user7208/)


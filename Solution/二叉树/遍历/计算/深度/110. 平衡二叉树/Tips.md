## 题干

* 题目的描述及输入输出案例(图片?)



## 相似

* LC104. 二叉树的最小深度

  * 这是标准的查找深度的递归写法, 本题在查找深度的同时, 海添加了节点的高度判断.
  * 如果高度差> 1, 则**中止递归, 返回False**
  
```
  def check(node):
  	while node:
  		if not node:
  			return 0
  		left = check(root.left)
  		right = check(root.right)
  		return max(left, right) + 1
  ```
  
  

## 心得

* 递归的终止条件
  * 比如这道题, 需要用递归去找到高度差>1的情况, 如果找到, 则不是平衡二叉树

​	



## 参考资料

[有价值的参考信息](https://leetcode-cn.com/)
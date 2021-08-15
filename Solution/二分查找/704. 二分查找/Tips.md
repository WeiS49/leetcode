# [二分查找](https://leetcode-cn.com/problems/binary-search/description/)

|  Category  |  Difficulty   | Likes | Dislikes |
| :--------: | :-----------: | :---: | :------: |
| algorithms | Easy (55.60%) |  307  |    -     |

给定一个 `n` 个元素有序的（升序）整型数组 `nums` 和一个目标值 `target` ，写一个函数搜索 `nums` 中的 `target`，如果目标值存在返回下标，否则返回 `-1`。


**示例 1:**

```
输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4
```

**示例 2:**

```
输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1
```

 

**提示：**

1. 你可以假设 `nums` 中的所有元素是不重复的。
2. `n` 将在 `[1, 10000]`之间。
3. `nums` 的每个元素都将在 `[-9999, 9999]`之间。



## 相似

* 和以前做过的题有什么相似之处

  ```
  相似代码
  ```

  

## 心得

* 虽然是最标准的二分查找, 但也有一些细节值得注意

  1. 整形溢出

     * 虽然不会在Python中出现, 但在C++/Java中可能会出现
     * 条件
       * mid = (low + high) // 2
       * 如果low和high足够大, 结果就可能溢出
     * 解决
       * mid = low + (high - low) // 2
       * 这种写法避免了溢出, 而上面的写法算是由此推导出来的

  2. 额外的判断

     * 正常的写法中, while循环会按照条件不断执行下去, 直到不符合条件

     * 添加一个判断, 可以有效减少语句的执行次数

       * 思路
         * 如果找到符合条件的值, 直接返回结果

       ```python
       if nums[mid] == target:
       	return mid
       ```

       

​	



## 参考资料

[官方题解, 评论](https://leetcode-cn.com/problems/binary-search/solution/er-fen-cha-zhao-by-leetcode/)
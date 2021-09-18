## 题干

* 题目的描述及输入输出案例(图片?)



## 相似

* 和以前做过的题有什么相似之处

  ```
  相似代码
  ```

  

## 心得

* 动态规划的初始化一般要提供一些余量
  * 比如len(给定内容) == s
  * 则len(dp) == s + 1/s + 2
  * 这是因为在动态规划的操作中, 在循环dp[i]时, 可能同时会对dp[i-1]或dp[i-2]进行操作, 如果len(dp) == s, 可能会导致溢出
    * 只设定len(dp) == s也是可以把题做出来的, 但可能思路不够罐头(也可能是另一种罐头), 所以也略过
    * 当然也可以对dp[i+1]、dp[i+2]进行操作,  不过这不太符合正常思路, 因此略过
  * 初始化dp时
    * 明确dp的目的, 可能的套路
      1. dp(int)
         * 这是比较常见的情况, 一般用在需要对dp中的值进行加减操作时
           * LC62
           * LC64
           * LC70
      2. dp(bool)
         * 在这道题中, dp就是bool类型, 需要用到dp去保存**是否能够进行操作**, 如果可以操作, 若dp[i] == True, 则进行下一步判断, 之后继续进行操作
           * LC139
    * dp赋初值
      * 根据题意要求, 一般会对dp[0]、dp[1]进行赋初值, 具体值根据上面的功能而定, 关键在于可以通过对初值的操作得到之后的值(找到某种规律)
        * 可行的做法是先手动对dp[2]、dp[3]进行推导, 得到结果后推广成公式, 写在代码中即可.



## 参考资料

[希望用一种规律搞定背包问题 - 单词拆分 - 力扣（LeetCode） (leetcode-cn.com)](https://leetcode-cn.com/problems/word-break/solution/xi-wang-yong-yi-chong-gui-lu-gao-ding-bei-bao-we-4/)

[动态规划+记忆化回溯 逐行解释 python3 - 单词拆分 - 力扣（LeetCode） (leetcode-cn.com)](https://leetcode-cn.com/problems/word-break/solution/dong-tai-gui-hua-ji-yi-hua-hui-su-zhu-xing-jie-shi/)
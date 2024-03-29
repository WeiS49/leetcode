## 题干

* 题目的描述及输入输出案例(图片?)



## 相似

* 和以前做过的题有什么相似之处

  ```
  相似代码
  ```

  

## 心得

* 这道题还是比较绕的, 主要在于这里的dp保存的和实际操作的并不是简单的数字, 而是用很多层"[ ]"包裹起来的字符串, 这就让题目看起来没有那么清晰, 但整体思路不变, 还是一道很标准的动态规划题目.



* 对于动态规划的题目, 首先是要想好要用dp表示的内容x, 其次就是根据x对dp的前几位进行初始化y, 然后根据这几个y的内容推出之后几位的内容, 找到规律, 之后再进行解题

  * 在本题中, 新加的"()"只能放在现有"()"的内部或右侧(也就是上一种可能性), 也就可以理解为上一种可能性的个数只能放在"()"的内部或右侧, 内部的个数a和外部的个数b之和 == 上一种可能性n-1

    ```
    a + b == n - 1
    ```

    

* 在循环嵌套中, 如果j(内存循环)的次数要比i(外层循环少), 或者说**i、j存在某种数学关系**, 可以计算出来

  * 则在某层循环中, j的循环次数随i的循环次数变化而变化

  ```
  for i in range(2, n + 1):	
  	for j in range(i):	# j的循环次数随i的递增而增加
  		pass
  # i - 1 = j + x -> x = i - j - 1
  ```

* 在本题中, i表示n == i时的情况, j表示内/外的可能性个数

  * 可以推出另一种的可能性个数为 i - j - 1
  * 则可以用[ j ]、[ i - j - 1 ]来分别表示当前内和外的括号个数



## 参考资料

[【最简单易懂的】动态规划 - 括号生成 - 力扣（LeetCode） (leetcode-cn.com)](https://leetcode-cn.com/problems/generate-parentheses/solution/zui-jian-dan-yi-dong-de-dong-tai-gui-hua-bu-lun-da/)
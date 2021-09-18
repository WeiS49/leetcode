#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
# 1. 初始化 hashMap_p保存s1的计数(保持不变) - 用作比较, hashMap用来保存s2的结果 - 循环操作
# 2. 设定左右边界
# 3. hashMap保存当前遍历的s1的值
# 4. 滑动窗口长度 > 字符串s1长度, 说明此时出现其他元素 - 执行删除操作 
# 5. 根据是否一致返回True/False
# Time: O(n) Space: O(n)

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        import collections

        hashMap = {}
        hashMap_p = {}

        hashMap_p = collections.Counter(s1)

        start = 0
        for end in range(len(s2)):
            content = s2[end]
            hashMap[content] = hashMap.get(content, 0) + 1

            if hashMap == hashMap_p:
                return True
            
            if end >= len(s1) - 1:
                head = s2[start]
                hashMap[head] -= 1
                if hashMap[head] == 0:
                    del hashMap[head]
                start += 1

        return False




# @lc code=end


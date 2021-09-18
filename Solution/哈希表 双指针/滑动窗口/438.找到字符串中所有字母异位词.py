#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
# 1. 初始化, hashMap_p用于比较, hashMap当前滑动窗口中的值
# 2. 设定左右窗口
# 3. 添加元素, 若内容相同则添加当前左侧索引
# 4. 窗口长度固定 - if, 左侧窗口移动, 保持窗口长度
# 5. 返回ans
# Time: O(n) Space: O(n)
# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        import collections

        ans, hashMap = [], {} 
        hashMap_p = {}

        hashMap_p = collections.Counter(p)

        start = 0
        for end in range(len(s)):
            content = s[end]
            hashMap[content] = hashMap.get(content, 0) + 1

            if hashMap == hashMap_p:
                ans.append(start)
            # 因为滑动窗口是固定长度, 所以用if
            # 维持滑动窗口长度
            if end >= len(p) - 1:
                head = s[start]
                hashMap[head] -= 1
                if hashMap[head] == 0:
                    del hashMap[head]
                start += 1

        return ans









        # index, ans, str = 0, [], ""

        # start = 0
        # for end in range(len(s)):
        #     str += s[end]
        #     if str == p:
        #         ans.append(start)
            
        #     if len(str) > len(p):
        #         str = str[1:]
        #         start += 1

        # return ans


# @lc code=end


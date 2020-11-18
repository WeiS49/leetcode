# 输入: [-1,0,1,2,-1,-4]
# 返回结果：[[-1,-1,2],[-1,0,1]]

class Solution:
    def threeSum(self, nums: list):
        res = []
        length = len(nums)
        if length < 3:
            return res
        nums.sort()
        for i in range(length):
            if nums[i] > 0:
                return res
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            L = i + 1
            R = length - 1
            while L < R:
                total = nums[i] + nums[L] + nums[R]
                if total > 0:
                    R -= 1
                elif total < 0:
                    L += 1
                else:
                    res.append([nums[i], nums[L], nums[R]])
                    while nums[R] == nums[R - 1] and L < R:
                        R -= 1
                    while nums[L] == nums[L + 1] and L < R:
                        L += 1
                    L += 1
                    R -= 1
        return res


answer1 = [-1,0,1,2,-1,-4]
solution = Solution()
print(solution.threeSum(answer1))



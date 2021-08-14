# 输入: [-1,0,1,2,-1,-4]
# 返回结果：[[-1,-1,2],[-1,0,1]]

class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []
        if len(nums) < 3:
            return []
        for n in range(len(nums)):
            if nums[n] > 0:
                return res
            if n > 0 and nums[n] == nums[n-1]:
                continue
            i = n + 1
            j = len(nums) - 1
            while i < j:
                total = nums[n] + nums[i] + nums[j]
                if total == 0:
                    res.append([nums[n], nums[i], nums[j]])
                    while i < j and nums[i] == nums[i + 1]:
                        i += 1
                    while i < j and nums[j] == nums[j - 1]:
                        j -= 1
                    i += 1
                    j -= 1

                elif total > 0:
                    j -= 1

                else:
                    i += 1
        return res

answer1 = [-1,0,1,2,-1,-4]
solution = Solution()
print(solution.threeSum(answer1))



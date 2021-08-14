
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a, b = 0, 0
        while a < len(nums):
            if nums[a] != nums[a + 1]:
                b += 1
                nums[b] = nums[a]

        return b+1
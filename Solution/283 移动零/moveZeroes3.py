
def moveZero(nums):
    # j = 0   # j指向遇到的第一个零
    # for i in range(len(nums)):
    #     if nums[i] != 0:
    #         nums[i], nums[j] = nums[j], nums[i]
    #         j += 1

    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if nums[j] == 0:
                nums[j], nums[j+1] = nums[j+1], nums[j]

    return nums

nums = [0, 1, 0, 3, 12]
answer = moveZero(nums)
print(answer)





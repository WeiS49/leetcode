def moveZero(nums: list):

    for i in range(len(nums)):
        if nums[i] == 0:
            nums.remove(0)
            nums.append(0)
    return nums

nums = [0, 1, 0, 3, 12]
answer = moveZero(nums)
print(answer)



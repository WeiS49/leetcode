def twosum(nums, target):
    nums.sort()
    print(nums)
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    # print(listx, type(listx))

listx = [3, 2, 4]
answer = twosum(listx, 6)
print(answer)
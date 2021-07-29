
nums = [2, 7, 11, 15]
target = 9
nums.sort()
listx = []

pivot = 0
while nums[pivot] < 0:  # 如果第一个值大于零 就没有必要继续
    i = pivot + 1   # 头指针为基准值的下一位
    j = len(nums) - 1   # 尾指针为列表末尾元素
    while i < j:

        if i < j and nums[i] == nums[i + 1]:
            i += 1
        if i < j and nums[j] == nums[j - 1]:
            j -= 1

        if nums[pivot] + nums[i] + nums[j] > 0:
            j -= 1
        elif nums[pivot] + nums[i] + nums[j] < 0:
            i += 1
        else:
            listx.append()



    i += 1







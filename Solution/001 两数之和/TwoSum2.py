def TwoSum(nums:list, target):
    j = -1
    for i in range(len(nums)):
        num1 = nums[i]
        num2 = target - num1
        # if num2 in nums[i+1:] and nums.count(num2) != 1:
        #     index = nums.index(num2, i+1)
        #     return [i, index]
        # else:
        #     continue
        if num2 in nums[i+1:]:
            if nums.count(num2) == 1 and num2 == num1:
                continue
            else:
                j = nums.index(num2, i + 1)
                break
            # j = nums.index(num2, i + 1)
    if j > 0:
        return [i, j]
    else:
        return []
        #         return [i,j]



list1 = [2, 7, 11, 15]
answer1 = TwoSum(list1, 9)
print(answer1)

list2 = [3, 3]
answer2 = TwoSum(list2, 6)
print(answer2)

list3 = [3, 2, 4]
answer3 = TwoSum(list3, 6)
print(answer3)

list4 = [2, 5, 5, 11]
answer4 = TwoSum(list4, 10)
print(answer4)





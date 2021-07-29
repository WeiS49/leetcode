def TwoSum(nums: list, target: int):
    j = -1
    for i in range(len(nums)):
        num1 = nums[i]
        num2 = target - num1
        
        if num2 in nums[i+1:]:

            j = nums.index(num2, i + 1)
            break

    if j > 0:
        return [i, j]
    else:
        print(j)
        return []

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



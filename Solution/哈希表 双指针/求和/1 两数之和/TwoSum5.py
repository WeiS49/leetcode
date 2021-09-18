def TwoSum(nums, target):
    hashmap={}
    for i,num in enumerate(nums):
        if hashmap.get(target - num) is not None:
            return [hashmap.get(target - num), i]
        hashmap[num] = i 

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
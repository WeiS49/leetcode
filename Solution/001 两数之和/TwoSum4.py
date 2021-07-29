
from typing import NamedTuple


def TwoSum(nums: list, target: int):
    hashmap = {}
    for ind, num in enumerate(nums):    # 把列表的结构用字典表示
        hashmap[num] = ind
    # return hashmap
    for i, num in enumerate(nums):
        j = hashmap.get(target - nums[i])
        if j is not None:
            return [i, j]


    # hsahmap = {}
    # for ind, num in enumerate(nums):
    #     hsahmap[num] = ind

    # return hsahmap
    
    # return hashmap






# list1 = [2, 7, 11, 15]
# answer1 = TwoSum(list1, 9)
# print(answer1)

# list2 = [3, 3]
# answer2 = TwoSum(list2, 6)
# print(answer2)

list3 = [3, 2, 4]
answer3 = TwoSum(list3, 6)
print(answer3)

# list4 = [2, 5, 5, 11]
# answer4 = TwoSum(list4, 10)
# print(answer4)








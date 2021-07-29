
def moveZero(nums):
    j = 0   # j指向遇到的第一个零
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1

    return nums

nums = [0, 1, 0, 3, 12]
answer = moveZero(nums)
print(answer)


for i in range(len(nums))
    a = nums[i]
    b = nums[i+1]
if 0:
    switch(a,b)






#     hashmap = {}
#     for ind, num in enumerate(nums):
#         hashmap[num] = ind

#     for num in hashmap.keys():
#         if num == 0:
#             # temp = nums.pop(hashmap[])
#             temp = hashmap.pop(num)
#             hashmap.update(0, temp)

    # for num in nums:
        # if num == 0:
            
            


# nums = [0, 1, 0, 3, 12]

# test = {1:0,2:1}
# temp = test.pop(1)
# print(temp)

# test.update(0,temp)
# print(temp)

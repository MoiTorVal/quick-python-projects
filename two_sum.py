# def twoSum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return  [i, j]

                       
    
    
# print(twoSum([2,7,11,15], 9))

def twoSum(nums, target ):
    hash_map = {}

    for index, value in enumerate(nums):
        diff = target -  value
        if diff in hash_map:
            return [hash_map[diff], index]
        hash_map[value] = index 




print(twoSum([2,7,11,15], 9))
# hash_map = {}

# hash_map["key"] = "value"

# print(hash_map["key"])
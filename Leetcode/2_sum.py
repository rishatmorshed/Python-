def twoSum(nums, target):
    dict = {}
    for key, value in enumerate(nums):
        dict[value] = key
    for key, value in enumerate(nums):
        ans = target-value
        if ans in dict and dict[ans] != key:
            return key, dict[ans]

nums = [2,7,11,15]
target = 20
indexes = twoSum(nums, target)
print(indexes)

#2nd method

def twoSum(nums, target):
    dict = {}
    for key, value in enumerate(nums):
        result = target-value
        if result in dict:
            return dict[result], key
        dict[value] = key
        print(key, value)

nums = [2,7,11,15]
target = 17
indexes = twoSum(nums, target)
print(indexes)
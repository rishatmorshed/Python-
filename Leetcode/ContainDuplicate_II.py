def containDuplicate_II(nums, k):
    dic = {}
    for i in range(len(nums)):
        if nums[i] in dic and i-dic[nums[i]] <=k:
            return True
        dic[nums[i]] = i
    return False
            
nums = [1,2,3,1,2,3]
k = 2
ans = containDuplicate_II(nums, k)
print(ans)
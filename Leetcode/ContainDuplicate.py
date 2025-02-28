def containDuplicate(nums):
    dic = {}
    for val in nums:
        if val in dic:
            return True
        dic[val] = True
    return False          
            
nums = [1,1,1,3,3,4,3,2,4,2]
ans = containDuplicate(nums)
print(ans)
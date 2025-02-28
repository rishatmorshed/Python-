def missingNumber(nums):
    size = len(nums)
    xor_all = 0
    for i in range(size+1):  #xor all element from 0 to N
        xor_all ^= i
    for num in nums:	     #xor all element in nums
        xor_all ^= num
    return xor_all           
            
nums = [9,6,4,2,3,5,8,0,1]
ans = missingNumber(nums)
print(ans)
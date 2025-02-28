### Method 1

def intersectionArray(nums1,m, nums2,n):   		#Time Complexity O(n)
    p1 = m-1						#Space Complexity O(n)
    p2 = n-1
    i = m+n-1
    while(p2 >= 0):
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[i] = nums1[p1]
            p1 -= 1
            i -= 1
        else:
            nums1[i] = nums2[p2]
            p2 -= 1
            i -= 1
    return(nums1)
        


nums1 = [1,2,3,0,0,0]
m,n = 3,3
nums2 = [2,5,6]
ans = intersectionArray(nums1,m, nums2,n)
print(ans)


###2nd Method 

def intersectionArray(nums1,m, nums2,n):
    new_num = nums1[0:m]
    new_num += nums2[0:n]		#Space Complexity O(n)
    new_num.sort()			#Time Complexity O(n log n)
    return new_num
        
nums1 = [1,2,3,0,0,0]
m,n = 3,3
nums2 = [2,5,6]
ans = intersectionArray(nums1,m, nums2,n)
print(ans)


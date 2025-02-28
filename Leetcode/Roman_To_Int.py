def romanToInt(s):
    dic = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
    ans = 0
    size = len(s)
    i = 0
    while i<size:						#Time Complexity O(n)
        if i<size-1 and dic[s[i]] < dic[s[i+1]]:		#Space Complexity O(1)
            ans += dic[s[i+1]] - dic[s[i]]
            i += 2
        else:
            ans += dic[s[i]]
            i += 1
    return ans
s = input()
ans = romanToInt(s)
print(ans)

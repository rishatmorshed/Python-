def isHappy(n):
    seen = {}  # Dictionary to track visited numbers
    while True: 					#Time Complexity: O(log n)
							#Space Complexity: O(1)
        digit_square_sum = 0
        while n != 0:
            digit_square_sum += (n % 10) ** 2
            n //= 10  # Use integer division
        
        if digit_square_sum == 1:
            return True
        
        n = digit_square_sum  # Update `n` to the new sum
        
        if n in seen:  # If we have seen this number before, it's a cycle
            return False
        seen[n] = True  # Mark the number as seen

n = int(input("Enter a number: "))
ans = isHappy(n)
print(ans)

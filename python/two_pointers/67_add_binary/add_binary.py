"""
we check if one string is longer then the other. We will traverse the longer string from the back
compare two values from a and b strings, but we have to convert string values to integers, and depending 
on the sum we will form our resulting string with prepending. Main logic of comparisons and bitwise
calculations: if total is >= 2, we put 1 into cary, if not we put 0. There is also a trick
how to utilize % and // operators for our solution. We know that there will be only 4 possible scenarios
for our total it's either 3, 2, 1 or 0. Thus we will prepend converted to string result of total % 2 to current result
0 % 2 = 0 no cary
1 % 2 = 1 no cary
2 % 2 = 0 with cary
3 % 2 = 1 with cary

And to calculate whether cary is 0 or 1 we will use // (floor division) operator. Discards decimal
part. In binary addition if sum exceeds 1 you carry 1 to the next position

0 // 2 = 0 cary 0
1 // 2 = 0 cary 0
2 // 2 = 1 cary 1
3 // 2 = 1 cary 1

First is a converted value, 2nd is b converted value, 3d is cary. 

0 + 0 + 0 = 0 <= 2 (cary is set to 0)
0 + 0 + 1 = 1 <= 2 (cary is set to 0)
0 + 1 + 0 = 1 <= 2 (cary is set to 0)
0 + 1 + 1 = 2 >= 2 (cary is set to 1)
1 + 0 + 0 = 1 <= 2 (cary is set to 0)
1 + 1 + 0 = 2 >= 2 (cary is set to 1)
1 + 0 + 1 = 2 >= 2 (cary is set to 1)
1 + 1 + 1 = 3 <= 2 (cary is set to 1)

"""

def add_binary(a, b):
    carry = 0
    result = ''
    
    # Iterate from the end, aligning the last digits
    i = len(a) - 1
    j = len(b) - 1
    
    while i >= 0 or j >= 0 or carry:
        # Get digits from a, default to 0 if out of bounds
        digit_a = int(a[i]) if i >= 0 else 0
        # Get digits from b, default to 0 if out of bounds
        digit_b = int(b[j]) if j >= 0 else 0
        
        # Calculate total sum with carry
        total = digit_a + digit_b + carry
        
        # Add the least significant bit to result
        result = str(total % 2) + result
        
        # Update carry for next iteration
        carry = total // 2
        
        # Move to the next position
        i -= 1
        j -= 1
    
    return result


t1 = add_binary('11', '1')
print(t1)
t2 = add_binary('1010', '1011')
print(t2)
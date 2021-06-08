def is_palindrome(s):
    if len(s) == 0:
        return True   # an empty string is a palindrome

    size = len(s)
    midpoint = size // 2
    
    for i in range(midpoint + 1):
        if s[i] != s[size - i - 1]:
            return False
    return True
is_palindrome("cat")
"""
TIME COMLEXITY 
len() function in Python runs in O(1) complexity.
O(1)+O(1)+O(1)+O(n)+O(1)
this program runs in linear time comlexity O(n)

SPACE COMLEXITY
memory alloaction occurs once hence  constant space depending on the input 

"""


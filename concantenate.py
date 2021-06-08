
def concatenate_arrays(A, B):
    result = []
    for x in A:
        result.append(x)
    for y in B:
        result.append(y)
    return result
"""
Time comlexity 
-------------
the time comlexity for the first loop occurs in linear time 
the second loop also happens in linear time 
therefore the time comlexity for the program is O(n)

space comlexity 
--------------
since there is a new memory location result 
the memory space might increase 
the space complexity is O(n)
"""
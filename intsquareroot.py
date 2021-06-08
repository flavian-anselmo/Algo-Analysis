def int_sqrt(x):
    for i in range(x):
        if i * i == x:
            return i
    
    return -1
"""
TIME COMLEXITY 
-------------
the loop runs in linear time 
the if statement is done in constant time 
with respect to the loop that runs in linear time O(n)
there for the timw complexity for the program is O(n)
this is slower than the bisection method since it has to check every value 

SPACE COMLEXITY 
---------------
The memory allocation is is conatant since initalisation occurs once 
hence the space comlexit is O(1)
"""
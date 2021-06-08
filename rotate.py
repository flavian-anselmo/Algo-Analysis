def rotate_left(A, d):
    for _ in range(d):
        first_item = A[0]
        for i in range(len(A)):
            A[i] = A[i + 1]
        A[-1] = first_item

"""
TIME COMPLEXITY 
---------------
The time comlexity for this program is O(n^2)
since the first loop runs in linear time
the second loop runs in linear time 
the initialization runa in constant time 

SPACE COMLEXITY 
--------------
Since there is new allocation of memory 
the space might incraese linearly
hence O(n)


"""
'''You are given an integer array heights where heights[i] represents the height of the ith bar.

You may choose any two bars to form a container. Return the maximum amount of water a container can store.'''

# Thoughts
    # Start with two pointers, one at the beginning and one at the end. 
    # Calculate the area between the two pointers.
    # Move the pointer that is shorter inward.
    # Update the max_water if the current area is greater.
    # Return the max_water.

# Code

# Extra that I missed

heights = [1,8,6,2,5,4,8,3,7]

max_water = 0
l = -0
r = len(heights)

while l<r:
    print(l,r)
    r-=1
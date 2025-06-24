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
    # Exactly as i did
heights = [2,2,2]

max_water = 0
l = -0
r = len(heights)-1

while l<r:
    distance  = r-l
    cap = min(heights[l],heights[r])
    area  = cap*distance
    print(cap,distance,area)
    max_water = max(max_water,area)
    if heights[l]< heights[r]:
        l +=1
    else:
        r-=1
print(max_water)
'''Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
Example 2:

Input: nums = [7,7], k = 1

Output: [7]'''

# Thoughts
    # freq hasmap will work
    # Sort by key, keep values as an array and return k elements

# Extra that I missed
    # Min-Heap
    # Bucket Sort

# nums = [1,2,2,3,3,3,4,4]
# k = 2

# from collections import Counter
# freq = Counter(nums)
# values_from_sorted = [k for k, v in sorted(freq.items(), key=lambda item: item[1], reverse= True)]
# print(values_from_sorted[:k])

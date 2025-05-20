# Thoughts
    # freq hasmap will work
    # we can use set and compare if it was before

# Extra that I missed
    # Sort and compare pairs
    # Compare length set vs original array

from collections import Counter
from typing import List 


# My solutions

# 1st solution using hashmap
# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         counter = Counter(nums)
#         for num, freq in counter.items():
#             if freq >1:
#                 return True

#         return False
# # Example usage
# if __name__ == "__main__":
#     solution = Solution()
#     nums = [1, 2, 3, 1]
#     print(solution.hasDuplicate(nums))  # Output: True
    
# 2nd solution using set
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_nums = set()
        for num in nums:
            if num in unique_nums:
                return True
            else:
                unique_nums.add(num)

        return False
    
# Example usage
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 1]
    print(solution.hasDuplicate(nums))  # Output: True


# Extra solutions:

# Sorting
# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         nums.sort()
#         for i in range(1, len(nums)):
#             if nums[i] == nums[i - 1]:
#                 return True
#         return False
    
# 4. Hash Set Length
# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         return len(set(nums)) < len(nums)
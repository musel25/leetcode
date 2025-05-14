from collections import Counter
from typing import List 

# 1st solution
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
    
# 2nd solution
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        for num, freq in counter.items():
            if freq >1:
                return True

        return False
# Example usage
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 1]
    print(solution.hasDuplicate(nums))  # Output: True
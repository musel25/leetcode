'''Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in 
O(n) time without using the division operation?

Example 1:

Input: nums = [1,2,4,6]

Output: [48,24,12,8]
Example 2:

Input: nums = [-1,0,1,2,3]

Output: [0,-6,0,0,0]'''

# Thoughts
    # You can iterate by brute force but the complexity its gonna be just too much
    # I can multiply all numbers then divide by the current. Account for special case when 0. Complexity 2n.
        # If there are 2 zeroes or more then zeroes for everyone, then edge case when only there is one zero.
# Extra that I missed
    # You can use Prefix & Suffix and make it optimal !!

# My solutions

# # nums = [1,2,4,6,0,0]
# nums = [-1,0,1,2,3]

# # Count number of zeroes
# num_of_zeroes = 0
# for num in nums:
#     if num ==0:
#         num_of_zeroes +=1

# # If only one zero skip it, otherwise do the full mult
# mult = 1
# if num_of_zeroes != 1:
#     for num in nums:
#         mult *= int(num)
    
# else:
#     for num in nums:
#         if num !=0:
#             mult *= int(num)

# out = []
# # If non zero exclude number normally, by division
# if num_of_zeroes == 0:
#     for num in nums:
#         out.append(int(mult/num))

# # If one zero, mult already stored the number excluded and for other numbers is 0
# elif num_of_zeroes == 1:
#     for num in nums:
#         if num == 0:
#             out.append(int(mult))
#         else:
#             out.append(0)

# # If two zero or more, pure zeroes
# else:
#     for num in nums:
#          out.append(0)

# print(out)


from typing import List 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        pref = [0] * n
        suff = [0] * n
        pref[0] = suff[n - 1] = 1
        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]
        for i in range(n - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        for i in range(n):
            res[i] = pref[i] * suff[i] 
        print(nums)
        print(pref)
        print(suff)
        return res
    
solution = Solution()
    
nums = [1,2,4,6]
result = solution.productExceptSelf(nums)
print(result)
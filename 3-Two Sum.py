'''Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Example 1:

Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]
'''
# Thoughts
    # Crear dic y buscamos si complemento existe key=num, value= Index
    # Iterar sobre nums buscando si complemento existe
    # Maybe tambien hay un ordered set que se pueda usar
    # Tiene que existir pareja porque si target 10 y tienes 5 podria haber error
    # Mejor checar mientras vas creando, pero elimnar ese cases

# Extra that I missed
# What i did was hash one pass, could be done also in two pass(exclude case where complement also has same index as the num you look)
# Sorting and two pointers from the ends, if equal return indices, if less than target move left pointer up, if greater move right pointer left.


# My Solution ONE PASS
# dic = {}
# for index,num in enumerate(nums):
#     complement = target-num
#     if complement in dic:
#         print([dic[complement], index])
#     else:
#         dic[num] = index
from typing import List 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i, num in enumerate(nums):
            A.append([num, i])
        
        A.sort()
        i, j = 0, len(nums) - 1
        while i < j:
            cur = A[i][0] + A[j][0]
            if cur == target:
                return [min(A[i][1], A[j][1]), 
                        max(A[i][1], A[j][1])]
            elif cur < target:
                i += 1
            else:
                j -= 1
        return []
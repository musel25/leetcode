'''Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [2,20,4,10,3,4,5]

Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:

Input: nums = [0,3,2,5,4,6,1,1]

Output: 7'''

# Thoughts
    # I create set. Then sort it. or use directly sorted set.
    # Then a for loop over the sorted set to verify continuous
    # you have to iterate over all array otherwise doesnt work because soution could be ahead, not in the beginning, cannot brea
    # Use a hasmap to save, lenghts and indices dont need both indices can recover by length, sort dict by length
    # Given we want only max value, then not need hasmap

# Extra that I missed
    # No need of both sorting and set. Only set enough, also can use hasmap key begining and value length.



nums=[0,3,2,5,4,6]

# set_nums = set(nums)
# sorted_set = sorted(set_nums)
# curr = 1
# len_sol  = 1
# prev = sorted_set[0]
# indices ={}
# for i in range(1,len(sorted_set)):
#     if sorted_set[i] == prev+1:
#         curr +=1
#         prev = sorted_set[i] 
#     else:
#         len_sol = max(len_sol, curr)
#         curr = 1
#         prev = sorted_set[i] 
# print(max(len_sol, curr))

set_nums = set(nums)
longest = 0
for num in nums:
    if num-1 not in set_nums:
        length = 1
        while (num + length) in set_nums:
            length += 1
        longest = max(length,longest)
print(longest)


# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         mp = defaultdict(int)
#         res = 0

#         for num in nums:
#             if not mp[num]:
#                 mp[num] = mp[num - 1] + mp[num + 1] + 1
#                 mp[num - mp[num - 1]] = mp[num]
#                 mp[num + mp[num + 1]] = mp[num]
#                 res = max(res, mp[num])
#         return res
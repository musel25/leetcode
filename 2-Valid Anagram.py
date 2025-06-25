'''Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
Example 2:

Input: s = "jar", t = "jam"

Output: false'''

# Thoughts
    # freq hasmap will work
        # Use counter
    # Sort and compare both words 
        # use sorted(), and compare arrays

# Extra that I missed
# Hash table. Using array. Each index in array is a letter.

# 1st
# from collections import Counter
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         s1 = Counter(s)
#         t1 = Counter(t)
#         return s1 ==t1

# 2nd
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
            
#         return sorted(s) == sorted(t)

# Hash Table
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False
        return True
'''Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:

Input: s = "tab a cat"

Output: false
Explanation: "tabacat" is not a palindrome.'''

# Thoughts
    # Convert all to lower case and remove spaces. Then 2 pointers both at the ends, meet at the midle, if they are always same true, false otherwise.

# Extra that I missed
    # Reverse string. 
    # in while loop condition, l < r


s = "Was it a car or a cat I saw?"


# s_array = [char for char in s.lower() if char.isalnum()]

# n = len(s_array)
# l = 0 
# r = n-1

# while l != n//2:
#     print(r)
#     if s_array[l] != s_array[r]:
#         print(False)
#     l +=1
#     r -=1
# print(True)

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         newStr = ''
#         for c in s:
#             if c.isalnum():
#                 newStr += c.lower()
#         return newStr == newStr[::-1]


s = ''.join([char for char in s.lower() if char.isalnum()])
print(s==s[::-1])
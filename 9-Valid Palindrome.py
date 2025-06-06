'''Given a string s, return true if it is a palindrome, otherwise return false.

'''

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
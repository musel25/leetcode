'''Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]'''

# Thoughts
    # Use pointers when one single words begin and ends, to decode
    # I will use a diccionary to encode and decorde, index will be the word and value accumulated, lenght of the word,

# Extra that I missed
    # Given that used i hasmap, which was ok. I wasnt able to convert it because i couldnt wrapped my head about how to delimit the words if there are special chars
    # The intuition here to transform my solution is, to first append the list of sizes and the word to be decoded, not intercaled as i first thought


# #### FIRST SOLUTION HASH MAP, BUT NOT POSSIBLE TO CHANGE FUNCTIONS

# # Encode
# Input= ["neet","code","love","you"]

# decode_map = {}
# encoded = ""
# value_index = -1
# for index, word in enumerate(Input):
#     encoded += word
#     value_index += len(word)
#     decode_map[index] = value_index

# print(encoded)
# print(decode_map)


# # Decode
# decoded_list = []
# key = 0
# value = 0
# word = ''
# for index_char, char in enumerate(encoded):
#     if index_char != decode_map[key]:
#         word += char
#     else:
#         word += char
#         decoded_list.append(word)
#         word = ''
#         key += 1
# print(decoded_list)


# solution
from typing import List 


# class Solution:
#     def encode(self, strs: List[str]) -> str:
#         if not strs:
#             return ""
#         sizes, res = [], ""
#         for s in strs:
#             sizes.append(len(s))
#         for sz in sizes:
#             res += str(sz)
#             res += ','
#         res += '#'
#         for s in strs:
#             res += s
#         return res

#     def decode(self, s: str) -> List[str]:
#         if not s:
#             return []
#         sizes, res, i = [], [], 0
#         while s[i] != '#':
#             cur = ""
#             while s[i] != ',':
#                 cur += s[i]
#                 i += 1
#             sizes.append(int(cur))
#             i += 1
#         i += 1
#         for sz in sizes:
#             res.append(s[i:i + sz])
#             i += sz
#         return res



# MINE ATTEMPT OPTIMAL

# input_strs = ["neetaaaaaa", "code", "love", "you"]


# encoded = ''
# for word in input_strs:
#     size = len(word)
#     encoded += str(size) + '#' + word
# print(encoded)


# decoded_list = []
# length = len(encoded)
# i = 0
# while i < length:
#     num_str = ''
#     while encoded[i] != "#":
#         num_str += encoded[i]
#         i += 1
#     i+=1
#     end_word = i+int(num_str)
#     print(i,end_word)
#     word = encoded[i:end_word]
#     decoded_list.append(word)
#     i = end_word

# print(decoded_list)







### REDO
# input_strs = ["neetaaaaaa", "code", "love", "you"]


# encoded = ''
# for word in input_strs:
#     size = len(word)
#     encoded += str(size) + '#' + word
# print(encoded)


# decoded_list = []
# length = len(encoded)
# i = 0
# while i < length:
#     num_str = ''
#     while encoded[i] != "#":
#         num_str += encoded[i]
#         i += 1
#     i+=1
#     end_word = i+int(num_str)
#     print(i,end_word)
#     word = encoded[i:end_word]
#     decoded_list.append(word)
#     i = end_word

# print(decoded_list)



# OPTIMAL
class Solution:
    
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res




solution = Solution()
    
# Test case 1: Basic string list
input_strs = ["neet", "code", "love", "you"]
encoded = solution.encode(input_strs)
decoded = solution.decode(encoded)

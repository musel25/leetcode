'''Given a string s, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: s = "zxyzxyz"

Output: 3
Explanation: The string "xyz" is the longest without duplicate characters.

Example 2:

Input: s = "xxxx"

Output: 1
'''
s = "zxyxabcde"

# Thoughts
    # You add every new letter to a dictionary, everytime you find a duplicated letter
    # you remove the letter from the dict, compute the len and keep track of the longest

# Extra that I missed
track = set()
max_len = 0
for char in s:
    if char in track:
        max_len = max(max_len, len(track))
        track.remove(char)
    track.add(char)

print(max_len)
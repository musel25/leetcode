'''Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
Example 2:

Input: strs = ["x"]

Output: [["x"]]
Example 3:

Input: strs = [""]

Output: [[""]]
'''

# Thoughts
    # hasmap, where key equal to ordered word
    # So for each word, we order it, then if not exist added to dict of anagrams as list.

# Extra that I missed
    # use defaultdict(list) to make it easier
    # Hash Table

# My solution 
    # strs = ["act","pots","tops","cat","stop","hat"]

    # dict_anagrams = {}
    # for str in strs:
    #     key = ''.join(sorted(str))
    #     if key not in dict_anagrams:
    #         dict_anagrams[key] = []
    #     dict_anagrams[key].append(str)

    # print(list(dict_anagrams.values()))
from collections import defaultdict
from typing import List 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())
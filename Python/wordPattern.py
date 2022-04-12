"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false

"""
# Solution
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        split = s.split()

        # base case - len of pattern should be same a num of words in s
        if len(split) != len(pattern): return False

        # create match string
        map = dict()
        match = list()
        for k, v in zip(pattern, split):
            if k not in map and v not in map.values():
                map[k] = v
            match.append(map.get(k, ''))
        return match == split

#Alternative slution - faster
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ls = s.split()
        if len(pattern) != len(ls): return False 
        d = dict()
        ds = set()
        for k,ss in enumerate(ls):
            if ss in d: 
                if d[ss]!=pattern[k]:break 
                continue 
            if pattern[k] in ds: break 
            d[ss] = pattern[k]
            ds.add(pattern[k])
        else:
            return True 
        return False       
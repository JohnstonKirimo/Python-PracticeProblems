"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.


Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

"""

#solution

 class Solution:
    def groupAnagrams(self, S: List[str]) -> List[List[str]]:

        d = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            d[key].append(word)
        return d.values()

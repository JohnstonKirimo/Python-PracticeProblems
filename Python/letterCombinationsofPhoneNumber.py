"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:

Input: digits = ""
Output: []

Example 3:

Input: digits = "2"
Output: ["a","b","c"]
"""

# solution 

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = { "2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        res = []
        l = len(digits)
        if l == 0:
            return []
        
        def helper(i,curr):
            if len(curr) == l:
                res.append(curr)
                return
            
            for j in dic[digits[i]]:
                helper(i+1,curr+j)
                
        helper(0,'')
        return res
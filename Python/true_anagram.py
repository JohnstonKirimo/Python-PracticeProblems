"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
"""

class Solution:
	def isAnagram(self, s: str, t: str) -> bool:

		frequecy_s = {}

		for i in range(len(s)):
			if s[i] not in frequecy_s:
				frequecy_s[s[i]] = 1
			else:
				frequecy_s[s[i]] = frequecy_s[s[i]] + 1

		frequecy_t = {}

		for i in range(len(t)):
			if t[i] not in frequecy_t:
				frequecy_t[t[i]] = 1
			else:
				frequecy_t[t[i]] = frequecy_t[t[i]] + 1

		if frequecy_s == frequecy_t:
			return True
		else:
			return False

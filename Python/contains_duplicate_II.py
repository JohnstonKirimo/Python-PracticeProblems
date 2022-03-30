"""
Given an integer array nums and an integer k,
return true if there are two distinct indices i and j in the array
such that nums[i] == nums[j] and abs(i - j) <= k.
"""
#Solution
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        D = {}

        for i,x in enumerate(nums):
            if x in D and abs(D[x] - i) <= k:
                return True
            D[x] = i

        return False
        

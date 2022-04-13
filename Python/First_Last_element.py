"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

"""
#solution
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(target):
            lo=0 ; hi=len(nums)-1    
            while lo<=hi:
                mid=(lo+hi)//2
                if nums[mid]<target: lo=mid+1
                else: hi=mid-1               
            return lo
        
        lo=binary_search(target) ; hi=binary_search(target+1)-1
        return [lo,hi] if lo<=hi else [-1,-1]

#Alternative solution
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=bisect_left(nums,target) ; r=bisect_right(nums,target)
        return [l,r-1] if l<r else [-1,-1]


"""
Given an integer n, return a binary string representing its representation in base -2.

Note that the returned string should not have leading zeros unless the string is "0".

 

Example 1:

Input: n = 2
Output: "110"
Explantion: (-2)2 + (-2)1 = 2
Example 2:

Input: n = 3
Output: "111"
Explantion: (-2)2 + (-2)1 + (-2)0 = 3
Example 3:

Input: n = 4
Output: "100"
Explantion: (-2)2 = 4

"""
#solution
class Solution:
    def baseNeg2(self, n: int) -> str:
        ans = ""
        while n != 0:
            if n%-2 != 0 :
                ans = '1' + ans
                n = (n-1)//-2
            else:
                ans = '0' + ans
                n = n//-2
        return ans if ans !="" else '0'
        
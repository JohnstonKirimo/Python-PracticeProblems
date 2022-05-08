"""
Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

Return the maximum product you can get.

Example 1:

Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:

Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
 

Constraints:

2 <= n <= 58
"""
#solution

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 1
        for i in range(2, n//2 + 2):
            p = n // i
            q = n % i
            temp = (p+1)**q * (p)**(i-q)
            res = max(res, temp)
        return res


# alternate solution
class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        res = collections.deque([1,1,2,0])
        for i in range(2, n-1):
            res[3] = max(2*res[1], 3*res[0], 2*i, 3*(i-1))
            res.rotate(-1)
        return res[2]
        
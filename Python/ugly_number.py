"""
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return true if n is an ugly number.
"""

#solution
class Solution:
    def isUgly(self, n: int) -> bool:
        return n>0 and (n==1 or (n%2==0 and self.isUgly(n//2)) or (n%3==0 and self.isUgly(n//3)) or (n%5==0 and self.isUgly(n//5)))
